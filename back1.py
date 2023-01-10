import mysql.connector
import webbrowser

conn = mysql.connector.connect(user='root', password='password',
                              host='localhost',database='xenon')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select_xenon = """SELECT * FROM data"""
cursor = conn.cursor()
cursor.execute(select_xenon)
result = cursor.fetchall()

p = []

tbl = "<tr><td>ID</td><td>name</td><td>email</td><td>subject</td></tr>message</td></tr>"
p.append(tbl)

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()
filename = 'webbrowser.html'
contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(p)

main(contents, filename)    
webbrowser.open(filename)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.")    