def stars_while():
    print("zacatek")
    i = 0

    while i<5:
        print ("*")
        i += 1

    print("konec")

#stars_while()
#funkce demonstrující cyklus for
def stars_for():
    print("zacatek")

    for i in range(5):
        print("*")

    print("konec")

#stars_for()

#funkce určující, zda number leží mezi min a max number
def in_range(min_number, max_number, number):
    if number > min_number and  max_number > number:
        print("Is in range")
    else:
        print("Is not in range")

#in_range(100,1000, 150)

def dopln_jmeno(jmeno):
    print("Ahoj ", jmeno)

    jmeno = input("Zadej jméno:")



