MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda nao pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teoricas, mas nao praticas")
else:
    print("Ainda nao pode tirar a CNH")