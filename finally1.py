try:
    f = open("myfile.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("❌ File not found!")
else:
    print(data)
finally:
    print("This always runs, closing file or cleanup.")
