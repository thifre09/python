def find_word(word:str, text:str) -> bool:
    achou = -1
    for letter in word:
        achou = text.find(letter, achou+1)
        if achou == -1:
            print("Não")
            break
    if achou != -1:
        print("Sim")

find_word("donot","Nabucodonosor")