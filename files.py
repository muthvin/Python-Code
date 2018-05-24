import os

for root, dirs, files in os.walk("C:\\Program Files\\Apache Software Foundation\\tomcat-instance1\\webapps\\CiscoPy\\WEB-INF\\cgi\\"):  
    for file in files:
        if file.endswith('.py'):
            print(file)


'''
C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0\\webapps\\LAPAM_Py\\\WEB-INF\\cgi\\
C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0\\webapps\\LAPAM\\JScript\\

path =("C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0\\webapps\\test\\WEB-INF\\cgi\\")
print ("Counting all .py files in: " + path)

x=0
for files in os.listdir(path):
    if files.endswith('.py'):
        x+=1
        #print ("\nFile #" + str(x) + ": " + files)
print ("\nTotal number of .py files in: " + path + "-" + '"'+ str(x)+'"')

'''
