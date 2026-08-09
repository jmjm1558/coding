n = input("File name: ").strip().lower()

if ".gif" in n:
    print("image/gif")
elif ".png" in n:
    print("image/png")
elif ".jpeg" in n or ".jpg" in n:
    print("image/jpeg")
elif ".pdf" in n:
    print("application/pdf")
elif ".txt" in n:
    print("text/plain")
elif ".zip" in n:
    print("application/zip")
else:
    print("application/octet-stream")
