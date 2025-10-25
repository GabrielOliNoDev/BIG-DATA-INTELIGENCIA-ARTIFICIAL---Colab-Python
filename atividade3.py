#atividade3
num = int(input("Insira um numero: "))
soma = 0
print("Numeros pares de 0 ate", num, ":")
for i in range(0, num + 1, 2):
    print(i, end="")
    soma += i
print(f"\nA soma dos numeros pares é: {soma}")