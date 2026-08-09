answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.strip()

if answer == str(42) or answer == "forty-two" or answer == "forty two" or answer.title() == "Forty Two":
    print("Yes")
else:
    print("No")
