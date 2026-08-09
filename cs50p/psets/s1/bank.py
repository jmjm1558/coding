g = input("Greeting: ")
g = g.strip().lower()
word = "hello"

if g[0:5] == word:
    print("$0")
elif g[0:1] == "h":
    print("$20")
else:
    print("$100")
