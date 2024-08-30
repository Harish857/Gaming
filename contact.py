#!C:\Python\python.exe

import cgi
import mysql.connector
print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>","Welcome","</h1>")
'''
form=cgi.FieldStorage()
fname=form.getvalue("Email")
uname=form.getvalue("Username")
passrd=form.getvalue("Password")
print("<h1>",fname,uname,passrd,"</h1>")
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="games"
)
mycursor=mydb.cursor()
sql="INSERT INTO login(Email,Username,Password) VALUES(%s,%s,%s)"
val=(fname,uname,passrd)
mycursor.execute(sql,val)
mydb.commit()'''
print("</body>")
print("</html>")
