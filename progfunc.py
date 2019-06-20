def func():
    servname=input("Enter server name")
    dbname=input("Enter database name")
    uname=input("Enter username")
    passs=input("password")
    string=servname+dbname+uname+passs
    return string

  
connectstring=func()
print("------------printing details-------------------")
print(connectstring)
