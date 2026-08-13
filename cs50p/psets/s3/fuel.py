while True:
    try:
        x = input("Fraction: ")
        num = int(x[:x.find("/")])
        den = int(x[x.find("/")+1:])
        factor = num/den * 100
        if num < 0 or num > den:
            continue
        elif factor >= 99:
            print("F")
        elif factor <= 1:
            print("E")
        else:
            print(f"{round(factor)}%")
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    else:
        break

