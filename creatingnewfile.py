#here i'm going create a new file so
try:
    obj=open("newfile.txt","x")
    print("creating done succiesfully")
except Exception as e:
    print("exception occured whilw creating....")
