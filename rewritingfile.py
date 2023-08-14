f=open("writingfile.py","w+")
f.write("after modification")
f.write(print("hello"))

print("after updation or rewriting...")
ff=open("writingfile.py","r")
obj=ff.read()
print(obj)