# 代码坏味道：重复代码 + 函数过长 + 未使用变量
def calculate_student_score1(name, score_list):
    total = 0
    count = 0
    max_score = 0
    min_score = 100
    for s in score_list:
        total += s
        count += 1
        if s > max_score:
            max_score = s
        if s < min_score:
            min_score = s
    avg = total / count
    print("学生：", name)
    print("总分：", total)
    print("平均分：", avg)
    print("最高分：", max_score)
    print("最低分：", min_score)
    unused_var = 123  # 未使用变量


def calculate_student_score2(name, score_list):
    total = 0
    count = 0
    max_score = 0
    min_score = 100
    for s in score_list:
        total += s
        count += 1
        if s > max_score:
            max_score = s
        if s < min_score:
            min_score = s
    avg = total / count
    print("学生：", name)
    print("总分：", total)
    print("平均分：", avg)
    print("最高分：", max_score)
    print("最低分：", min_score)
    unused_var2 = 456  # 未使用变量


calculate_student_score1("小明", [85, 92, 78, 90])
calculate_student_score2("小红", [88, 95, 91, 89])
