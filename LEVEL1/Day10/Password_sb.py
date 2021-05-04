def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    u_alpha = alphabet.upper()
    answer = ''
    for letter in s:
        if letter.isspace() == True:
            answer = answer + " "
        elif letter.islower() == True:
            position = alphabet.find(letter)
            newPosition = (position+n) % 26
            answer = answer + alphabet[newPosition]
        else:
            position = u_alpha.find(letter)
            newPosition = (position+n) % 26
            answer = answer + u_alpha[newPosition]
    return answer

s1 = "AB"
s2 = "z"
s3 = "a B z"

n1 = 1
n2 = 1
n3 = 4

print(solution(s1, n1))
print(solution(s2, n2))
print(solution(s3, n3))
