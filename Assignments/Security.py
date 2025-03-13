def new_user():
    credentials = {}
    
    while True:
        choice = input("\nWould you like to create a username and password? (yes/no)")
        if choice.lower() == 'yes':
            username = input('Please type in a new username: ')
            if username in credentials:
                print("Sorry, this username already exists. Please try again.")
            else:
                password = input('Please type in a password for your username: ')
                confirm = input('Please confirm your password: ')
                if password == confirm:
                    credentials[username] = password
                    print('Username and password accepted!')
                else:
                    print('Sorry, your passwords do not match. Username and password not accepted.')
        elif choice.lower() == 'no':
            print("Thank you for completing your new user information.")
            break
        else:
            print("Sorry, invalid input. Please try again.")
    
    return credentials

def login(security):
    print("Let's try logging in.")
    for i in range(3):
        user = input("Username: ")
        password = input("Password: ")
        if user in security:
            if security[user] == password:
                print('Successful login!')
                break
        else:
            print(f'Incorrect login information. {2 - i} tries remaining.')
            if i == 2:
                print('Account locked.')

if __name__ == '__main__':
    login(new_user())