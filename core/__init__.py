# 这是一个标识包
# 在 `core/__init__.py` 文件中写入：
from .input_handler import 验证并获取输入
from .analyzer import 智能分析, 综合评估, 能量守恒检查
from .data_manager import 计算时间, 保存今日数据, 读取历史数据

# 这样，在主程序中就可以直接从 `core` 包导入，而不需要深入子模块：
# from core import 验证并获取输入, 智能分析, 计算时间
# 这进一步封装了内部结构，让顶层代码更简洁。