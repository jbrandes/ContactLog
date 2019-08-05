import io
import json
import requests
import sqlite3



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
            json.dump({'Name':name, 'Phone':phone, 'Email': email}, outfile)

def sqldb():

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NONE EXISTS contacts ( data json)")
        

f = open('contacts.txt', 'a')

    

print("Welcome to your contact directory.")
print("Would you like to enter a new name into the directory? ")
answer = input()
if answer == "no":
    print("Thanks for using our program.")
else:
    contact()
    f.close()
