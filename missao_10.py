# Missão 10: Contando Letras 🔄

# O sistema precisa contar quantas letras há em um nome.

# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

def contar_letras(nome):
    return(f"O nome {nome} tem {len(nome)} letras.")

nome = input("Digite um nome: ")
print(contar_letras(nome))