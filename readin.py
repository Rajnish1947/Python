# Assume 'data.txt' already exists in the same directory.

print("------ Method 1: read() ------")
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()





print("------ Method 2: readline() ------")
file = open("sample.txt", "r")
line1 = file.readline()
line2 = file.readline()
line3 = file.readline()
print("Line 1:", line1.strip())
print("Line 2:", line2.strip())
print("Line 3:", line3.strip())
file.close()

print("------ Method 3: readlines() ------")
file = open("sample.txt", "r")
lines = file.readlines()
for i, line in enumerate(lines, start=1):
    print(f"Line {i}:", line.strip())
file.close()

print("------ Method 4: with open() ------")
with open("sample.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}:", line.strip())
