def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")
def greeting_2(name):
    print('hello {} !'.format(name.title()))
    print(f'hello {name.title()}!')
greeting_2('Adanna')
hello_name('Adanna')
def odd_numbers():
    for i in range(0,101,2):
        print(i)
def odd_numbers2():
    numbers = list(range(0, 101))
    for number in numbers:
        if number % 2 != 0:
            print(number)
odd_numbers2()












def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)



    else:
        a_year = False
        print(f'{a_year}')


        # Question 4 1.b solution

        """
        TRUTH TREE
        AND 
        T & T == T
        T & F == F
        F & F == F

        OR 
        T || F == T
        F || T == T
        F || F == F

        """

        def is_leap(a_year):
            if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
                print(True)
            else:
                print(False)

        is_leap_year(2019)

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else:
                status = False
                break
        print(status)

is_consecutive([1,2,3,4,5])
