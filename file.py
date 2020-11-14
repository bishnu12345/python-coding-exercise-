import sys


# f = open("file.txt", "w")
# f.write("My name is Apoorba \n")
# f.write("Content 1 \n")
# f.close()
#
# f = open("file.txt", "a")
# f.write("Appending \n")
# f.write("Append \n")
# f.close()

# f = open("file.txt", "r")
# print(f.read())
# print(f.read(1))
# print(f.read(12))
# print(f.readline())
# f.close()

try:
    f1 = open("file12.txt", "r")
    print(f1.read())
except:
    print(sys.exc_info())
finally:
    f1.close()

print('Working')


# with open("file123.txt", "r") as f:
#     print(f.read())


