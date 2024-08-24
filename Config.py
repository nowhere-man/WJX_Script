import random
import json
from ZM_IP import *

def select_Simple(question,choices):
    if 'affected_id' not in question:
        options = list(range(1, len(question['probabilities']) + 1))
        answer = random.choices(options, weights=question['probabilities'], k=1)[0]
    else:
        affected_id = question['affected_id']                # 受影响选项ID
        affected_value = choices[f'{affected_id}'][0]        # 受影响选项答案
        options = list(range(1, len(question['probabilities'][f'{affected_value}']) + 1))
        answer = random.choices(options, weights=question['probabilities'][f'{affected_value}'], k=1)[0]
    return [answer]

def select_Multiple(question,choices):
    options = list(range(1, len(question['probabilities']) + 1))
    # 使用random.choice选出3个，可能会重复，再用random.sample确保选择的答案不重复
    sampled_elements = random.choices(options, weights=question['probabilities'], k=3)
    seen = set()
    answers = [x for x in sampled_elements if x not in seen and not seen.add(x)]
    return answers

def select_Sort(question,choices):
    options = list(range(1, len(question['probabilities']) + 1))
    answers = random.sample(options, len(question['probabilities']))
    return answers

def select_Scale(question,choices):
    options = list(range(1, len(question['probabilities']) + 1))
    answer = random.choices(options, weights=question['probabilities'], k=1)[0]
    return [answer]

def input_Gap(question,choices):
    id = random.randint(1,3)
    answer = question['input'][f'{id}']
    return answer

class Config(object):
    def __init__(self):
        '''
        :param id: 题号
        :param type: 题目类型,Simple单选,Multiple多选,Sort排序,Scale量表,Gap填空
        :param affected_id: 受影响选项的题号
        :param probabilities: 题目选项的概率分布
        '''
        with open("config.json") as f:
            config = json.load(f)

        self.batch = config["batch"]
        self.proxy = config["proxy"]
        self.questions = config["questions"]



# TODO 自定义测试
if __name__ == "__main__":
    config = Config()
    # 答案汇总字典
    choices = {}
    # 遍历每个题目并选择答案
    for question in config.questions:
        id = question['id']
        if question['type'] == 'Simple':
            answers = select_Simple(question,choices)
        elif question['type'] == 'Multiple':
            answers = select_Multiple(question,choices)
        elif question['type'] == 'Sort':
            answers = select_Sort(question,choices)
        elif question['type'] == 'Scale':
            answers = select_Scale(question,choices)
        elif question['type'] == 'Gap':
            answers = input_Gap(question,choices)
        choices[f'{id}'] = answers
        print(f"For question {id}, the selected answer is: {answers}")
    print('Question selection presentation：',choices)

