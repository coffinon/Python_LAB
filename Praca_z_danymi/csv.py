position = []
name = []
year = []
color = []

with open("cars.csv", "r") as input_file:
    lines = input_file.read().splitlines()
    print(lines)
    for i in lines:
            position.append(i.split(" , ")[0])
            name.append(i.split(" , ")[1])
            year.append(i.split(" , ")[2])
            color.append(i.split(" , ")[3])
input_file.close()

position[0] = "Pozycja"
name[0] = "Nazwa"
year[0] = "Rok produkcji"
color[0] = "Kolor"

while 1:
    print("\nAKTUALNA BAZA SAMOCHODOW : ")
    for i in range(0, len(position)):
        print(position[i], 4 * "\t", name[i], 4 * "\t", year[i], 4 * "\t", color[i])

    print("_-_-_-_-_ WYBIERZ CO CHCESZ ZROBIC _-_-_-_-_")
    print("\t 1.DODAJ NOWY WIERSZ")
    print("\t 2.USUN WIERSZ")
    print("\t 3.KONIEC (ZAPISZ)")

    n = int(input("\nWYBOR : "))

    if n == 1:
        position.append(str(len(position)))
        name.append(str(input("PODAJ NAZWE SAMOCHODU : ")))
        year.append(str(input("PODAJ ROK PRODUKCJI SAMOCHODU : ")))
        color.append(str(input("PODAJ KOLOR SAMOCHODU : ")))
    elif n == 2:
        i = int(input("\nWYBIERZ KTORY REKORD CHCESZ USUNAC : "))
        if i == 0 or i > len(position):
            print("REKORD NIE ISTNIEJE")
        else:
            del name[i]
            del year[i]
            del color[i]
            position.pop()
    elif n == 3:
        break
    else:
        print("NIE ROZPOZNANO KOMENDY")

save_data = []

with open("cars.csv", "w") as output_file:
    for i in range(0, len(position)):
        save_data.append(position[i] + " , " + name[i] + " , " + year[i] + " , " + color[i] + "\n")

    output_file.writelines(save_data)
output_file.close()
