database_dict = {}
def login(email, password):
    if '@' not in email:
        print("Enter a Valid Email Address")
    elif email in database_dict.keys():
        if database_dict[email] == password:
            print("Logged in Successfully")
            exit()
        elif database_dict[email] != password:
            print("Your Password is wrong!")
    elif email not in database_dict.keys():
        print("You dont have an account with us.Please choose sign up!!")


print("Welcome to Pratik's Application , Please Choose One of these.")
while True:
    print('1. Login\n2.Sign Up\n')
    ok = int(input())
    if ok == 1:
        print('Enter your Email Address')
        login_email = input()
        print('Enter your Password')
        login_password = input()
        login(login_email, login_password)
    elif ok == 2:
        signup_email = input("Enter Email Address : \n")
        if '@' not in signup_email:
            print('Please enter valid email address')
        elif signup_email in database_dict.keys():
            print('Email is already used.')
        signup_password = input("Choose a Password :")
        database_dict.update({f'{signup_email}': f'{signup_password}'})
        print('Signed Up Successfully')


