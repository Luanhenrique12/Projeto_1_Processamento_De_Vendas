arquivo= open("vendas_dia.txt", "r")

total = 0
for linha in arquivo:
    valor=float (linha.strip())
    total= total +valor

arquivo.close()
print("Soma das vendas:", total)