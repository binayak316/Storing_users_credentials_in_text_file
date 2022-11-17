def register():
    database = open('database.txt', "r")

    username = input("Enter Your Username:")
    email = input("Enter Your Email address:")
    password = input("Enter Your Password:")
    confirmPassword = input("Confirm your password:")


    u_name = []
    emailadd =[]
    pwd= []

    for i in database:
        a,b,c = i.split(", ")
        c = c.strip()
        u_name.append(a)
        emailadd.append(b)
        pwd.append(c)
    # data = dict(zip(u_name, pwd))
    # print(data)

    if password != confirmPassword:
        print("Password didn't match please check.")
        register()
    else:
        if len(password)<=5:
            print("password is too short!!!:")
            register()

        if  not any(char.isdigit() for char in password):
            print("password should contain numeric values!!!")
            register()
        if not any(char.isupper() for char in password):
            print("password should contain uppercase!!!")
            register()
        if not any (char.islower()for char in password):
            print("password should contain lowercase!!!")
            register()
        elif email in emailadd:
            print("email is already exists")
            register()
        else:  
            database = open("database.txt", "a")
            database.write(username+", "+email+", "+password+"\n")
            print("Successfully created a User!!!")
            print("Now login with your credentials,", username)
# register()


def login():
    database = open('database.txt', "r")

    username  = input("Enter Your Username:")
    password = input("Enter Your Password:")

    if not len(username or password) <1: #1 vanda sano nahune

        u_name = []
        # emailadd =[]
        pwd= []

        for i in database:
            a,b,c = i.split(", ")
            c = c.strip()
            u_name.append(a)
            # emailadd.append(b)
            pwd.append(c)
        data = dict(zip(u_name, pwd))
        # print(data)
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("login successfully")
                    else:
                        print("Invalid credentials")
                except:
                    print("Incorrect Credentials")
            else:
                print("username doesn't exist")
        except:
            print("Login Error")
# login()


def index(option=None):
    option = input("login | register: ")
    if option == "login":
        login()
    elif option == "register":
        register()
    else:
        print("select any option !!!")


index()