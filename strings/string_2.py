nome = "Emmanuel"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Emmanuel", "idade": 28}

print("Nome: %s   Idade: %d" % (nome, idade))
print("Nome: {}   Idade: {}" .format(nome, idade))
print("Nome: {0}   Idade: {1}" .format(nome, idade))
print("Nome: {nome}   Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {nome}   Idade: {idade}" .format(**dados))