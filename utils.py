def div(a, b):
    if b == 0:
        return "0으로 나눌 수 없음"
    return a / b

def reverse(s):
    return s[::-1]

def is_even(n):
    if n % 2 ==0:
        return print("짝수입니다")
    elif n == 0:
        return print("0입니다")
    else:
        return print("홀수입니다")
