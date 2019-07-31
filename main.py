import io


def contact():
        name = input("What is your contact's name? ")
        phone = int(input("What is your contacts number? "))
        email = input("What is your contact's email? ")
        print("Confirmed")
        f.write("\n")
        f.write("Name: " + name)
        f.write("\n")
        f.write ("phone: " + str(phone))
        f.write("\n")
        f.write("email: " + email)
        f.write("\n")
        return json.dumps("contacts.json")

f = open('contacts.txt', 'a')
print("Welcome to your contact directory.")
print("Would you like to enter a new name into the directory? ")
answer = input()
if answer == "no":
    print("Thanks for using our program.")
if answer == "yes":
    contact()
    f.close()
