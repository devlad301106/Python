#with open("temp.txt", "w") as t:
#    t.write("Yo!")

#import os
#os.remove("temp.txt")

#Q.1
#with open("data.txt","x") as f:
#    pass

#Q.2
'''with open("data.txt","w") as f:
    f.write("My name is Dev!\n")
    f.write("I'm learing python\n")
    f.write("I'm currently learing file handling\n")'''

#Q.3
'''with open("Student.txt", "w") as s:
    s.write("Name: Dev\n")
    s.write("Age: 20\n")'''

#Q.4
'''name = input("Enter your name:- ")
age = input("Enter your age:- ")
course = input("Enter which course you are studying:- ")

with open("Student.txt", "w") as s:
    s.write(name + "\n")
    s.write(age + "\n")
    s.write(course + "\n")'''

#Q.5
'''with open("data.txt", "r") as d:
    content = d.read()
    print(content)'''

#Q.6
'''with open("data.txt", "r") as d:
    fline = d.readline()
    print(fline)'''

#Q.7
'''with open("data.txt", "r") as d:
    content = d.readlines()
    print(content)'''

#Q.8
'''with open("data.txt", "r") as d:
    for line in d:
        print(line)'''

#Q.9
'''with open("data.txt", "r") as d:
    lines = d.readlines()
    print("No. of line = ", len(lines))'''

#Q.10 to Q.12
#Done! Practiced on kartik's laptop

#Q.13
'''with open("data.txt", "r") as d:
    print(d.tell())
    print(d.read(5))
    print(d.tell())'''

#Q.14
'''with open("data.txt", "r") as d:
    print(d.read(5))
    d.seek(0)
    print(d.read(5))'''

#Q.15
'''with open("data.txt", "r") as d:
    d.seek(5)
    print(d.read())'''

#Q.16 & 17
'''try:
    with open("test.txt", "r") as t:
        pass

except FileNotFoundError:
    print("File doesnot exist!!")'''

#Q.18
'''with open("data.txt", "r") as d:
    content = d.read()

words = content.split()

print("words = ", len(words))'''

#Q.19
'''with open("data.txt", "r") as d:
    data = d.read()

words = data.split()
count = 0
for w in words:
    if w == "Python":
        count +=1

print(count)'''

#Q.21
'''with open("data.txt", "r") as d:
    data = d.read()

print(data.count("a"), data.count("e"), data.count("i"), data.count("o"), data.count("u"))'''

#Q22
'''with open("data.txt", "r") as d:
    longest = ""

    for line in d:
        if len(line) > len(longest):
            longest = line

print(longest)'''

#Q.23
'''with open("data.txt", "r") as d:
    data = d.read()

with open("student.txt", "w") as w:
    w.write(data)'''

#Q.24
'''with open("Student.txt", "r+") as d:
    data = d.read()

    udata = data.upper()
    print(udata)
    d.seek(0)
    d.write(udata)'''