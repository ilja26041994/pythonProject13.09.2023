import random

def climbStairs(n):
    countOfSteps1 = 0
    countOfSteps2 = 0
    countOfSteps3 = 0
    while True:
        countOfSteps1 += 1
        if countOfSteps1 == n or countOfSteps1 == n + 1:
            break
        countOfSteps2 += 2
        if countOfSteps2 == n or countOfSteps2 == n + 1:
            break
        countOfSteps3 += random.randint(1, 2)
        if countOfSteps3 == n or countOfSteps3 == n + 1:
            break
    return (f'шагов по 2 ступени: {countOfSteps1}, шагов по 1 ступени: {countOfSteps2}, шагов по хз ступени: {countOfSteps3}')

