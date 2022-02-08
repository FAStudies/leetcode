def remove_consecutive_repeating_characters(string):
    new_string = ""
    for i in range(len(string)):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            new_string += string[i]
    return new_string


def is_palindrome(string):
    new_string = ""
    for i in range(len(string)):
        if i == len(string) - 1 or string[i] != string[i + 1]:
            new_string += string[i]
    return new_string == new_string[::-1]


def permute(string):

    if len(string) == 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        char = string[i]
        sub_permutations = permute(string[:i] + string[i + 1:])

        for perm in sub_permutations:
            permutations.append(char + perm)
    return permutations


inp = input()
perms = permute(inp)
pals = []
for perm in perms:
    if is_palindrome(perm):
        pals.append(perm)

even = 0
odd = 0
for pal in pals:
    if len(pal) % 2 == 0:
        even += 1
    else:
        odd += 1

print(even, odd)
