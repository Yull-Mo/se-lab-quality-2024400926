# 重构后：消除重复代码 + 简化函数 + 删除无用变量
def calculate_score_info(score_list):
    """抽取公共逻辑：计算总分、平均分、最高分、最低分"""
    total = sum(score_list)
    count = len(score_list)
    max_score = max(score_list)
    min_score = min(score_list)
    avg = total / count
    return total, avg, max_score, min_score


def print_student_score(name, score_list):
    """统一输出学生成绩"""
    total, avg, max_score, min_score = calculate_score_info(score_list)
    print("学生：", name)
    print("总分：", total)
    print("平均分：", avg)
    print("最高分：", max_score)
    print("最低分：", min_score)


print_student_score("小明", [85, 92, 78, 90])
print_student_score("小红", [88, 95, 91, 89])
