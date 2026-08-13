months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    try:
        date = input("Date: ")
        if date.count("/") == 2:
            date = date.strip().split("/")
            if 0 < int(date[0]) <= 12 and 0 < int(date[1]) <= 31:
                print(f'{date[2]}-{int(date[0]):02d}-{int(date[1]):02d}')
                break
            else:
                continue
        elif "," in date:
            date = date.replace(",", "").split()
            if date[0] in months and 0 < int(date[1]) <= 31:
                print(f'{date[2]}-{int(months[date[0]]):02d}-{int(date[1]):02d}')
                break
    except ValueError:
        continue
    except EOFError:
        break
