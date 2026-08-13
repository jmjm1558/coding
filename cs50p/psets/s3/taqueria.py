
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = 0

while True:
    try:
        x = input("Item: ").title()
        if x in menu:
            order += menu[x]
            print(f"Total: ${order:.2f}")
        else:
            continue
    except EOFError:
        break

