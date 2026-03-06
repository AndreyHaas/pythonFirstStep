userEingabe = input('Geben Sie eine ganze Zahl ein: ')
print(f'Eingegebenes Wert: {userEingabe}')

userHeight = float(input('Geben Sie seine Größe in Meter ein: '))
userGewicht = float(input('Geben Sie sein Gewicht in kg ein: '))

bmi = userGewicht / (userHeight ** 2)

if bmi < 18.5:
    print('Untergewicht. Empfehlung 2500 kcal täglich')
elif 18.5 <= bmi <= 24.9:
    print('Normalgewicht. Empfehlung 2000 kcal täglich')
elif 25.0 <= bmi <= 29.9:
    print('Übergewicht. Empfehlung 1800 kcal täglich')
else:
    print('Adipositas. Empfehlung 1500 kcal täglich')