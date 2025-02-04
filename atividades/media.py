def media(): 
    notas = []

    for i in range(4):
        notas.append(int(input(f"Digite a nota {i+1}:")))

    media = 0
    for nota in notas:
        media += nota
    media = media/len(notas)


    if media >= 70:
        return "Aprovado"
    elif media >= 50:
        return "Recuperação"
    elif media < 50:
        return "Reprovado"

print(media())