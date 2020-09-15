f = open("C:/Users/user/Desktop/Cynthia/student.txt.txt", "r")
print(f.read())
f.close()

f1 = open("C:/Users/user/Desktop/Cynthia/student.txt.txt", "w")
f1.write("This is an extra text added on the app!")
f1 = open("C:/Users/user/Desktop/Cynthia/student.txt.txt", "r")

print(f1.read())