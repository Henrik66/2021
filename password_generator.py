

def contacts():
    return None


def newcontact(name):
    email = input("What is " + str(name) + "'s email address? ")
    phone_number = input("What is " + str(name) + "'s phone number? ")
    contact = (str(name) + " - " + str(email) + " - " + str(phone_number))
    return contact
