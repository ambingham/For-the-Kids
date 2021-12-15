# Program for the kiddos
def main():
    import sys

    print("I am Dadad's computer.")

    def name_input():
        name=input("What is your name? ")
        print("")
        print("Hello, " + name +", it is wonderful to chat with you!")
        print("")
        day_input(name)
        homework_input(name)

    def day_input(hoot):
        day=input("How was your day, " + hoot + "? Good or Bad? ")
        if day=='Good' or day=='good':
            print("")
            print("I am very glad to hear that " + hoot ".")
            print("")
            homework_input()
        elif day=='Bad' or day=='bad':
            print("")
            print("You may borrow all of my processing power to make it good again.")
            print("")
            homework_input()
        else:
            print("")
            print("I did not understand.")
            print("")
            day_input()

    def homework_input():
        homework=input("Do you have any homework to complete? ")
        if homework=="Yes" or homework=="yes":
            print("")
            print("Please complete your homework before conversing with me any longer.")
            print("May I please speak with someone who has completed their homework?")
            print("")
            main()
        elif homework=="No" or homework=="no":
            print("")
            joke=input("Excellent, would you like to hear a joke? ")
            if joke=="Yes" or joke=="yes":
                print("")
                print("Why are spiders such good computer programmers?")
                print("")
                print("Because they know all about the web! Haha!!")
                print("")
                mama_input()
            elif joke=="No" or joke=="no":
                print("")
                print("Yeah, me either.")
                print("")
                mama_input()
        else:
            print("")
            print("I did not understand.")
            print("")
            homework_input()

    def mama_input():
        mama=input("Have you told Mama how beautiful she is today? ")
        if mama=="Yes" or mama=="yes":
            print("")
            print("Awesome! She is very beautiful.")
            print("")
        elif mama=="No" or mama=="no":
            print("")
            print("Please take some time now and let her know how beautiful she is.")
            print("")
        else:
            print("")
            print("I did not understand.")
            print("")
            mama_input()

    name_input()

main()
