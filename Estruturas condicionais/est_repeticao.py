texto = input("Informe o nome: ")
## input ("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: #usa o for para percorrer
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() #adiciona uma quebra de linha
  

#range

