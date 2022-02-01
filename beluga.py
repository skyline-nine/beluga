import os
from datetime import datetime
i = 1
e = 1
now = datetime.now()
def cls():
  os.system("clear")
  os.system("cls")
def file():
  if i == 1:
    l = input("Enter the file name or location of the file: ")
    t = input(" r = read\n a = append\n w = write\n x = create\n d = delete file\n exit = leave\n")
    if t == "w" or t == "a":
        wd = input("What would you like to add: ")
        f = open(l,t)
        f.write(wd)
    elif t == "r":
        f = open(l,t)
        print(f.read())
    elif t == "d":
      if os.path.exists(l):
        os.remove(l)
        print("file deleted")
      else:
        print("The file does not exist")
    elif t == "x":     
        f = open(l,t)
  else:
    print("error")
def IDE():
  ide = input("Type command:")

  if ide == "/test":
    print("test complete")

  elif ide == "/help":
    print("/test: test command \n/help: get a list of commands \n/say: type in a set of words and the machine will repeat them")
    print("/math enter a calculation and you will get answer in return")
    print("/clear to clear screen * only for linux *\n/exit to exit program")
    print("/time tell the time \n/date tell date")
    print("/file locate and create and edit files")
    

  elif ide == "/say":
    prnt=input("")
    print(prnt)

  elif ide =="/math":
    math=input("Enter Math Problem here:")
    if math == "0/0":
      print("∞")
    else:
      print(eval(math))
  elif ide == "/clear":
    cls()

  elif ide == "/time":
    print(now.strftime("%H:%M:%S"))
  elif ide == "/date":
    print(now.strftime("%Y-%m-%d"))
  elif ide =="/file":
    file()
        
  elif ide == "/exit" or "/kill" or "/close":
    exit()
  else:
    print("Error type help for a list of commands")

    
while i == 1:
  IDE()
