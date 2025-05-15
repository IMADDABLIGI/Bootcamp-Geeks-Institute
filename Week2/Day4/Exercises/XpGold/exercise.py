users_dict = {
    "imad": "root123",
    "hamza": "pas123",
    "hind": "test123",
    }

logged_in = None

def get_user_name():
    while 1:
        user_input = input('username: ')
        if user_input in users_dict:
            print(">- 7AYD MNEK HAD LF3AIL A SAHBY -<")
        else:
            return user_input

def get_user_password():
    while 1:
        user_input = input('password: ')
        return user_input

try:
    while 1:
        user_input = input("Service: ").lower()
        if user_input == 'exit':
            print("\n>- THALA -<\n")
            break
        elif user_input == 'login':
            username = input('username: ')
            password = input('password: ')
            if username in users_dict:
                if users_dict[username] == password:
                    print("you are now logged in")
                    logged_in = username
                else:
                    print("Nice try diddy")
            else:
                print(">- 7ayd 3liya, aji creer compte fabor -<")
                new_username = get_user_name()
                new_password = get_user_password()
                users_dict[new_username] = new_password
                # print(users_dict)
                        
                    

        else:
            print(">- 7AYD MNEK HAD LF3AIL A SAHBY -<")

except Exception as e:
    print("\nError: ", e)
    print("\n\n>- THALA -<\n")


