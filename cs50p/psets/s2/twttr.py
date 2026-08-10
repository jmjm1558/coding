vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

text = input("Input: ")
for vowel in vowels:
    if vowel in text:
        text = text.replace(vowel, "")
print("Output:", text)
