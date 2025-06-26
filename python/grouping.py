import random

group = ["A", "B", "C", "D", "E", "F"]

pattern = random.choice([3, 2])
random_list1 = random.sample(group, pattern)
random_list2 = [v for v in group if not v in random_list1]

print(sorted(random_list1))
print(sorted(random_list2))