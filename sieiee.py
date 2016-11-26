Liczba1 = input("Podaj pierwszą liczbę")

if not Liczba1.isnumeric():
    print("Podaj liczbę!!!")
    quit()    

Liczba2 = input("Podaj drugą liczbę")

if not Liczba2.isnumeric():
    print("Podaj liczbe!!1")
    quit()

if Liczba1 > Liczba2 :
    print("Pierwsza liczba jest większa od drugiej")

elif Liczba2 > Liczba1 :
    print("Druga liczba jest wieksza od pierwszej")

else:
    print("Liczba jest równa")



