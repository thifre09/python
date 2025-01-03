text = input("Insira um texto:")
text = text.replace(" ","")
text = text.upper()

text2 = text[::-1]

if text == text2 and len(text) > 1:
    print("É palindromo")
else:
    print("Não é palindromo")