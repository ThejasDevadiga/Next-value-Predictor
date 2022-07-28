import numpy as np


def find_num(a1, a2, a3, a4, a5):
    global result
    c = 0
    if a1 == 'x': c += 1
    else: a1 = a1
    if a2 == 'x': c += 1
    else: a2 = a2
    if a3 == 'x': c += 1
    else: a3 = a3
    if a4 == 'x': c += 1
    else: a4 = a4
    if a5 == 'x': c += 1
    else: a5 = a5
    if c > 1:
        print(" <<More than two unknown number>> ")
    elif c ==0:
        print(" No unknown number found ")
    else:
        #If 1st letter is not given
        if a1 == 'x':
            print("[Step_1]")
            for l in (1, 2, 4, 5, 8, 10, 20, 40, 50, 80, 100, 200, 400, 500, 800, 1000):
                result = 0.5
                for n in range(1000000000000000):
                    A = ((a5 - n) ** (1. / l))
                    B = ((a4 - n) ** (1. / l))
                    C = ((a3 - n) ** (1. / l))
                    D = ((a2 - n) ** (1. / l))
                    b5 = a5 - n
                    b4 = a4 - n
                    b3 = a3 - n
                    b2 = a2 - n
                    if (b5 < 0) or (b4 < 0) or (b3 < 0) or (b2 < 0):
                        break
                    else:
                        x = A - B
                        y = B - C
                        z = C - D
                        h = abs(x) - abs(y)
                        i = abs(y) - abs(z)
                        j = i
                        if x < 0:
                            num = abs(x)
                        else:
                            num = x * (-1)
                        if z < 0:
                            nun = z - abs(j)
                        else:
                            nun = z - j
                        if x == y and y == z:
                            nun2 = D + num
                            a1 = (nun2 ** l) + n

                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a5)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a4)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [3] >>(", D, "**", l, "+", n, ")===>>", a2)
                            print("The 1st  number of this series will be>>(", nun2, "**", l, "+", n, ")===>", a1)

                            if a1 == round(a1):
                                result = a1
                                break
                        elif h == i:
                            nun1 = D - nun
                            a1 = (nun1 ** l) + n
                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a5)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a4)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [3] >>(", D, "**", l, "+", n, ")===>>", a2)
                            print("The 1st number of this series will be>>(", nun1, "**", l, "+", n, ")===>", a1)
                            if a1 == round(a1):
                                result = a1
                                break
                        else:
                            continue
                if result == round(result):
                    break
                else:

                    continue
            print("[Step_2]")
            for n in range(100):
                A = (np.cbrt(a5 - n))
                B = (np.cbrt(a4 - n))
                C = (np.cbrt(a3 - n))
                D = (np.cbrt(a2 - n))
                b5 = a5 - n
                b4 = a4 - n
                b3 = a3 - n
                b2 = a2 - n
                if b5 < 0 or b4 < 0 or b3 < 0 or b2 < 0:
                    break
                else:
                    x = A - B
                    y = B - C
                    z = C - D
                    h = abs(x) - abs(y)
                    i = abs(y) - abs(z)
                    j = i
                    if x < 0:
                        num = abs(x)
                    else:
                        num = x * (-1)
                    if z < 0:
                        nun = z - abs(j)
                    else:
                        nun = z - j
                    if x == y and y == z:
                        nun2 = D + num
                        a1 = (nun2 ** 3) + n

                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a5)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a4)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a3)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a2)
                        print("The next number of this series will be>>(", nun2, "**3 +", n, ")===>", a1)

                        if a1 == round(a1):
                            result = a1
                            break
                    elif h == i:
                        nun1 = D - nun
                        a1 = (nun1 ** 3) + n
                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a5)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a4)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a3)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a2)
                        print("The next number of this series will be>>", nun1, "**3 +", n, "===>", a1)
                        if a1 == round(a1):
                            result = a1
                            break
                    else:
                        continue
                if result == round(result):
                    break
                else:

                    continue
            print("[Step_3]")
            if a1 == 'x':
                r = a3/a2
                a1 = a2/r
                t2 = a1 * (r ** 1)
                t3 = a1 * (r ** 2)
                t4 = a1 * (r ** 3)
                t5 = a1 * (r ** 4)
                if (a2 == t2) and (a3 == t3) and (a4 == t4) and (a5 == t5):
                    print("Entered number [0] >>", a2)
                    print("Entered number [1] >>", a3)
                    print("Entered number [2] >>", a4)
                    print("Entered number [3] >>", a5)
                    print("The 1st number of this series will be>>", a1)
                    print("This is Geometrical progression[G.P]")

            print("[Step_4]")
            a11 = a5 - a3
            a1 = a3 - a11
            print("Entered number [0] >>", a5)
            print("Entered number [1] >>", a4)
            print("Entered number [2] >>", a3)
            print("Entered number [3] >>", a2)
            print("The 1st number of this series will be>>", a1)
            print("In this series>>[a,b,a+x,b+y,a+2x].So the 1st word [", a1, "]")

        #If 2nd Number is not given
        elif a2 == 'x':
            print("[Step_1]")
            for l in (1, 2, 4, 5, 8, 10, 20, 40, 50, 80, 100, 200, 400, 500, 800, 1000):
                result = 0.5
                for n in range(1000000000000000):
                    A = ((a1 - n) ** (1. / l))
                    C = ((a3 - n) ** (1. / l))
                    D = ((a4 - n) ** (1. / l))
                    E = ((a5 - n) ** (1. / l))
                    b1 = a1 - n
                    b2 = a3 - n
                    b3 = a4 - n
                    b4 = a5 - n
                    if (b1 < 0) or (b2 < 0) or (b3 < 0) or (b4 < 0):
                        break
                    else:
                        x = A - C
                        y = C - D
                        z = D - E
                        i = abs(y) - abs(z)
                        if y < 0:
                            num = abs(y)
                        else:
                            num = y * (-1)
                        if x == 2 * y and y == z:
                            B = A + num
                            a2 = (B ** l) + n

                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [2] >>(", B, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [3] >>(", C, "**", l, "+", n, ")===>>", a4)
                            print("Entered number [4] >>(", D, "**", l, "+", n, ")===>>", a5)
                            print("The 2nd number of this series will be>>(", B, "**", l, "+", n, ")===>", a2)

                            if a2 == round(a2):
                                result = a2
                                break
                        elif abs(i) >= 1:
                            x1  = abs(y) + i
                            if i == abs(i):
                                B = C + x1
                            else:
                                B = C - x1
                            a2 = (B ** l) + n
                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [1] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [2] >>(", D, "**", l, "+", n, ")===>>", a4)
                            print("Entered number [3] >>(", E, "**", l, "+", n, ")===>>", a5)
                            print("The 2nd  number of this series will be>>(", B, "**", l, "+", n, ")===>", a2)
                            if a2 == round(a2):
                                result = a2
                                break
                        else:
                            continue
                if result == round(result):
                    break
                else:

                    continue

            print("[Step_2]")
            for n in range(100):
                A = (np.cbrt(a1 - n))
                C = (np.cbrt(a3 - n))
                D = (np.cbrt(a4 - n))
                E = (np.cbrt(a5 - n))
                b1 = a1 - n
                b2 = a3 - n
                b3 = a4 - n
                b4 = a5 - n
                if b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0:
                    break
                else:
                    x = A - C
                    y = C - D
                    z = D - E
                    i = abs(y) - abs(z)
                    if y < 0:
                        num = abs(y)
                    else:
                        num = y * (-1)
                    if x == 2 * y and y == z:
                        B = A + num
                        a2 = (B**3) + n

                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(",C, "**3 +", n, ")===>>", a3)
                        print("Entered number [2] >>(", D, "**3 +", n, ")===>>", a4)
                        print("Entered number [3] >>(", E, "**3 +", n, ")===>>", a5)
                        print("The 2nd number of this series will be>>(", B, "**3 +", n, ")===>", a2)

                        if a2 == round(a2):
                            result = a2
                            break
                    elif abs(i) >= 1:

                        x1 = abs(y) + i
                        print(x1)
                        if i == abs(i):
                            B = C + x1
                        else:
                            B = C - x1
                        a2 = (B ** 3) + n
                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a3)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a4)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a5)
                        print("The next number of this series will be>>", B, "**3 +", n, "===>", a2)
                        if a2 == round(a2):
                            result = a2
                            break
                    else:
                        continue
                if result == round(result):
                    break
                else:

                    continue

            print("[Step_3]")
            if a1 > 0:
                a = a1
                r = a4/a3
                a2 = a * r
                t2 = a * (r ** 2)
                t3 = a * (r ** 3)
                t4 = a * (r ** 4)
                if (a5 == t4) and (a3 == t2) and (a4 == t3):
                    print("Entered number [0] >>", a1)
                    print("Entered number [1] >>", a3)
                    print("Entered number [2] >>", a4)
                    print("Entered number [3] >>", a5)
                    print("The 2nd  number of this series will be>>", a2)
                    print("This is Geometrical progression[G.P]")

        #If 3rd number is not given
        elif a3 == 'x':
            print("[Step_1]")
            for l in (1, 2, 4, 5, 8, 10, 20, 40, 50, 80, 100, 200, 400, 500, 800, 1000):
                result = 0.5
                for n in range(1000000000000000):
                    A = ((a1 - n) ** (1. / l))
                    B = ((a2 - n) ** (1. / l))
                    D = ((a4 - n) ** (1. / l))
                    E = ((a5 - n) ** (1. / l))
                    b1 = a1 - n
                    b2 = a2 - n
                    b3 = a4 - n
                    b4 = a5 - n
                    if (b1 < 0) or (b2 < 0) or (b3 < 0) or (b4 < 0):
                        break
                    else:
                        x = A - B
                        y = B - D
                        z = D - E
                        h = abs(x) + abs(z)
                        i = abs(x) - abs(z)
                        if x < 0:
                            num = abs(x)
                        else:
                            num = x * (-1)
                        if x == z and y == 2*z and y == 2*x:
                            C = B + num
                            a3 = (C ** l) + n

                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a2)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a4)
                            print("Entered number [3] >>(", D, "**", l, "+", n, ")===>>", a5)
                            print("The next number of this series will be>>(", C, "**", l, "+", n, ")===>", a3)

                            if a3 == round(a3):
                                result = a3
                                break
                        elif h == abs(y):
                            C = B+(num + (abs(i) / 3))
                            a3 = (C ** l) + n
                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a2)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a4)
                            print("Entered number [3] >>(", D, "**", l, "+", n, ")===>>", a5)
                            print("The next number of this series will be>>(", C, "**", l, "+", n, ")===>", a3)
                            if a3 == round(a3):
                                result = a3
                                break
                        else:
                            continue
                if result == round(result):
                    break
                else:

                    continue
            print("[Step_2]")
            for n in range(100):

                A = (np.cbrt(a1 - n))
                B = (np.cbrt(a2 - n))
                D = (np.cbrt(a4 - n))
                E = (np.cbrt(a5 - n))
                b1 = a1 - n
                b2 = a2 - n
                b3 = a4 - n
                b4 = a5 - n
                if b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0:
                    break
                else:
                    x = A - B
                    y = B - D
                    z = D - E
                    i = abs(y) - abs(z)
                    if y < 0:
                        num = abs(y)
                    else:
                        num = y * (-1)
                    if 2*x == y and x == z:
                        C = B + num
                        a3 = (C ** 3) + n

                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a2)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a4)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a5)
                        print("The 2nd number of this series will be>>(", B, "**3 +", n, ")===>", a3)

                        if a3 == round(a3):
                            result = a3
                            break
                    elif abs(i) == abs(x):
                        if abs(y) == ((abs(x)+1)+abs(x)+2):
                            C = (B + abs(x)+1)
                        elif abs(y) == ((abs(x)+2)+abs(x)+4):
                            C = (B + abs(x)+2)
                        else:
                            C = (B + abs(x)+n)

                        a3 = (C ** 3) + n
                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a2)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a4)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a5)
                        print("The next number of this series will be>>", C, "**3 +", n, "===>", a3)
                        if a3 == round(a3):
                            result = a3
                            break
                    else:
                        continue
                if result == round(result):
                    break
                else:

                    continue
            print("[Step_3]")
            if a1 > 0:
                a = a1
                r = a2/a1
                t2 = a * (r ** 1)
                t4 = a * (r ** 3)
                t5 = a * (r ** 4)
                a3 = a * (r ** 2)
                if (a5 == t5) and (a2 == t2) and (a4 == t4):
                    print("Entered number [0] >>", a1)
                    print("Entered number [1] >>", a2)
                    print("Entered number [2] >>", a4)
                    print("Entered number [3] >>", a5)
                    print("The 3rd  number of this series will be>>", a3)
                    print("This is Geometrical progression[G.P]")

            print("[Step_4]")
            a3 = (a1 + a5) / 2
            print("Entered number [0] >>", a1)
            print("Entered number [1] >>", a2)
            print("Entered number [2] >>", a4)
            print("Entered number [3] >>", a5)
            print("The 3rd number of this series will be>>", a3)
            print("In this series>>[a,b,a+x,b+y,a+2x].So the 1st word [", a3, "]")

        #If 4th number is not given
        elif a4 == 'x':
            print("[Step_1]")
            for l in (1, 2, 4, 5, 8, 10, 20, 40, 50, 80, 100, 200, 400, 500, 800, 1000):
                result = 0.5
                for n in range(1000000000000000):
                    A = ((a1 - n) ** (1. / l))
                    C = ((a3 - n) ** (1. / l))
                    B = ((a2 - n) ** (1. / l))
                    E = ((a5 - n) ** (1. / l))
                    b1 = a1 - n
                    b2 = a2 - n
                    b3 = a3 - n
                    b4 = a5 - n
                    if (b1 < 0) or (b2 < 0) or (b3 < 0) or (b4 < 0):
                        break
                    else:
                        z = C - E
                        y = B - C
                        x = A - B
                        i = abs(x) - abs(y)
                        if y < 0:
                            num = abs(y)
                        else:
                            num = y * (-1)
                        if z == 2 * x and y == x:
                            D = E + num
                            a4 = (D ** l) + n

                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [2] >>(", B, "**", l, "+", n, ")===>>", a2)
                            print("Entered number [3] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [4] >>(", E, "**", l, "+", n, ")===>>", a5)
                            print("The 2nd number of this series will be>>(", D, "**", l, "+", n, ")===>", a4)

                            if a4 == round(a4):
                                result = a4
                                break
                        elif abs(i) >= 1:

                            if i == abs(i):
                                x1 = y - i
                                D = C -  x1
                            else:
                                x1 = y + i
                                D = C - x1
                            a4 = (D ** l) + n
                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a2)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [3] >>(", E, "**", l, "+", n, ")===>>", a5)
                            print("The 4th  number of this series will be>>(", D, "**", l, "+", n, ")===>", a4)
                            if a4 == round(a4):
                                result = a4
                                break
                        else:
                            continue
                if result == round(result):
                    break
                else:
                    continue

            print("[Step_2]")
            for n in range(100):
                A = (np.cbrt(a1 - n))
                B = (np.cbrt(a2 - n))
                C = (np.cbrt(a3 - n))
                E = (np.cbrt(a5 - n))
                b1 = a1 - n
                b2 = a2 - n
                b3 = a3 - n
                b4 = a5 - n
                if b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0:
                    break
                else:
                    z = C - E
                    y = B - C
                    x = A - B
                    i = abs(x) - abs(y)
                    if y < 0:
                        num = abs(y)
                    else:
                        num = y * (-1)
                    if z == 2 * x and y == x:
                        D = E + num
                        a4 = (D ** 3) + n

                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a2)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a3)
                        print("Entered number [3] >>(", E, "**3 +", n, ")===>>", a5)
                        print("The 2nd number of this series will be>>(", D, "**3 +", n, ")===>", a4)

                        if a4 == round(a4):
                            result = a4
                            break
                    elif abs(i) >= 1:

                        if i == abs(i):
                            x1 = y - i
                            D = C - x1
                        else:
                            x1 = y + i
                            D = C - x1
                        a4 = (D ** 3) + n
                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a2)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a3)
                        print("Entered number [3] >>(", E, "**3 +", n, ")===>>", a5)
                        print("The next number of this series will be>>", D, "**3 +", n, "===>", a4)
                        if a4 == round(a4):
                            result = a4
                            break
                    else:
                        continue
                if result == round(result):
                    break
                else:
                    continue

            print("[Step_3]")
            if a1 > 0:
                a = a1
                r = a2/a1
                t3 = a * (r ** 2)
                t2 = a * (r ** 1)
                t5 = a * (r ** 4)
                a4 = a * (r ** 3)
                if (a5 == t5) and (a2 == t2) and (a3 == t3):
                    print("Entered number [0] >>", a1)
                    print("Entered number [1] >>", a2)
                    print("Entered number [2] >>", a3)
                    print("Entered number [3] >>", a5)
                    print("The 3rd  number of this series will be>>", a4)
                    print("This is Geometrical progression[G.P]")

        #If 5th number is Unknown
        elif a5=='x':
            print("[Step_1]")
            for l in (1, 2, 4, 5, 8, 10, 20, 40, 50, 80, 100, 200, 400, 500, 800, 1000):
                result = 0.5
                for n in range(1000000000000000):
                    A = ((a1 - n) ** (1. / l))
                    B = ((a2 - n) ** (1. / l))
                    C = ((a3 - n) ** (1. / l))
                    D = ((a4 - n) ** (1. / l))
                    b1 = a1 - n
                    b2 = a2 - n
                    b3 = a3 - n
                    b4 = a4 - n
                    if (b1 < 0) or (b2 < 0) or (b3 < 0) or (b4 < 0):
                        break
                    else:
                        x = A - B
                        y = B - C
                        z = C - D
                        h = abs(x) - abs(y)
                        i = abs(y) - abs(z)
                        j = i
                        if x < 0:
                            num = abs(x)
                        else:
                            num = x * (-1)
                        if z < 0:
                            nun = z - abs(j)
                        else:
                            nun = z - j
                        if x == y and y == z:
                            nun2 = D + num
                            a5 = (nun2 ** l) + n

                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a2)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [3] >>(", D, "**", l, "+", n, ")===>>", a4)
                            print("The next number of this series will be>>(", nun2, "**", l, "+", n, ")===>", a5)

                            if a5 == round(a5):
                                result = a5
                                break
                        elif h == i:
                            nun1 = D - nun
                            a5 = (nun1 ** l) + n
                            print("Entered number [0] >>(", A, "**", l, "+", n, ")===>>", a1)
                            print("Entered number [1] >>(", B, "**", l, "+", n, ")===>>", a2)
                            print("Entered number [2] >>(", C, "**", l, "+", n, ")===>>", a3)
                            print("Entered number [3] >>(", D, "**", l, "+", n, ")===>>", a4)
                            print("The next number of this series will be>>(", nun1, "**", l, "+", n, ")===>", a5)
                            if a5 == round(a5):
                                result = a5
                                break
                        else:
                            continue
                if result == round(result):
                    break
                else:

                    continue

            print("[Step_2]")
            for n in range(100):
                A = (np.cbrt(a1 - n))
                B = (np.cbrt(a2 - n))
                C = (np.cbrt(a3 - n))
                D = (np.cbrt(a4 - n))
                b1 = a1 - n
                b2 = a2 - n
                b3 = a3 - n
                b4 = a4 - n
                if b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0:
                    break
                else:
                    x = A - B
                    y = B - C
                    z = C - D
                    h = abs(x) - abs(y)
                    i = abs(y) - abs(z)
                    j = i
                    if x < 0:
                        num = abs(x)
                    else:
                        num = x * (-1)
                    if z < 0:
                        nun = z - abs(j)
                    else:
                        nun = z - j
                    if x == y and y == z:
                        nun2 = D + num
                        a5 = (nun2 ** 3) + n

                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a2)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a3)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a4)
                        print("The next number of this series will be>>(", nun2, "**3 +", n, ")===>", a5)

                        if a5 == round(a5):
                            result = a5
                            break
                    elif h == i:
                        nun1 = D - nun
                        a5 = (nun1 ** 3) + n
                        print("Entered number [0] >>(", A, "**3 +", n, ")===>>", a1)
                        print("Entered number [1] >>(", B, "**3 +", n, ")===>>", a2)
                        print("Entered number [2] >>(", C, "**3 +", n, ")===>>", a3)
                        print("Entered number [3] >>(", D, "**3 +", n, ")===>>", a5)
                        print("The next number of this series will be>>", nun1, "**3 +", n, "===>", a5)
                        if a5 == round(a5):
                            result = a5
                            break
                    else:
                        continue
                if result == round(result):
                    break
                else:

                    continue
            print("[Step_3]")
            if (a1 > 0):
                a = a1
                r = a2 / a
                t1 = a * (r ** 1)
                t2 = a * (r ** 2)
                t3 = a * (r ** 3)
                a5 = a * (r ** 4)
                if (a2 == t1) and (a3 == t2) and (a4 == t3):
                    print("Entered number [0] >>", a1)
                    print("Entered number [1] >>", a2)
                    print("Entered number [2] >>", a3)
                    print("Entered number [3] >>", a4)
                    print("The next number of this series will be>>", a5)
                    print("This is Geometrical progression[G.P]")

            print("[Step_4]")
            b1 = a3 - a1
            a5 = a3 + b1
            print("Entered number [0] >>", a1)
            print("Entered number [1] >>", a2)
            print("Entered number [2] >>", a3)
            print("Entered number [3] >>", a4)
            print("The next number of this series will be>>", a5)
            print("In this series>>[a,b,a+x,b+y].So the next word [a+2x]")


find_num(1,1,1,0,'x')
