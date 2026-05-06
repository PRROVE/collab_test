import utils

print("=============================================")
# 숫자 입력
a, b = map(int, input("두 숫자를 입력하세요: ").split())
print("=============================================")
n = input("1.add 2.sub 3.mul 4.div: ")
print("=============================================")
if n== 1:
    print(utils.add(a,b))
elif n== 2:
    print(utils.sub(a,b))
elif n== 3:
    print(utils.mul(a,b))
elif n== 4:
    print(utils.div(a,b))
print("=============================================")
# 문자열 입력
s = input("문자열을 입력하세요: ")
print("=============================================")
print("reverse:", utils.reverse(s))
print("is_even (숫자 기준):", utils.is_even(a))