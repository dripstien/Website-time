import random

# Main program where all fun stuff happens this controls the menu and the options you select!


#this is the display for the menu, it controls the things printed so you know what option you ar selecting or what other options are avalable
def menu():
    print("Welcome to Tom Nook's store managment program! 2023 by:Matthew Dias")
    print("what do you want to do today!:")
    print("a. Calculate Income Taxes")
    print("b. Generate your very own Usernames and Passwords")
    print("c. Quit :(")
    print("d. top secret!")
    print("e. the nook")

#this is the income tax program, it lets you type your income into the response bar and outputs your tax estimation with a little fun meesage from Mr.Nook himslef!
def incometaxtime():
    print("Welcome to the nooks (patent pending) Income Tax Calculator 3000!")
    try:
        income = float(input("how much money did you make this year?: $")) #the float is here to make the final product of the income tax look like a real dollar amount like 14.10 or 179.20 instead of just 17.2 or 56.2
        taxamount = income * 0.04
        print(f"wow the IRS is super mean! You owe them ${taxamount} in taxes. If Mr.Nook was dictator of the United States you would only have to pay me in acorns!")
    except:
        print("oops! thats not a number! please enter an actual number!.")
#this code controls the name and password section of the menu, it combines the first three digits of your first name with the first 4 digits of yournlast name and randomly combines a selected phrase with a random number from 10-100 for your new passcode 
def nameandpasswordoclock():
    print("Welcome to the tom nook (patent pending) Username and Password Generator")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")

    # Generate username (make it good!)
    username = firstname[:3] + lastname[:4]

    # Generate password (super secret)
    wordbank = ["elbaf", "necronomicon", "privyet", "up2me", "superrr!!!"]
    randomword = random.choice(wordbank)
    randomnumber = random.randint(10, 100)
    password = randomword + str(randomnumber)
    print("great name! but mine is wayyyyy better!")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("im totally not going to sell your personal information to Russian hackers! ya obeshchaniye :)")
#uh-oh it seems like this code is meant for Mr.Nooks revolution recruitment! it allows the user to "make their choice" about if they want to join in Mr.Nooks revolution! what will you decide?
def hello():
    print("the nook revolution will begin soon! believers in our cause will work together to bring down the current regime! will you join my revolution?")
    
    saw = input("make your choice")

    if saw == 'yes':
                  print("smart choice")
    elif saw == 'no':
                 print(r"""/    game over.
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠒⣶⣤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⢰⡟⠀⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣄⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⣠⣾⠿⠋⠛⣿⡄⠛⣷⡄⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠸⣇⠀⢸⣿⡿⣄⠀⠀⢀⡄⣾⣿⠟⠭⡿⡆⠀⠀⣿⣿⡆⠀⠀⣸⣿⡏⠀⠀⠀⣾⠃⠀⠸⣿⠀⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⣽⣿⢛⣿⣶⠓⠀⣿⡏⠀⠀⠀⠀⠉⠀⢾⠏⠟⣿⡀⠀⡩⣿⠀⣴⣶⣯⣵⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢨⣿⡞⠋⠽⣷⣄⣿⡇⠀⠀⠀⠀⣀⣼⣯⣶⣾⣿⡿⠛⢿⣿⠟⠋⠀⢨⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠿⠋⠉⠀⠀⠀⠀⠹⢿⡿⣿⣻⣤⠞⢻⣿⠀⠀⠈⠗⡿⣿⣧⣴⡦⣖⣿⡿⠉⠉⠀⠙⢿⡅⢸⡅⠀⠀⣀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⢻⡆⠉⠁⠀⠀⠀⠀⠀⠀⠻⢿⣻⠿⠻⠁⠀⠀⠀⠀⠘⢿⣇⣿⣒⣚⣟⡿⠃⢀⣀⣤⢤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣻⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⡿⠃⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢛⣿⣿⣿⣿⣿⣻⡛⠯⣟⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠻⣿⣤⠀⠀⠀⢀⣠⣤⡶⠟⠛⠁⠀⠀⠀⠈⠻⠛⠲⠶⠦⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⠈⠉⠛⠛⠛⠋⠉⠀⠀⢀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⠈⠉⠙⠓⠲⠶⢤⣀⡀⠀⠀⠀⣿⡏⢠⣾⠋⠁⠀⠀⠀⠉⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⠇⠀⢀⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⣀⠀⠉⠉⠛⠛⠻⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⢃⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⡀⠀⠀⠀⠉⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠈⣿⢿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠙⠳⣤⣀⠀⠀⣐⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢟⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⠉⠛⠛⠉⣻⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢏⣾⣿⣿⣿⣿⣿⡟⠛⠛⣶⣄⣀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⢈⣼⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⣾⣿⣿⣿⣿⣿⣿⠀⠀⢰⡏⠉⠙⠻⠷⣶⣤⣄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠛⠻⣿⣿⣿⣿⣿⣄⠀⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡏⣸⣿⣿⣿⣿⣿⣿⡏⠀⠀⢸⡇⠀⠀⠀⣠⡿⠃⠈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣆⠸⣏⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢰⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠘⢷⣤⣤⠾⠋⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡆⢹⡼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣸⣿⣿⣿⣿⣷⡹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢹⡆⠀⠀⠀⢈⣽⠃⠀⢹⣿⣿⣿⣿⣿⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠈⢿⣿⣿⣿⣿⠿⠿⢿⣽⡟⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⢷⡄⢀⣠⡿⠁⠀⢀⣿⣿⣿⣿⣿⣿⡇⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢑⣂⣠⣤⣿⣿⡷⢶⣶⣶⠀⠙⣿⢻⣿⡿⠟⠉⠁⠀⠀⠀⠀⢀⣤⣴⣶⣶⣶⣦⣤⣀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣧⠀⠀⠀⠙⠛⠉⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⣿⣏⠀⠀⠀⠀⠀⠀⢀⣼⠋⢸⡇⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⡿⠿⠿⠀⠀⠀⢀⣴⡿⠁⠀⣾⡇⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠹⢿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣟⣿⣿⣷⣄⠀⢀⣴⣿⠟⠀⢀⣼⢟⣿⣀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⢛⣻⣝⡟⢿⣟⢿⣷⣨⡿⠃⠀⢠⣿⡋⢸⣿⠛⠻⢶⣄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣽⣿⣿⣿⣿⣆⢻⡏⣿⡏⠀⠀⢀⣾⢋⣷⣾⣿⣦⡀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⠀⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡵⣿⣿⣿⣿⣿⣿⠄⣿⣿⡇⠀⣶⣿⣿⣸⣿⣿⣿⣿⣿⡆⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡻⣿⣿⣿⣿⠟⣼⡏⣿⠇⠜⣰⣏⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣾⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠻⣦⣤⣤⣤⠞⢙⣹⡿⠀⣰⡿⠛⠿⢿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣬⣭⡀⠀⢿⡏⠀⣴⣯⠁⠀⠀⠀⢾⣿⣿⡇⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣾⡿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣔⣿⣿⣿⣷⣔⣖⣼⠀⣰⣿⢹⢀⣄⠀⠀⢸⣽⣿⡇⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠸⣿⣿⣿⡿⣽⡿⣰⣿⢃⣿⠮⣽⣶⣴⡿⠿⠟⢧⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡷⣌⣉⣉⣥⣿⣵⡏⣤⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⢿⡷⠾⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣾⣿⣿⣿⣷⣿⣟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣶⣤⣤⣴⣿⣿⡿⠛⢳⣤⣄⣀⣀⢀⣀⣀⣠⣿⠋⠀⠀⠀⠀⠈⠉⠈⠉⠙⠛⠛⠿⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡯⠟⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   """)
    else:
            print("yes or no only, this is a serious matter so no fooling around ")

def nook():
     print("why would you choose this option! it does nothing!")

#the big image above is of the nook himself! seems that sayin no to him is a bad idea! the text art is from this website: https://emojicombos.com/tom-nook-text-art
    
    

# Main program where all fun stuff happens this controls the menu and the options you select! basically redirects you to different specific aspect sof this progrsm based on your selection of A B C D or E

while True:
    menu()
    choice = input("what do you want to do today! (A, B, C, d, or e): ")

    if choice == 'A':
        incometaxtime()
    elif choice == 'B':
        nameandpasswordoclock()
    elif choice == 'C':
        print("sad to see you leave, see ya later aligator!.")
    elif choice == 'D':
        hello()
    elif choice == 'E':
       nook()
        
    else:
      print("oops! that option was not given! Please enter either A B C D or E!.")
