n = int(input())
group_num = 0
people = list(map(int, input().split()))

current_num = 0
for num in sorted(people):
    current_num += 1
    if current_num >= num:
        group_num += 1
        current_num = 0

print(group_num)
