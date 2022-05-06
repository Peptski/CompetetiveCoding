for i in range(int(input())):
    answers = [ans for ans in input()]
    if not ("1" in answers or "0" in answers) or len(answers) <= 2:
        print(len(answers))
    else:
        one = 0
        dontKnow = 0
        for i, ans in enumerate(answers):
            if ans == "0":
                print(dontKnow + 1 + one)
                break
            elif ans == "1":
                one = 1
                dontKnow = 0
            else:
                dontKnow += 1 
        else:
            print(dontKnow + 1)