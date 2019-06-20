def func():
    servname=input("Enter server name")
    dbname=input("Enter database name")
    uname=input("Enter username")
    passs=input("password")
    string="servername="+servname+";"+"database name="+dbname+";"+"username="+uname+";"+"password="+passs
    return string

  
connectstring=func()
print("------------printing details-------------------")
print(connectstring)
