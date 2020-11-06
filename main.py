
def solution(number):
    sum = 0
    for i in range(3, number, 3):
        sum += i
    for j in range(5, number, 5):
        if j % 3 != 0:
            sum += j
    return sum


print(solution(56))
