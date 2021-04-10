# 암호 만들기
# https://www.acmicpc.net/problem/1759

from itertools import combinations


def is_valid(password):
    vowels = 'aeiou'
    vowel_num = 0

    for letter in password:
        if letter in vowels:
            vowel_num += 1

    if vowel_num < 1 or (len(password) - vowel_num) < 2:
        return False

    return True


l, c = map(int, input().split(' '))
letters = sorted(input().split(' '))
possible_passwords = []

for comb in combinations(letters, l):
    password = ''.join(comb)
    if is_valid(password):
        possible_passwords.append(password)

possible_passwords.sort()

for password in possible_passwords:
    print(password)
