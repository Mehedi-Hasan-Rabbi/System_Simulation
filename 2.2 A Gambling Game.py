import math
import random

total_cost = 0
total_income = 0
n_simulatio = 100

for game in range(n_simulatio):
    sl_no = 0
    head = 0
    tail = 0
    while(True):
        sl_no += 1
        total_cost += 1
        r_num = random.randint(0, 9)

        if r_num < 5:
            head += 1
        else:
            tail += 1

        dif = abs(head-tail)

        if (dif == 3):
            print("Win 8 dollar cost", sl_no, "dollar")
            total_income += 8
            break;

print('Total Cost:',total_cost," Total Income:",total_income)
print("Each game on the average", math.ceil(total_cost/n_simulatio), "flip needed to win 8 dollar")