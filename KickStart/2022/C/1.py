for case in range(1, int(input()) + 1):
    checks = [0, 0, 0, 0]
    special = ["#", "@", "*", "&"]
    baseLen = int(input())
    password = input()
    for char in password:
        if char.isnumeric():
            checks[0] = 1
        elif char.islower():
            checks[1] = 1
        elif char.isupper():
            checks[2] = 1
        elif char in special:
            checks[3] = 1

        if not 0 in checks:
            break

    if not checks[0]: password += "0"
    if not checks[1]: password += "a"
    if not checks[2]: password += "A"
    if not checks[3]: password += "#"

    if len(password) < 7:
        password += ("a" * (7 - len(password)))

    print("Case #{}: {}".format(case, password))