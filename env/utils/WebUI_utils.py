from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener  
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  
import importlib.util  
import sys  
import numpy as np
from scipy.optimize import linear_sum_assignment 
import random
import os, json
import re
import atexit  

def check_px(x_res, y_res):
    x = float(x_res.strip("px"))
    y = float(y_res.strip("px"))
    relative_diff = abs(y-x)/x if x != 0 else float(y!=0)
    return 1-relative_diff if relative_diff < 1.0 else 0

def check_color(x_res, y_res):
    assert "rgb" in x_res and "rgb" in y_res
    x = [float(t) for t in x_res.split("(")[1].strip(")").split(", ")]   # for rgba, we dont want a
    y = [float(t) for t in y_res.split("(")[1].strip(")").split(", ")]
    MAX_CHANGE = 256
    return np.mean([max(1 - abs(x[i]-y[i])/MAX_CHANGE, 0) for i in range(3)])


def check_text(x, y):
    if len(x.strip().split(" "))<10:
        return x.strip().lower() == y.strip().lower()
    else:
        xx = x.strip().split(" ")
        yy = y.strip().split(" ")
        union = set(xx+yy)
        insert = set([k for k in xx if k in yy])
        return len(insert) / len(union)



color_type = lambda ty: [
        lambda x, y: 0 if check_color(x.value_of_css_property(ty), y.value_of_css_property(ty))>0.01 else -1,
        lambda x, y: check_color(x.value_of_css_property(ty), y.value_of_css_property(ty))
    ]

pixel_type = lambda ty: [
    lambda x, y: 0 if check_px(x.value_of_css_property(ty), y.value_of_css_property(ty))>0.01 else -1, lambda x, y: check_px(x.value_of_css_property(ty), y.value_of_css_property(ty))
]

choice_type = lambda ty: [lambda x, y: 0 if x.value_of_css_property(ty) == y.value_of_css_property(ty) else -1,
                         lambda x, y: x.value_of_css_property(ty) == y.value_of_css_property(ty)]




def box_shadow(x,y):
    def parse(k):
        ls = k.split(" ")
        c = " ".join(ls[:-5]) if "rgba(" in k else " ".join(ls[:-4])
        return c, ls[-4], ls[-3], ls[-2], ls[-1]
    xc, xt, xl, xb, xr = parse(x.value_of_css_property('box-shadow'))
    yc, yt, yl, yb, yr = parse(y.value_of_css_property('box-shadow'))
    c = check_color(xc, yc)
    t = check_px(xt, yt)
    l = check_px(xl, yl)
    b = check_px(xb, yb)
    r = check_px(xr, yr)
    return (c *2 + t + l + b + r ) / 6.0

def background_size(x, y):
    xw, xh = x.value_of_css_property('background-size').split(" ")
    yw, yh = y.value_of_css_property('background-size').split(" ")
    w = check_px(xw, yw)
    h = check_px(xh, yh)
    return (w+h)/2

def background_linear_gradient(x, y):
    x_gradient_colors = re.findall(r'rgb\(\d+, \d+, \d+\)', x.value_of_css_property('background'))
    y_gradient_colors = re.findall(r'rgb\(\d+, \d+, \d+\)', y.value_of_css_property('background'))
    cs = 0.0
    n = 0.0
    for xc, yc in zip(x_gradient_colors, y_gradient_colors):
        cs += check_color(xc, yc)
        n += 1
    if n == 0:
        raise RuntimeError
    return cs / n

def text_shadow(x, y):
    s, w = 0, 0
    if "rgb" in x.value_of_css_property('text-shadow'):
        xc = re.findall(r'rgba\(\d+, \d+, \d+, \d+\)', x.value_of_css_property('text-shadow')) + re.findall(r'rgb\(\d+, \d+, \d+\)', x.value_of_css_property('text-shadow'))
        yc = re.findall(r'rgba\(\d+, \d+, \d+, \d+\)', y.value_of_css_property('text-shadow')) + re.findall(r'rgb\(\d+, \d+, \d+\)', y.value_of_css_property('text-shadow'))
        if not len(xc) == len(yc): # ==1
            w += 2
        else:
            s += check_color(xc[0], yc[0]) * 2
            w += 2
    
    def filterpx(k):
        ks = k.value_of_css_property('text-shadow').split(" ")
        ks = list(filter(lambda x: x.endswith("px"), ks))
        return ks

    xs = filterpx(x)
    ys = filterpx(y)
    N = min(len(xs), len(ys))
    for i in range(N):
        s += check_px(xs[i], ys[i]) * 1
        w += 1
    if w == 0:
        raise RuntimeError
    return s / w 



CSS_element = {  # type: [weight, filter-method, eval-method
    'has_text': [44, lambda x, y: 0 if len(y.text.strip().split(" ")) >= 1 else -1, lambda x, y: 1 if len(y.text.strip().split(" ")) >= 1 else 0],
    'text': [
        6.8, lambda x, y: 0 if check_text(x.text, y.text) > 0.6 else -1,  lambda x, y: check_text(x.text, y.text)
    ],
    'placeholder': [
        6.8, lambda x, y: 0 if check_text(x.text, y.text) > 0.6 else -1,  lambda x, y: check_text(x.text, y.text)
    ],
    'value': [
        6.8, lambda x, y: 0 if check_text(x.text, y.text) > 0.6 else -1,  lambda x, y: check_text(x.text, y.text)
    ],
    'text-shadow': [83, None, text_shadow],
    'color': [30,] + color_type('color'),
    'background-color': [59.] + color_type('background-color'),
    'background-image': [12.6] + choice_type('background-image'),
    'background-repeat': [24.5] + choice_type('background-repeat'),
    'background-size': [14.3] + [None, background_size],
    'background-linear-gradient': [18, None, background_linear_gradient],
    'src': [12.6] + choice_type('src'),
    'type': [18.9] + choice_type('type'),
    'border-bottom-color': [16.9] + color_type('border-bottom-color'),
    'border-bottom-width': [2.1] + pixel_type('border-bottom-width'),
    'border-bottom-style': [79.2] + choice_type('border-bottom-style'),
    'border-bottom-left-radius': [100] + pixel_type('border-bottom-left-radius'),
    'border-bottom-right-radius': [100] + pixel_type('border-bottom-right-radius'),
    'border-right-color': [16.9] + color_type('border-right-color'),
    'border-right-style': [79.2] + choice_type('border-right-style'),
    'border-right-width': [2.1] + pixel_type('border-right-width'),
    'border-left-color': [16.9] + color_type('border-left-color'),
    'border-left-style': [79.2] + choice_type('border-left-style'),
    'border-left-width': [2.1] + pixel_type('border-left-width'),
    'border-top-color': [16.9] + color_type('border-top-color'),
    'border-top-width': [2.1] + pixel_type('border-left-width'),
    'border-top-style': [79.2] + choice_type('border-top-style'),
    'border-top-left-radius': [100] + pixel_type('border-top-left-radius'),
    'border-top-right-radius': [100] + pixel_type('border-top-right-radius'),
    'outline-style': [79.2] + choice_type('outline-style'),
    'outline-width': [2.1] + choice_type('outline-width'),
    'outline-color': [16.9] + color_type('outline-color'),
    'font-family': [94.6] + choice_type('font-family'),
    'font-size': [9.8] + pixel_type('font-size'),
    'font-style': [94.6] + choice_type('font-style'),
    'font-weight': [2.1] + choice_type('font-weight'),
    'height': [31.92] + pixel_type('height'),
    'width': [31.92] + pixel_type('width'),
    'tab-size': [50.8] + choice_type('tab-size'),
    'class': [66.6, lambda x, y: 0 if x.get_attribute("class") == y.get_attribute("class") else -1, None],
    'letter-spacing': [67] + pixel_type('letter-spacing'),
    'box-shadow': [56.7, None, box_shadow],
    'display': [51] + choice_type('display'),
}

ignore_element = ['padding', 'margin', 'left', 'position', 'transition', 'top', 'z-index', 'flex-wrap', 'justify-content', 'text-transform',
                  'transform', 'cursor', 'align-items', 'overflow', 'margin-right', 'margin-left', 'margin-top', 'margin-bottom', 'padding-right', 'padding-left', 'padding-top', 'padding-bottom']

def split_properties(prop, elemnt):
    
    if prop == "background":
        ps = []
        if 'linear-gradient' in elemnt.value_of_css_property('background'):
            ps += ['background-linear-gradient', 'background-color', 'background-repeat']
        return ps
    elif prop =="border-radius":
        return ["border-bottom-left-radius", "border-bottom-right-radius", "border-top-left-radius", "border-top-right-radius"]
    elif prop =="border":
        return ["border-bottom-width", "border-top-width", "border-left-width", "border-right-width"]
    elif prop in ["border-top", "border-down", "border-left", "border-right"]:
        return [f"{prop}-width", f"{prop}-color"]
    elif prop =="outline":
        return ['outline-style', 'outline-width', 'outline-color']
    else:
        return [prop]
    
class AlertHandlerListener(AbstractEventListener):  
    def before_click(self, element, driver):  
        self.handle_alert(driver)  
  
    def before_navigate_to(self, url, driver):  
        self.handle_alert(driver)  
  
    def before_navigate_back(self, driver):  
        self.handle_alert(driver)  
  
    def before_navigate_forward(self, driver):  
        self.handle_alert(driver)  
  
    def before_find(self, by, value, driver):  
        self.handle_alert(driver)  
  
    def handle_alert(self, driver):  
        try:  
            alert = driver.switch_to.alert  
            alert.accept()  
        except NoAlertPresentException:  
            # 没有弹出警告时捕获异常并记录日志  
            pass
        except UnexpectedAlertPresentException:  
            # 捕获意外的弹出警告并处理  
            alert = driver.switch_to.alert  
            alert.accept()  
        except Exception as e:  
            # 捕获其他所有异常并记录日志  
            print(f"An unexpected exception occurred: {e}")  

def get_driver(html):
    chrome_options = Options()  
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument('--no-sandbox')  
    chrome_options.add_argument('--disable-dev-shm-usage')  
    chrome_options.add_argument('--disable-gpu')  
    target_driver = webdriver.Chrome(options=chrome_options)
    target_driver = EventFiringWebDriver(target_driver, AlertHandlerListener())  
    target_driver.set_window_size(1920, 1080)
    html_file_path = os.path.abspath(html)
    target_driver.get(f'file://{html_file_path}') 
    atexit.register(target_driver.quit) 
    return target_driver


def get_elements_html(driver):  
    body = driver.find_element(By.TAG_NAME, 'body')
    elements = body.find_elements(By.CSS_SELECTOR, '*')  
    elements_html = {element: element.get_attribute('outerHTML') for element in elements}  
    return elements_html

def GIoU(target_element, generated_element):

    box1 = target_element.bounding_box[0] + target_element.bounding_box[1]
    box2 = generated_element.bounding_box[0] + generated_element.bounding_box[1]

    def area(box):
        return (box[2] - box[0] + 1) * (box[3] - box[1] + 1)

    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    box1_area = area(box1)
    box2_area = area(box2)

    union_area = box1_area + box2_area - intersection_area

    c_x1 = min(box1[0], box2[0])
    c_y1 = min(box1[1], box2[1])
    c_x2 = max(box1[2], box2[2])
    c_y2 = max(box1[3], box2[3])
    c_area = area((c_x1, c_y1, c_x2, c_y2))

    giou = intersection_area / union_area - (c_area - union_area) / c_area

    return giou


def GIOU_score(target_element, generated_element):

    box1 = target_element.bounding_box[0] + target_element.bounding_box[1]
    box2 = generated_element.bounding_box[0] + generated_element.bounding_box[1]

    def area(box):
        return (box[2] - box[0] + 1) * (box[3] - box[1] + 1)

    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    box1_area = area(box1)
    box2_area = area(box2)

    union_area = box1_area + box2_area - intersection_area

    if intersection_area > 0:
        return (intersection_area / min(box1_area, box2_area)) / 2 + 0.5

    c_x1 = min(box1[0], box2[0])
    c_y1 = min(box1[1], box2[1])
    c_x2 = max(box1[2], box2[2])
    c_y2 = max(box1[3], box2[3])
    c_area = area((c_x1, c_y1, c_x2, c_y2))

    giou = intersection_area / union_area - (c_area - union_area) / c_area

    return (giou + 1) / 2



def get_body_elements_info(driver, ):  
    body = driver.find_element(By.TAG_NAME, 'body')  # 获取<body>元素  
    html = driver.find_element(By.TAG_NAME, 'html') 
    html_space = (html.rect['width'], html.rect['height'])

    elements = body.find_elements(By.CSS_SELECTOR, '*')  # 获取<body>中的所有元素  
    all_elements = []  
  
    for element in elements:  

        rect = element.rect
        displayed = element.is_displayed()  
          
        x1 = rect['x']
        y1 = rect['y']
        x2 = x1 + rect['width']  
        y2 = y1 + rect['height']

        space = rect['width'] * rect['height']
          
        bounding_box = ((x1,y1), (x2,y2))
        element.bounding_box = bounding_box
        element.is_target_point = element.get_attribute('data-filter-by') is not None
        element.filter_method = element.get_attribute('data-filter-by')
        if element.is_target_point:
            element.eval_methods = element.get_attribute('data-evalby').split("|")
        element.space = space
  
        if space > 0.1 and displayed:
            all_elements.append(element)  
    return all_elements, html_space


from PIL import Image, ImageDraw  
  
def create_canvas_with_rectangles(space, rectangles):    
    canvas = Image.new('RGB', space, 'white')  
    draw = ImageDraw.Draw(canvas)  
      
    for rect in rectangles:  
        top_left, bottom_right = rect
        draw.rectangle([top_left, bottom_right], outline='black' if all([top_left[0]>0,top_left[1]>0,bottom_right[0]>0,bottom_right[1]>0]) else 'red')  
 
    canvas.save('canvas_with_rectangles_e2egpt.png')  

def draw_match(target_elements, generated_elements, match, space, tdir):
    '''return 4 image: origin_target, origin_generated, matched_target, matched_generated'''
    def randc(n_sample):
        import matplotlib.pyplot as plt  
        color_list = plt.cm.Dark2(np.linspace(0, 1, 50))
        cs = random.sample(list(color_list), n_sample)  
        return [(int(255*c[0]), int(255*c[1]), int(255*c[2])) for c in cs]
    # origin_target
    canvas = Image.new('RGB', space, 'white')  
    draw = ImageDraw.Draw(canvas)
    for e in target_elements:  
        draw.rectangle(e.bounding_box, outline='black', width=2)  
    canvas.save(os.path.join(tdir, 'origin_target.png')) 

    # origin_generated
    canvas = Image.new('RGB', space, 'white')  
    draw = ImageDraw.Draw(canvas)
    for e in generated_elements:  
        draw.rectangle(e.bounding_box, outline='black', width=2)  
    canvas.save(os.path.join(tdir, 'origin_generated.png')) 

    # matched_target & generated
    tcanvas = Image.new('RGB', space, 'white')  
    tdraw = ImageDraw.Draw(tcanvas)
    gcanvas = Image.new('RGB', space, 'white')  
    gdraw = ImageDraw.Draw(gcanvas)
    cs = randc(len(match))
    for idx, m in enumerate(match):
        te, ge  =  m
        c = cs[idx]
        tdraw.rectangle(te.bounding_box, outline=c, width=2)  
        gdraw.rectangle(ge.bounding_box, outline=c, width=2)  
    tcanvas.save(os.path.join(tdir, 'matched_target.png')) 
    gcanvas.save(os.path.join(tdir, 'matched_generated.png')) 




def parse_target_generation(target_driver, generated_driver):

    '''
    here we only consider a fixed state (e.g. after mouse click)
    '''
    target_elements, target_space = get_body_elements_info(target_driver)
    target_elements = list(filter(lambda x: x.is_target_point, target_elements))
    generated_elements, generated_space = get_body_elements_info(generated_driver)
    return target_elements, generated_elements, target_space


def get_cost_metrics(target_elements, generated_elements, threshold, penalty):
    '''return a T x G cost metric, lower is better'''
    cost = np.zeros(shape = (len(target_elements), len(generated_elements)))
    for t, te in enumerate(target_elements):
        filter_score_func = CSS_element[te.filter_method][1]
        for g, ge in enumerate(generated_elements):
            try:
                n_child = ge.find_elements(By.CSS_SELECTOR, '*') # not atomic element
            except:
                n_child = []
            try:
                fs = filter_score_func(te, ge)
            except:
                fs = -0.01
            cost[t][g] = (GIoU(te, ge) + fs - len(n_child)*1e-5)  # this is weight
            if cost[t][g] >= threshold:
                cost[t][g] = - cost[t][g]
            else:
                cost[t][g] = penalty
    return cost


def eval_static(target_driver, generated_driver, kept_element, debug_mode=False):
    target_elements, generated_elements, target_space = parse_target_generation(target_driver, generated_driver)
    # clean out kept element
    cleaned_elements = []
    for te in target_elements:
        if any([te.get_attribute('outerHTML') == ke.get_attribute('outerHTML') for ke in kept_element]) or te.filter_method not in CSS_element or CSS_element[te.filter_method][1] is None:
            pass
        else:
            cleaned_elements.append(te)
    target_elements = cleaned_elements

    threshold = -1.0 # weight

    cost = get_cost_metrics(target_elements, generated_elements, threshold, penalty=1e5)
    row_ind, col_ind = linear_sum_assignment(cost)  
      
    final_match = [(target_elements[i], generated_elements[j]) for i, j in zip(row_ind, col_ind) if cost[i, j] <= -threshold]
    unmatched_te = [target_elements[i] for i in range(len(target_elements)) if i not in row_ind]
    unmatched_ge = [generated_elements[i] for i in range(len(generated_elements)) if i not in col_ind]

    if debug_mode and kept_element == []:
        draw_match(target_elements, generated_elements, final_match, target_space, "./")
    
    score = 0.0
    space_w = 0.0
    detailed = dict()
    for m in final_match:
        te, ge = m
        try:
            html = te.get_attribute('outerHTML')
        except:
            continue
        if html in detailed:
            r = random.randint(1, 10086)
            en = html + f"repeat - {r}"
        else:
            en = html
        detailed[en] = dict()
        ss = 0.0
        all_w = 0.0 
        for method in te.eval_methods:
            if method in ignore_element:
                continue
            detailed[en][method] = dict()
            properties = split_properties(method, te)
            n_sucess = 0
            ps = 0.0
            pw = 0.0
            for p in properties:
                if p not in CSS_element:  
                    continue
                w, s_func = CSS_element[p][0], CSS_element[p][2]
                try:
                    ps += s_func(te, ge) * w
                    detailed[en][method][p] = [s_func(te, ge), w] 
                    pw += w
                    n_sucess += 1
                except Exception as e:
                    # print(method, p, e)
                    continue
            ss += ps / n_sucess if n_sucess > 0 else 0
            all_w += pw / n_sucess if n_sucess > 0 else 0
            
        # GIOU
        gs = GIOU_score(te, ge)
        ss += gs * 46   # 46 is a turned hyper parameter!!!!
        all_w += 46
        detailed[en]["GIOU"] = [gs, 46] 

        ss = ss / all_w
        
        sw = np.power(te.space, 0.8987018465995789)  # hyper parameter too
        detailed[en]["space"] = te.space
        score += ss * sw
        space_w += sw
    
    for te in unmatched_te:
        try:
            html = te.get_attribute('outerHTML')
        except:
            continue
        if html in detailed:
            r = random.randint(1, 10086)
            en = html + f"repeat - {r}"
        else:
            en = html
        detailed[en] = dict(space = te.space)
        sw = np.power(te.space, 0.8987018465995789)
        score += 0
        space_w += sw
    
    return score, space_w, detailed




def evaluate_different_interaction(target_html, generated_html, eval_py_path, debug_mode=False):
    sizes = (1920, 1080)
    spec = importlib.util.spec_from_file_location("external", eval_py_path)  
    external = importlib.util.module_from_spec(spec)  
    sys.modules["external"] = external  
    spec.loader.exec_module(external)
    actions = external.actions
    # parse target
    chrome_options = Options()  
    chrome_options.add_argument('--headless')  
    chrome_options.add_argument('--no-sandbox')  
    chrome_options.add_argument('--disable-dev-shm-usage')  
    chrome_options.add_argument('--disable-gpu')  
    target_driver = webdriver.Chrome(options=chrome_options)
    atexit.register(target_driver.quit) 
    target_driver = EventFiringWebDriver(target_driver, AlertHandlerListener())  
    target_driver.set_window_size(sizes[0], sizes[1])
    html_file_path = os.path.abspath(target_html)
    target_driver.get(f'file://{html_file_path}')  
    generated_driver = webdriver.Chrome(options=chrome_options)  
    atexit.register(generated_driver.quit) 
    generated_driver = EventFiringWebDriver(generated_driver, AlertHandlerListener())  
    generated_driver.set_window_size(sizes[0], sizes[1])
    html_file_path = os.path.abspath(generated_html)
    generated_driver.get(f'file://{html_file_path}')  
    
    before_ = get_elements_html(target_driver)
    kept_element = []
    
    _score, _weight, details = eval_static(target_driver, generated_driver, kept_element, debug_mode)
    
    score = [_score]
    weight = [_weight]
    all_details = dict(origin=[details, _score/_weight if _weight > 0 else 0])
    for act in actions:
        act(target_driver)
        action_success = False
        try:
            act(generated_driver)
            action_success = True
        except Exception as e:
            # print(f"generated html failed to perform action: {e}")
            pass
        after_ = get_elements_html(target_driver)
        kept_element = []  
        for element, html in before_.items():  
            if element in after_ and after_[element] == html:  
                kept_element.append(element)
        
        if action_success:
            _score, _weight, details = eval_static(target_driver, generated_driver, kept_element, debug_mode)
            all_details[act.__name__] = [details, _score/_weight if _weight > 0 else 0]
            score.append(_score)    
        else:
            _score, _weight, details = eval_static(target_driver, target_driver, kept_element, debug_mode)
            all_details[act.__name__] = ["action failed", details]
            score.append(0)
        
        before_ = after_
        weight.append(_weight)
        
    
    eval_result = sum(score)/sum(weight) if sum(weight)>0 else 0
    return eval_result, all_details
