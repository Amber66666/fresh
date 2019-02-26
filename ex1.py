def money():
    print(">>>>>>>money=",money)


def flatwhite():
    flatwhite=input(">")

    if "Yes" in flatwhite or "yes"in flatwhite:
        print("oh~then you must run alot to cover that")
        print("For your heathy,you get a cold water instead!")
        exit(0)
    elif "No" in flatwhite or "no" in flatwhite:
        print("You think highly of your health.As a gift,I will give you some money.")
        print("How much do you want?")
        money=int(input(">>>"))

        if money < 50 :
            print("Good boy!")
        else:
            print("Greedy person got nothing!")
            print("One more chance.")
            money()

    else:
        print("sorry,pardon?")
        flatwhite()


def coffee():
    print("We have flat white and latte.")

    coffee=input(">")

    if "flat white" in coffee or "flatwhite" in coffee:
        print("It is a good choice,would you want some sugar?")
        flatwhite()
    elif "latte" in coffee:
        print("latte !Here you are,Merci!")
    else :
        print("Sorry?")
        start()

def start():
    print("Hi buddy,welcome to KMM Frog.")
    print("Do you want some coffee?")
    coffee()
start()

def end():
    print("Have a nice day!Bye!")
end()
