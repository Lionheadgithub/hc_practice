hole_score = []

list1, list2 = [list(map(int, input().split(","))) for _ in range(2)]
for score_1, score_2 in zip(list1, list2):
    score = score_1 - score_2

    if score_1 <= 4 and score_2 == 1:
        hole_score.append("ホールインワン")
    elif score_1 == 5 and score_2 == 1:
        hole_score.append("コンドル")
    elif score_1 == 5 and score_2 == 2:
        hole_score.append("アルバトロス")
    elif score_2 == score_1 - 2:
        hole_score.append("イーグル")
    elif score_2 == score_1 - 1:
        hole_score.append("バーディ")
    elif score_1 == score_2:
        hole_score.append("パー")
    elif score < 0:
        hole_score.append("ボギー" if score == -1 else f"{-score}ボギー")
    else:
        print("score_1は3 <= score_1 <= 5, score_2は,1 <= score_1で入力して下さい")

print(",".join(hole_score))