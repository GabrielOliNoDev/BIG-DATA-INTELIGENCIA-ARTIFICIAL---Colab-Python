#atividade 2
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 16:
    print(f"{nome} voce esta apto para votar")
else:
    print(f"{nome} voce nao esta apto para votar")