def main():
    x = input("What time is it? ")
    if ":" in x:
        if 7 <= convert(x) <= 8:
            print("breakfast time")
        elif 12 <= convert(x) <= 13:
            print("lunch time")
        elif 18 <= convert(x) <= 19:
            print("dinner time")

def convert(time):
    if ":" in time:
        x = time[0:time.find(":")]
        y = float(time[(time.find(":"))+1:])
        y = y/60
        if (len(x) <= 2 and len(x) > 0) and (0 <= int(x) <= 24):
            x = float(x)
            return x + y

if __name__ == "__main__":
    main()
