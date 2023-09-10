# Peça ao usuário para inserir seu salário e o tempo de serviço. Se o tempo de serviço
# for superior a 5 anos, conceda um bônus de 5% ao salário.

print("------------------------------")
print("|  CÁLCULO DE BÔNUS SALARIAL |")
print("------------------------------")
print("_")
print("_")

salario = float(input("Informe o valor de seu salário."))
tempo = int(input("Informe o tempo de serviço em anos."))


if tempo > 5: bonus = 0.05 * salario
else: bonus = 0

print("_")
print(f"Valor do salário: {salario} reais")
print(f"Tempo de serviço: {tempo} anos")
print(f"Valor do bônus: {bonus} reais") 