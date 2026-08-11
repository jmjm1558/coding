# letters numbers as a str
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
           "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = str(numbers)

# criteria to solve:
# - first number =/ 0
# - no intermediate numbers
# - starts with at least two letters
# - 2 chars min and 6 chars max
# - No periods, spaces or punctuation marks

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # list of x's numbers
    num = []
    let = []
    # string of x's numbers
    criteria = ""
    # allowed char
    not_allowed = ""

    # add each number in x to the list and to the string
    for i in s:
        if i in numbers:
            num += i
            criteria += i
        elif i in letters:
            let += i
        elif i not in numbers and i not in letters:
            not_allowed += i

    # No periods, spaces or punctuation marks
    if not_allowed != "":
        return False
    # 2 chars min and 6 chars max
    elif len(s) < 2 or len(s) > 6:
        return False
    elif num == []:
        return True
    # first number =/ 0
    elif num[0] == "0":
        return False
    # no intermediate numbers
    elif criteria not in s or s[-1] not in num:
        return False
    # starts with at least two letters
    elif (s[0] and s[1]) not in letters:
        return False
    else:
        return True


main()
