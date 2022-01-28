def P1259():
    while True:
        try:
            num = int(input())
            if num == 0:
                break

            number = list(str(num))
            print("yes" if number == list(reversed(number)) else "no")
        except:
            break


if __name__ == '__main__':
    P1259()
