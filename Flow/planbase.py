'''
Base class for a `plan`, which refer to a workflow that call LMMs and fulfill a task.
'''


class Plan():
    def __init__(self, generator, env, generator_parameters, args=None):
        self.generator = generator
        self.para = generator_parameters
        self.env = env
        self.task = self.env.task
        self.args = args

    def run(self, ):
        pass

    def special_prompt_for_task(self):
        return 
