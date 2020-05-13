f = open("./data/basic.txt", "w")
f.write("Hello python programming!")
f.close()

f1 = open("./data/basic.txt","a")
f1.write("\nAdded documents")
f1.close()

with open("./data/test.txt","w") as f3:
    f3.write("sentence document")
f3.close()

with open("./data/test.txt","a") as f3:
    f3.write("\nwith sentence document")
f3.close()

contents = " "

with open("./data/test.txt","r") as f4:
    contents = f4.read()

print(contents)