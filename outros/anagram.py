def isanagram(text1: str, text2: str) -> bool:
    letras1 = {}
    letras2 = {}
    for i in range(26):
        letras1[chr(65+i)] = 0
        letras2[chr(65+i)] = 0

    text1 = text1.upper()
    text2 = text2.upper()

    for letra in text1:
        letras1[letra] += 1

    for letra in text2:
        letras2[letra] += 1
    if text1 == "" or text2 == "":
        print("Não é um anagrama")
    elif letras1 == letras2:
        print("É um anagrama")
    else:
        print("Não é um anagrama")

isanagram("","")