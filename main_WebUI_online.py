import argparse
import os, json
from tqdm import tqdm
from API import get_generator
from env import get_env
from Flow import get_flow
import multiprocessing
import traceback


def parse_args():
    parser = argparse.ArgumentParser("Mage Bench")
    parser.add_argument("--API-type", choices = ["HuggingFace", "OpenAI", "AzureOpenAI", "Local", "Gemini", "Claude"], required=True)
    parser.add_argument("--webui_online_type", type=str, default="Natural" , required=False)
    parser.add_argument("-hf", "--Human-Knowledge", default=False, action='store_true')
    
    parser.add_argument("--data-dir", type=str, default="./resources")
    parser.add_argument("--output-dir", type=str, default="./output")
    parser.add_argument("--init-dir", type=str, default="./output")
    parser.add_argument("--task-path", type=str, required=True, default=None, help="a path of the sub task, or a json containing paths to eval")
    parser.add_argument("--override", action='store_true', default=False, help="resume or regenerate")
    parser.add_argument("--model-no-system", action='store_true', default=False, help="the model has no system prompt")
    parser.add_argument("--repeat", default=1, type=int)
    parser.add_argument("--debug", action='store_true', default=False, help="debug mode")
    # api configs
    parser.add_argument("--model", default="gpt4o")
    parser.add_argument("--port", nargs='+', default=["8000"])
    parser.add_argument("--temperature", default=0.1, type=float)
    parser.add_argument("--top_p", default=0.95, type=float)
    parser.add_argument("--max_tokens", default=4000, type=int)
    parser.add_argument("--resolution", default=1920, type=int)
    parser.add_argument("--model_no_system", default=False, action='store_true')
    parser.add_argument("--max_image", default=10, type=int)
    parser.add_argument("--frequency_penalty", default=1.00, type=float)
    parser.add_argument("--n_workers", default=2, type=int)
    # online planing args
    parser.add_argument("--max_memory", default=20, type=int)
    parser.add_argument("--max_loop", default=4, type=int)
    parser.add_argument("--max_actions", default=1, type=int)

    args = parser.parse_args()
    return args

def main(ag):
    task_id, sub_task, repeat, args = ag
    out_path = sub_task[sub_task.rfind("/")+1:] if "/" in sub_task else sub_task
    if "." in out_path:
        out_path = out_path[:out_path.rfind(".")]
    outp_path = os.path.join(args.output_dir, out_path+f"_r{repeat}_loop1")
    if all([os.path.exists(os.path.join(args.output_dir, out_path+f"_r{repeat}_loop{r}/eval.json")) for r in range(1,6)]):
        return -1
        
    init_path = os.path.join(args.init_dir, out_path+f"_r{repeat}")  # need init dir in args !!!


    ENV_CLS, ACTION_CLS = get_env('WebUI')
    FLOW_CLS = get_flow(args)
    GENRATOR = get_generator(args)
    env = ENV_CLS(os.path.join(args.data_dir, sub_task), outp_path, args.resolution)

    # for online setting, we init from a global results
    env.start_from_exists(init_path)
    # assert env.trajectory.last_state.cur_html != ""

    flow = FLOW_CLS(
        generator = GENRATOR,
        env = env,
        generator_parameters = {
            "model": args.model,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "max_tokens": args.max_tokens,
            "frequency_penalty": args.frequency_penalty,
            "port": args.port[task_id%len(args.port)]
        },
        args = args
    )
    for r in range(3):
        if args.debug:
            res, details = flow.run(ACTION_CLS, args.model_no_system)
            break
        try:
            res, details = flow.run(ACTION_CLS, args.model_no_system)
            break
        except Exception as e:
            print(e)
            traceback.print_exc()  
            res = 0
    # env.Ending()
    return -1 # in this debug model, you have to calculate the avg score your own

def init(tqdm_lock):  
    global pbar  
    pbar = tqdm_lock 

def update(*a):  
    global pbar 
    pbar.update() 

if __name__ == "__main__":
    args = parse_args()
    num_workers = args.n_workers # multiprocessing.cpu_count() // 2

    if args.task_path.endswith(".json"):
        task_paths = json.load(open(args.task_path, encoding="utf-8"))
    elif args.task_path is not None:
        task_paths = [args.task_path]
    else:
        task_paths = [os.path.join(args.data_dir, f) for f in json.load(open(os.path.join(args.data_dir, args.env+"_all.json"), encoding="utf-8"))]
    
    results = []

    inp_args = [(it*args.repeat+irp, t, rp, args) for it, t in enumerate(task_paths) for irp, rp in enumerate(range(args.repeat))]

    with tqdm(total=len(inp_args)) as pbar:  
        tqdm_lock = pbar.get_lock()  
        with multiprocessing.Pool(processes=num_workers, initializer=init, initargs=(tqdm_lock,)) as pool:  
            results = []  
            for arg in inp_args:  
                result = pool.apply_async(main, args=(arg,), callback=lambda _: pbar.update())  
                results.append(result)  
              
            pool.close()  
            pool.join()  
          
        # Collect results  
        results = [r.get() for r in results]  
    
    print("All finished! Average results: ", sum(results) / len(results))
    # open(args.output_dir+"/res.txt", "w", encoding="utf-8").write(str(sum(results) / len(results)))




