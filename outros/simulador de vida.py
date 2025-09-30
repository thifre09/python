import random
import tkinter as tk
from tkinter import scrolledtext
from enum import Enum

# ===== ENUMS =====
class Sexo(Enum):
    MACHO = 1
    FEMEA = 2

class Alimentacao(Enum):
    HERBIVORO = 1
    CARNIVORO = 2
    ONIVORO = 3

# ===== CLASSES =====
class Especie:
    def __init__(self, nome):
        self.nome: str = nome
        self.numero: int = 0
        self.seresVivos: list["SerVivo"] = []

class Habitate:
    def __init__(self, nome: str, caracteristicasVantajosas: list[str]):
        self.nome: str = nome
        self.caracteristicasVantajosas: list[str] = caracteristicasVantajosas

class SerVivo:
    def __init__(self, nomeEspecie: str, expectativa_vida: int, fertilidade: float, tamanho: float, peso: float, 
                 velocidade: float, forca: int, sexo: Sexo, agressividade: int, inteligencia: int, sociabilidade: int, 
                 habitate: Habitate, alimentacao: Alimentacao, pai: "SerVivo"=None, mae: "SerVivo"=None):
        if nomeEspecie not in especies:
            especies[nomeEspecie] = Especie(nomeEspecie)
        self.especie: Especie = especies[nomeEspecie]
        self.especie.numero += 1
        self.especie.seresVivos.append(self)
        self.nome: str = f"{self.especie.nome}{self.especie.numero}"
        self.pai: "SerVivo" = pai
        self.mae: "SerVivo" = mae
        self.caracteristicas: dict = {
            "idade": 0,
            "expectativa_vida": validarNumero(expectativa_vida, 1, 10000),
            "saude": 100.0,
            "fertilidade": validarNumero(fertilidade, 0, 100),
            "tamanho": validarNumero(tamanho, 0.001, 1000),
            "peso": validarNumero(peso, 0.00000001, 10000000),
            "velocidade": validarNumero(velocidade, 0.000001, 1000),
            "sexo": sexo,
            "forca": validarNumero(forca, 1, 100),
            "agressividade": validarNumero(agressividade, 1, 100),
            "inteligencia": validarNumero(inteligencia, 1, 100),
            "sociabilidade": validarNumero(sociabilidade, 1, 100),
            "habitat": habitate,
            "alimentacao": alimentacao
        }

# ===== DADOS GLOBAIS =====
especies: dict[str, Especie] = {}
habitates: dict[str, Habitate] = {}

# ===== FUNÇÕES =====
def validarNumero(num, minimo, maximo):
    return max(min(num, maximo), minimo)

def atualizar_listas():
    """Atualiza as listas da interface gráfica"""
    list_especies.delete(0, tk.END)
    for nome in especies:
        list_especies.insert(tk.END, nome)

    list_seres.delete(0, tk.END)
    for especie in especies.values():
        for ser in especie.seresVivos:
            list_seres.insert(tk.END, ser.nome)

    list_habitats.delete(0, tk.END)
    for nome in habitates:
        list_habitats.insert(tk.END, nome)

def mostrar_detalhes(event, origem):
    selecao = origem.curselection()
    if not selecao:
        return
    nome = origem.get(selecao[0])
    texto = ""

    if origem == list_especies:
        obj = especies[nome]
        texto += f"Espécie: {obj.nome}\n"
        texto += f"Número de Seres Vivos: {obj.numero}\n"
        texto += "Seres Vivos:\n"
        for ser in obj.seresVivos:
            texto += f"  - {ser.nome}\n"

    elif origem == list_seres:
        # Buscar o ser vivo
        ser_obj = None
        for especie in especies.values():
            for ser in especie.seresVivos:
                if ser.nome == nome:
                    ser_obj = ser
                    break
            if ser_obj:
                break

        if ser_obj:
            texto += f"Ser Vivo: {ser_obj.nome}\n"
            texto += f"Espécie: {ser_obj.especie.nome}\n"
            texto += f"Pai: {ser_obj.pai.nome if ser_obj.pai else 'Nenhum'}\n"
            texto += f"Mãe: {ser_obj.mae.nome if ser_obj.mae else 'Nenhuma'}\n"
            texto += f"Habitat: {ser_obj.caracteristicas['habitat'].nome}\n"
            texto += f"Alimentação: {ser_obj.caracteristicas['alimentacao'].name}\n"
            texto += "Características detalhadas:\n"
            for k, v in ser_obj.caracteristicas.items():
                if k not in ["habitat", "alimentacao"]:  # já mostramos acima
                    texto += f"  {k}: {v}\n"

    elif origem == list_habitats:
        obj = habitates[nome]
        texto += f"Habitat: {obj.nome}\n"
        texto += "Características Vantajosas/Desvantajosas:\n"
        for c in obj.caracteristicasVantajosas:
            texto += f"  - {c}\n"

    details.delete(1.0, tk.END)
    details.insert(tk.END, texto)

# ===== CRIAÇÃO DE SERES =====
def criar_ser_aleatorio():
    especie_nome = "EspecieAleatoria"
    expectativa_vida = random.randint(10, 500)
    fertilidade = random.uniform(0, 100)
    tamanho = random.uniform(0.1, 10)
    peso = random.uniform(1, 500)
    velocidade = random.uniform(0.1, 50)
    forca = random.randint(1, 100)
    sexo = random.choice(list(Sexo))
    agressividade = random.randint(1, 100)
    inteligencia = random.randint(1, 100)
    sociabilidade = random.randint(1, 100)
    habitate = Habitate("Floresta", ["camuflagem", "velocidade"])
    habitates[habitate.nome] = habitate
    alimentacao = random.choice(list(Alimentacao))

    ser = SerVivo(especie_nome, expectativa_vida, fertilidade, tamanho, peso, velocidade,
                  forca, sexo, agressividade, inteligencia, sociabilidade, habitate, alimentacao)

    console.insert(tk.END, f"Ser Vivo criado aleatoriamente: {ser.nome}\n")
    atualizar_listas()

def criar_ser_manual():
    janela = tk.Toplevel(root)
    janela.title("Criar Ser Vivo Manualmente")

    campos = {
        "especie": tk.Entry(janela),
        "expectativa_vida": tk.Entry(janela),
        "fertilidade": tk.Entry(janela),
        "tamanho": tk.Entry(janela),
        "peso": tk.Entry(janela),
        "velocidade": tk.Entry(janela),
        "forca": tk.Entry(janela),
        "agressividade": tk.Entry(janela),
        "inteligencia": tk.Entry(janela),
        "sociabilidade": tk.Entry(janela)
    }

    row = 0
    for label, entry in campos.items():
        tk.Label(janela, text=label.capitalize()).grid(row=row, column=0, padx=5, pady=5)
        entry.grid(row=row, column=1, padx=5, pady=5)
        row += 1

    tk.Label(janela, text="Sexo").grid(row=row, column=0, padx=5, pady=5)
    sexo_var = tk.StringVar(value="MACHO")
    tk.OptionMenu(janela, sexo_var, "MACHO", "FEMEA").grid(row=row, column=1, padx=5, pady=5)
    row += 1

    tk.Label(janela, text="Alimentação").grid(row=row, column=0, padx=5, pady=5)
    alim_var = tk.StringVar(value="HERBIVORO")
    tk.OptionMenu(janela, alim_var, "HERBIVORO", "CARNIVORO", "ONIVORO").grid(row=row, column=1, padx=5, pady=5)
    row += 1

    def salvar():
        especie_nome = campos["especie"].get()
        expectativa_vida = int(campos["expectativa_vida"].get())
        fertilidade = float(campos["fertilidade"].get())
        tamanho = float(campos["tamanho"].get())
        peso = float(campos["peso"].get())
        velocidade = float(campos["velocidade"].get())
        forca = int(campos["forca"].get())
        agressividade = int(campos["agressividade"].get())
        inteligencia = int(campos["inteligencia"].get())
        sociabilidade = int(campos["sociabilidade"].get())
        sexo = Sexo[sexo_var.get()]
        alimentacao = Alimentacao[alim_var.get()]
        habitate = Habitate("Floresta", ["camuflagem", "velocidade"])
        habitates[habitate.nome] = habitate

        ser = SerVivo(especie_nome, expectativa_vida, fertilidade, tamanho, peso, velocidade,
                      forca, sexo, agressividade, inteligencia, sociabilidade, habitate, alimentacao)

        console.insert(tk.END, f"Ser Vivo criado manualmente: {ser.nome}\n")
        atualizar_listas()
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=row, column=0, columnspan=2, pady=10)

# ===== CRIAÇÃO DE HABITATS =====
def criar_habitat():
    janela = tk.Toplevel(root)
    janela.title("Criar Habitat")

    # Nome do habitat
    tk.Label(janela, text="Nome do Habitat").grid(row=0, column=0, padx=5, pady=5)
    nome_entry = tk.Entry(janela, width=30)
    nome_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

    # Dropdown de características
    caracteristicas_possiveis = [
        "Camuflagem", "Velocidade", "Força", "Inteligência", "Sociabilidade",
        "Resistência ao frio", "Resistência ao calor", "Visão noturna"
    ]
    caract_var = tk.StringVar(value=caracteristicas_possiveis[0])
    tk.Label(janela, text="Características").grid(row=1, column=0, padx=5, pady=5)
    tk.OptionMenu(janela, caract_var, *caracteristicas_possiveis).grid(row=1, column=1, padx=5, pady=5)

    # Funções para adicionar características
    def adicionar_vantajosa():
        valor = caract_var.get()
        if valor not in lista_vantajosas.get(0, tk.END):
            lista_vantajosas.insert(tk.END, valor)

    def adicionar_desvantajosa():
        valor = caract_var.get()
        if valor not in lista_desvantajosas.get(0, tk.END):
            lista_desvantajosas.insert(tk.END, valor)

    # Botões de adicionar
    tk.Button(janela, text="Adicionar Vantajosa", command=adicionar_vantajosa).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(janela, text="Adicionar Desvantajosa", command=adicionar_desvantajosa).grid(row=1, column=3, padx=5, pady=5)

    # Listboxes para mostrar as listas
    tk.Label(janela, text="Vantajosas").grid(row=2, column=0, padx=5, pady=5)
    lista_vantajosas = tk.Listbox(janela, width=30, height=5)
    lista_vantajosas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    tk.Label(janela, text="Desvantajosas").grid(row=2, column=2, padx=5, pady=5)
    lista_desvantajosas = tk.Listbox(janela, width=30, height=5)
    lista_desvantajosas.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

    # Função para remover item com duplo clique
    def remover_item(lista):
        selecao = lista.curselection()
        if selecao:
            lista.delete(selecao[0])

    lista_vantajosas.bind("<Double-Button-1>", lambda e: remover_item(lista_vantajosas))
    lista_desvantajosas.bind("<Double-Button-1>", lambda e: remover_item(lista_desvantajosas))

    # Botão salvar habitat
    def salvar():
        nome = nome_entry.get()
        vantajosas = list(lista_vantajosas.get(0, tk.END))
        desvantajosas = list(lista_desvantajosas.get(0, tk.END))

        if nome.strip() == "":
            console.insert(tk.END, "Erro: Nome do habitat vazio!\n")
            return

        hab = Habitate(nome, vantajosas + desvantajosas)
        habitates[nome] = hab

        console.insert(tk.END, f"Habitat criado: {nome}\n"
                                f"Vantajosas: {vantajosas}\n"
                                f"Desvantajosas: {desvantajosas}\n")
        atualizar_listas()
        janela.destroy()

    tk.Button(janela, text="Salvar Habitat", command=salvar).grid(row=4, column=0, columnspan=4, pady=10)

# ===== GUI =====
root = tk.Tk()
root.title("Simulação de Seres Vivos")
root.geometry("1300x600")

# Divisão em 4 áreas
frame_console = tk.Frame(root, bd=2, relief="groove")
frame_console.pack(side="left", fill="both", expand=True)

frame_especies = tk.Frame(root, bd=2, relief="groove")
frame_especies.pack(side="left", fill="both", expand=True)

frame_seres = tk.Frame(root, bd=2, relief="groove")
frame_seres.pack(side="left", fill="both", expand=True)

frame_habitats = tk.Frame(root, bd=2, relief="groove")
frame_habitats.pack(side="left", fill="both", expand=True)

# Console
tk.Label(frame_console, text="Console").pack()
console = scrolledtext.ScrolledText(frame_console, height=15)
console.pack(fill="both", expand=True)
tk.Button(frame_console, text="Criar Ser Manualmente", command=criar_ser_manual).pack(pady=5)
tk.Button(frame_console, text="Criar Ser Aleatoriamente", command=criar_ser_aleatorio).pack(pady=5)
tk.Button(frame_console, text="Criar Habitat", command=criar_habitat).pack(pady=5)

# Listas
tk.Label(frame_especies, text="Espécies").pack()
list_especies = tk.Listbox(frame_especies)
list_especies.pack(fill="both", expand=True)

tk.Label(frame_seres, text="Seres Vivos").pack()
list_seres = tk.Listbox(frame_seres)
list_seres.pack(fill="both", expand=True)

tk.Label(frame_habitats, text="Habitats").pack()
list_habitats = tk.Listbox(frame_habitats)
list_habitats.pack(fill="both", expand=True)

# Área de detalhes
details = scrolledtext.ScrolledText(root, height=10)
details.pack(fill="x", pady=5)

# Eventos
list_especies.bind("<<ListboxSelect>>", lambda e: mostrar_detalhes(e, list_especies))
list_seres.bind("<<ListboxSelect>>", lambda e: mostrar_detalhes(e, list_seres))
list_habitats.bind("<<ListboxSelect>>", lambda e: mostrar_detalhes(e, list_habitats))

root.mainloop()
