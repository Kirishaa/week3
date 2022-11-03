set_password = input("Choose a password(must be 8 to 12 characters): ")
check_password = input("Confirm the password: ")
if set_password == check_password: 
    if 8<=len(set_password)<=12:
        print ("Password Set")
    elif len(set_password)<8:
        print ("Password too short.")
    else:
        print ("Password too long.")
else:
    print ("Error")

