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