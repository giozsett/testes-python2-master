# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, 
# classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

print("----------------------")
print("CLASSIFICAÇÃO DE NOTAS")
print("----------------------")
print(".")
print(".")

nota = float(input("Informe uma nota de 0 a 100:"))
classif = ""
print(".")


if nota <= 100:
    if nota <= 89:
        if nota <= 79:
            if nota <= 69:
                if nota < 60: classif = "F"
                else: classif = "D"
            else: classif = "C"
        else: classif = "B"
    else: classif = "A"
else: classif = "ERRO - Desculpe, apenas são classificadas notas de 0 a 100."


print(f"Sua nota foi: {nota}")
print(f"A classificação obtida foi: {classif}")
