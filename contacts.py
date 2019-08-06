import io
import json
import sqlite3

conn = sqlite3.connect('contacts.sqlite')

cursor = conn.cursor()

print("Opened database successfully")

def contact():
        name = input("What is your contact's name? ")
        phone = int(input("What is your contacts number? "))
        email = input("What is your contact's email? ")
        print("Confirmed")
        f.write("\n")
        f.write("Name: " + name)
        f.write("\n")
        f.write ("Phone: " + str(phone))
        f.write("\n")
        f.write("Email: " + email)
        f.write("\n")
        with open('contactlist.json', 'a') as outfile:
            json.dump({'name':name, 'Phone':phone, 'Email': email}, outfile)
            
            cursor.execute('''CREATE TABLE CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         PHONE           INT     NOT NULL,
         EMAIL        CHAR(50));''')
            
            
conn.commit()
conn.close()    

f = open('contacts.txt', 'a')


    

print("Welcome to your contact directory.")
print("Would you like to enter a new name into the directory? ")
answer = input()
if answer == "no":
    print("Thanks for using our program.")
else:
    contact()
    f.close()
