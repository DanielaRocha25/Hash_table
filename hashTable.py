def printLine():
    print("-"*30)

# Criação da hash table A e B.
hash_tableA = {"p1":"Farofa","p2":"Arroz","p3":"Massa","p4":"Coca"}
hash_tableB = {"b1":"Refri","b2":"Suco","b3":"Cerveja","p4":"Coca"}

# Inserção de elementos no final
#for i in range(2): #Utiliza um  loop para adicionar em cada conjunto 4 números informados pelo usuário.
item_a = input("Informe um produto para adicionar ao conjunto A:")
hash_tableA["p5"] = item_a
item_b = input("Informe uma bebida para adicionar ao conjunto B:")
hash_tableB["b5"] = item_b
printLine()

#Mostra os dois conjuntos
print("Conjunto A: ",hash_tableA.values())
print("Conjunto B: ",hash_tableB.values())
printLine()

#Remoção de elementos
chave_del = input("Informe a posição (começando em p1) do elemento do conjunto A que deseja deletar: ")
del hash_tableA[chave_del]
print(f"Conjunto A após a remoção do elemento na posição {chave_del}: ",hash_tableA.values())
printLine()

#Busca de valores
item = input("Informe um valor (nome do produto ou bebida) para busca: ")
if item in hash_tableA.values() and item in hash_tableB.values():
    print(f"{item} encontrado nos conjuntos A e B.")
elif item in hash_tableA.values():
    print(f"{item} encontrado no conjunto A.")
elif item in hash_tableB.values():
    print(f"{item} encontrado no conjunto B.")
else:
    print("Elemento não encontrado.")
printLine()

#União dos conjuntos
unidos = {**hash_tableA,**hash_tableB}
print("União dos conjuntos: ", unidos.values())
printLine()

#Intersecção dos conjuntos. Retorna o item que tiver mesma chave e valor em ambos os conjuntos
interseccao = dict(hash_tableA.items() & hash_tableB.items())
print("Intersecção dos conjuntos: ",interseccao )
printLine()

#Diferença Mostra os items do conjunto B que não estão no conjunto A.
for key in hash_tableB.keys():
    if not key in hash_tableA:
        print("Diferença entre os conjuntos (chave): ", key)





