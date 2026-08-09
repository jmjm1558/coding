o = input("Expression: ").replace("Expression", "").replace(" ", "")

if "+" in o:
    x = (float(o[0:o.find("+")]) + float(o[o.find("+"):]))
    print(round(x,1))
elif "-" in o:
    x = (float(o[0:o.find("-")]) - float(o[(o.find("-"))+1:]))
    print(round(x,1))
elif "*" in o:
    x = (float(o[0:o.find("*")]) * float(o[(o.find("*"))+1:]))
    print(round(x,1))
elif "/" in o:
    x = (float(o[0:o.find("/")]) / float(o[(o.find("/"))+1:]))
    print(round(x,1))
