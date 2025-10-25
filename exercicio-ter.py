#atividade 1
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print(f"O maior numero é: {n1}")
elif n2 > n1:
    print(f"O maior numero é: {n2}")
else:
    print("Os dois numeros sao iguais")
soma = n1 + n2
div = n1 / n2

print(f"O resultado da soma dos 2 numeros é: {soma}")
print(f"A divisao entre os dois numeros é: {div}")


