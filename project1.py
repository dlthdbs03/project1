num1 = int(input("첫 번째 숫자를 입력해주세요: "))
op = input("연산을 입력해주세요: ")
num2 = int(input("두 번째 숫자를 입력해주세요: "))

result = 0

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("잘못 입력했습니다.")

print(result)

print("feature-branch2 충돌2")