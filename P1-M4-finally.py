try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File doesn't exist.")
finally:
    print("Done attempting to read the file.")