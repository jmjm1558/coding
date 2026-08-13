nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
try:
    x = input("Fraction: ")
    numerator = ""
    denominator = ""
    if "/" in x:
        for i in x:
            if i in nums:
                for i in x[:x.find("/")]:
                    numerator += i
                for i in x[x.find("/"):]:
                    denominator += i
            numerator = int(numerator)
            denominator = int(denominator)
        if (numerator < denominator and numerator > 0) and 0 <= numerator <= 4 and 0 <= denominator <= 4:
            factor = (numerator/denominator) * 100
            if factor <= 1:
                print("E")
            elif factor >= 99:
                print("F")
            else:
                print(factor)
        else:
            pass
    else:
        pass
except ZeroDivisionError:
    pass
except ValueError:
    pass
