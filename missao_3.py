# Missão 3: Recuperando o Sistema de Notas 📊

# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

def classificacao(nota):
    if 90 <= nota <= 100:
        return ("Parabéns!! Você tirou A.")
    elif 80 <= nota < 90:
        return ("Muito bem!! Você tirou B.")
    elif 70 <= nota < 80:
        return ("Bom trabalho! Você tirou C.")
    elif 60 <= nota < 70:
        return ("Fique atento! Você tirou D.")
    elif nota < 60:
        return ("ESTUDO UM POUCO MAIS! Você tirou F.")
    
nota = float(input("Digite a sua nota: "))
print(classificacao(nota))