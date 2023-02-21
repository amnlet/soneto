with open("soneto/soneto.txt", "r") as f:
    linhas = f.read().splitlines() #Aqui ele vai ler e separar as linhas e tira o \n
    matriz = {} #aqui estou usando o dictionary eu tentei [] por muito tempo o chat GPT me indicou isso, mas precisava entender
    for linha in linhas:
        palavra_de_cada_linha = linha.split() #aqui ele verifica todas as linhas e separa elas
        for palavra in palavra_de_cada_linha:
            palavra = palavra.strip(",.").lower() #aqui ele separa todas as plavaras de cada linha e deixa caps lower
            if palavra in matriz:
                matriz[palavra] += 1 #aqui ele soma para cada palavra dentro da dictionary(matriz) uma pontuacao por palavras repetidas
            else:
                matriz[palavra] = 1 #aqui ele define como 1 se houve apenas uma palavra e ela nao for repetida.

#aqui vou imprimir o codigo
print("Contador de palavras repetidas: ")
for palavra, contagem in matriz.items(): #aqui ele pega a var palavra e contagem dentro da dic matriz onde uso .items() eu entendi que ela conta todos items dentro da matriz
    if contagem > 1: #se o item for maior que 1 ele retorna o valor abaixo
        print(f"{palavra} = {contagem}") #usei o format ja conhecia
