#AND para ser TRUE tudo tem que ser true
#OR para ser TRUE apenas um tem que ser true


print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print(False and True)

saldo = 1000
saque = 250
limite = 200
conta_especial = True


exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp2 = (saldo >= saque and saldo <= limite) or (conta_especial and saque >= saldo)

print(exp2)


conta_normal_saldo_suficiente = (saldo >= saque and saldo <= limite)
conta_especial_com_saldo = (conta_especial and saldo >= saque)

exp3 = conta_normal_saldo_suficiente or conta_especial_com_saldo

print(exp3)