# print('Andreas Haas')
# print('o----')
# print(' ||||')
# print('*' * 10)

print("Driver application\n")

isStarted = False

while True:
    command = input("> ").strip().lower()

    if command == "start":
        if not isStarted:
            print("Car started... Ready to go!")
            isStarted = True
        else:
            print("the car is started...")
    elif command == "stop":
        if isStarted:
            print("Car stopped...")
            isStarted = False
        else:
            print("the car is stopped...")
    elif command == "help" or command == "?":
        print('''
start   - to start the car
stop    - to stop the car
help/?  - to show this help
quit    - to exit the application
        ''')
    elif command == "quit":
        print("Got out of the car... Program was stopped!")
        break
    else:
        print("I don't understand that...")

#1
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print('x' * number)
#2
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#3
userEingabe = input('Geben Sie eine ganze Zahl ein: ')
print(f'Eingegebenes Wert: {userEingabe}')

userGroesse = float(input('Geben Sie seine Größe in Meter ein: '))
userGewicht = float(input('Geben Sie sein Gewicht in kg ein: '))

bmi = userGewicht / (userGroesse ** 2)

if bmi < 18.5:
    print('Untergewicht. Empfehlung 2500 kcal täglich')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Normalgewicht. Empfehlung 2000 kcal täglich')
elif bmi >= 25.0 and bmi <= 29.9:
    print('Übergewicht. Empfehlung 1800 kcal täglich')
else:
    print('Adipositas. Empfehlung 1500 kcal täglich')

#4
plastik_flaschen_stk = int(input('Geben Sie Anzahl der Plastikflaschen ein: '))
glas_flaschen_stk = int(input('Geben Sie Anzahl der Glasflaschen ein: '))

pfand_pf = plastik_flaschen_stk * 0.25
pfand_gf = glas_flaschen_stk * 0.15

pfand_satz_gesamt = pfand_pf + pfand_gf
print(f'Gesamtpfand: {pfand_satz_gesamt:.2f} €')

if pfand_satz_gesamt < 1:
    print('Sie haben nur wenige Flaschen abgegeben.')
elif pfand_satz_gesamt <= 5:
    print('Eine gute Menge an Flaschen zurückgegeben!')
else:
    print('Wow, das sind viele Flaschen!')

#5
numbers = [3, 6, 8, 2, 4, 9, 4, 1, 2]

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'Max = {max}')

#6
numbers = [3, 2, 8, 2, 4, 9, 4, 1, 7]
numbers2 = []
for number in numbers:
    if numbers not in numbers2:
        numbers2.append(number)
print(numbers2)

#7
numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

phone_nummer = input('Geben Sie bitte Phone nummer: ')

out_str = ""
for ch in phone_nummer:
    out_str += numbers.get(ch, "!") + " "
print(out_str)

#8
message = input(">")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":|" : "😒",
    ":(" : "😢"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)