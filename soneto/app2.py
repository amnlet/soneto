from re import sub
from typing import Callable, List
from collections import OrderedDict


def processa_soneto(file: str) -> tuple[Callable[[List[str]], List[str]], Callable[[], List[str]]]:

    def gera_lista_palavras() -> List[str]:
        
        pattern = "[^A-Za-z\\s]"

        with open(file, "r") as f:
            return sub(pattern, "", f.read().lower()).split()

    def total_ocorrencias(lista_palavras:List[str]) -> List[str]:

        palavras = list(OrderedDict.fromkeys(map(lambda x:f"{x}:{lista_palavras.count(x)}", lista_palavras)))

        palavras.sort(key=lambda w:w.split(":")[1], reverse=True)

        return palavras

    return total_ocorrencias, gera_lista_palavras

if __name__ == "__main__":

    total_ocorrencias, palavras = processa_soneto("soneto/soneto.txt")
    
    for palavra in total_ocorrencias(palavras()):
        print(palavra)
