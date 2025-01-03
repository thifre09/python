text = input("Digite  o texto:")
shiftnum = int(input("Digite um número entre 1 e 25:"))
if shiftnum <= 0 or shiftnum > 25:
    print("numero invalido")

result = ""

lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for char in text:
    if not char.isalpha():
        result += char
    else:
        code = ord(char) % 32
        if char.islower():
            code = (code + shiftnum) % 26
            result += lower_letters[code - 1]
        elif char.isupper():
            code = (code + shiftnum) % 26
            result += upper_letters[code - 1]

print(result)
            