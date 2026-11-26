'''用于计算、保存、读取历史数据'''

from models import 每日记录

# 计算模块    
def 计算时间(睡眠, 学习, 娱乐, 运动) -> 每日记录:  # “-> 每日记录” 是类型提示，说明返回类型
    # 直接创建对象，总时间和剩余时间会自动计算！
    return 每日记录(睡眠 = 睡眠, 学习 = 学习, 娱乐 = 娱乐, 运动 = 运动)

# 数据存储模块
# 1. 写入数据到文件
def 保存今日数据(记录: 每日记录) -> None:
    '''将一条每日记录保存到CSV文件。'''
    print("=== 📁 学习文件操作 - 数据持久化的魔法 ===")
    
    # 准备数据行
    数据行 = f'\n{记录.日期}, {记录.睡眠}, {记录.学习}, {记录.娱乐}, {记录.运动}'
    
    # 写入文件（追加模式）
    with open ('时间记录.csv', 'a', encoding='utf-8') as f:
        f.write(数据行)
        
    print(f"💾 已保存今日数据到时间记录.csv")

# 2. 从文件读取历史数据
def 读取历史数据():
    try:
        with open('时间记录.csv', 'r', encoding='utf-8') as f:
            
            # 创建表头
            print('\n' + '='*20 + '📅 历史时间记录' + '='*20)
            记录数量 = 0
            for 行号,行 in enumerate(f,1):
                
                # 清理数据
                行 = 行.strip()
                
                # 跳过空行
                if not 行:
                    print(f'第{行号} 是空行, 已跳过')
                    continue
                
                # 分割数据
                数据列 = 行.split(',')
                
                # 验证数据格式
                if len(数据列) != 5:
                    print(f'⚠️  第{行号} 行格式错误: {行}')
                    print(f'原始数据: {repr(行)}')
                    print(f'数据类型: {type(行)}')
                    print(f'数据长度: {len(数据列)}\n')
                    continue
                
                # 数据解包
                日期, 睡眠, 学习, 娱乐, 运动 = 数据列
                
                # 显示记录
                print(f'📅 {日期} | 睡眠:{睡眠}h 学习:{学习}h 娱乐:{娱乐}h 运动:{运动}h\n')
                记录数量 += 1
            
            if 记录数量 == 0:
                print('暂无有效记录')
            else:
                print(f'共找到{记录数量} 条有效记录')           
    except FileNotFoundError:
        print('📝 还没有历史记录，开始你的第一笔记录吧！')
    except Exception as e:
        print(f'❌ 读取文件时出错: {e}')