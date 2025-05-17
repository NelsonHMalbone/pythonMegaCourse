# have user enter a password
# tells user if password is correct ends program or wrong enter till right

password = input("Enter password: ")

while password != "pass123": # not equal to
    password = input("Enter password: ")

print("password is correct")