n = int(input())

solution_known = list()

for i in range(n):
    arr = [int(x) for x in input().split()]
    solution_known.append(arr)

total_problems_solved = 0

for i in solution_known:
    if(i[0] + i[1] + i[2] >= 2):
        total_problems_solved += 1

print(total_problems_solved)
