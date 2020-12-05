def solution(phone_number):
    answer = '*' * (len(phone_number)-4) + phone_number[-4:]
    return answer

phone_number1 = "01033334444"
phone_number2 = "027778888"

print(solution(phone_number1))
print(solution(phone_number2))