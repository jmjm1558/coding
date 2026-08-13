lista = []
complete_list = []

while True:
    try:
        item = input().lower()
        complete_list.append(item)
        if item not in lista:
            lista.append(item)
    except EOFError:
        break

for i in sorted(lista, key=str):
    print(complete_list.count(i), i.upper(), end="\n")
