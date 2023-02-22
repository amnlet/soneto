from re import sub

def processa_soneto(file:str):
    
    def gera_lista_palavras():
        
        pattern = "[^A-Za-z\\s]"

        with open(file, "r") as f:
            return sub(pattern, "", f.read().lower()).split()
    
    def total_ocorrencias(lista_palavras:list[str]):

            lista_palavras = gera_lista_palavras()

            num_palavras = list(map(lambda x:[x, lista_palavras.count(x)], lista_palavras))

            palavras = []

            [palavras.append(item) for item in num_palavras if item not in palavras]
            
            palavras.sort(key=lambda x:x[1], reverse=True)

            for palavra in palavras:
                print(f"{palavra[0]:10}:{palavra[1]}")
                

    return total_ocorrencias, gera_lista_palavras

if __name__ == "__main__":

    total_ocorrencias, palavras = processa_soneto("soneto/soneto.txt")
    
    total_ocorrencias(palavras())