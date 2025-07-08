hole_score = []

list1, list2 = [list(map(int, input().split(","))) for _ in range(2)]
for hole, score in zip(list1, list2):
    SCORE_MAP = {-4: "コンドル", -3: "アルバトロス", -2: "イーグル", -1: "バーディ", 0: "パー",
                 1: "ボギー"}

    result = score - hole

    if hole <= 4 and score == 1:
        hole_score.append("ホールインワン")
        continue
    elif result >= 2:
        hole_score.append(f"{result}ボギー")
        continue
    game_score = SCORE_MAP.get(result)
    hole_score.append(game_score)

print(",".join(hole_score))