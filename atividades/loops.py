mat:str = input("Digite sua matricula:")
while len(mat) != 14 and mat.isdigit():
    mat = input("Digite sua matricula corretamente:")

ano:str = mat[:4]
periodo:str = mat[4]
curso:str = mat[5:8]
id:str = mat[-3:]

print(ano,periodo,curso,"010",id)