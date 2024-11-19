import tkinter as tk

def on_button_click():
    print("Botão clicado!")

# Criar a janela principal
root = tk.Tk()
root.title("Minha Primeira Aplicação Tkinter")

# Criar um botão na janela
button = tk.Button(root, text="Clique aqui!", command=on_button_click)
button.pack(pady=20, padx=50)  # Adicionar espaço ao redor do botão

# Iniciar o loop principal da aplicação
root.mainloop()
