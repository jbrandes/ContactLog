import io
import json


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
        with open('contactlist.json', 'w') as outfile:
            json.dump({'name':name, 'Phone':phone, 'Email': email}, outfile)
        

f = open('contacts.txt', 'a')

    

print("Welcome to your contact directory.")
print("Would you like to enter a new name into the directory? ")
answer = input()
if answer == "no":
    print("Thanks for using our program.")
if answer == "yes":
    contact()
    f.close()
