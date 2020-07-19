# 在螢幕上輸出姓名和成績
score = [80, 70, 90]  # 定義變數score
min_grade = None  # 定義變數min_grade是最低分
max_grade = None  # 定義變數max_grade是最高分
sum_grade = None  # 定義變數sum_grade是總分
print("我的名字是：小小。")  # 輸出相關資訊
print("我這次的語文成續：%d" % score[0])  # 輸出相關資訊
print("數學成續：%d" % score[1])  # 輸出相關資訊
print("英文成續：%d" % score[2])  # 輸出相關資訊
sum_grade = score[0] + score[1] + score[2]  # 求總分
avg_grade = sum_grade / 3  # 求平均分
min_grade = score.index(min(score))  # 最低分
max_grade = score.index(max(score))  # 最高分
