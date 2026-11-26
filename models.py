'''用于数据模型定义（如：每日记录），描述数据模型的样子'''

from dataclasses import dataclass
from datetime import datetime

@dataclass
class 每日记录:
    '''封装一天的时间记录及相关计算结果。这是一个清晰的数据契约。'''
    # 原始输入数据
    睡眠: float
    学习: float
    娱乐: float
    运动: float
    
    # 计算派生数据（通过“__post_init__”自动计算）
    总时间: float = 0.0
    剩余时间: float = 0.0
    日期: str = ''       # 可以加入日期
    
    def __post_init__(self):
        '''在对象创建后自动执行，用于计算派生字段'''
        self.总时间 = self.睡眠 + self.学习 + self.娱乐 + self.运动
        self.剩余时间 = 24 - self.总时间
        if not self.日期:   # # 如果没提供日期，就用今天
            self.日期 = datetime.now().strftime('%Y-%m-%d-%a')