resultados = []

print("""1 = cesta de 1 ponto\n
2 = cesta de 2 pontos\n
3 = cesta de 3 pontos\n
0 = arremesso errado\n
""")

def registrar():
    for i in range(0, 9):
        while True:
            resultado = int(input("Qual o resultado? "))
            if(resultado > 3 or resultado < 0):
                print("Coloque um resultado valido")
                continue
            else:
                resultados.append(resultado)
                break

def convertidos():
    convertidos = 0
    
    for i in range(0, 9):
        if(resultados[i] > 0):
            convertidos+=1

    return convertidos

def errados():
    errados = 0
    
    for i in range(0, 9):
        if(resultados[i] <= 0):
            errados+=1

    return errados
    

registrar()
print(f"Pontos : {sum(resultados)}")
print(f"Convertidos : {convertidos()}")
print(f"Errados : {errados()}")

print(f"Aproveitamento : {(convertidos() / 10) * 100}%")
print(f"Mais frequente : {max(set(resultados), key=resultados.count)}")