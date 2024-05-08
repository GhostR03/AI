def intro(bot_name, created_in):
    print("Hello my name is {0}".format(bot_name))

    print("I was created in the year {0}".format(2006))


def ask_name():
    print("I forgot your name can you remind me of it ?")

    name = str(input())

    print("{0} have a really nice day".format(name))


def guess_age():
    print("Let me guess your age")
    print(" Give me remainders when your age is divided by 3, 5 and 7")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("I know you will be suprised but your age is {0}".format(age))


def end():
    print("It was nice meeting you pratham C.U")


def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    print('Completed, great talent huh!')


intro("paaji", 2009)
ask_name()
guess_age()
test()
end()
