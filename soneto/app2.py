from re import sub
from typing import Callable, List
from collections import OrderedDict


def processa_soneto(file: str) -> dict:

    def gera_lista_palavras() -> List[str]:
        
        pattern = "[^A-Za-z\\s]"

        with open(file, "r") as f:
            return sub(pattern, "", f.read().lower()).split()

    def remove_duplicidade(palavras: map):
        return list(OrderedDict.fromkeys(palavras))

    def conta_palavras(palavras:List[str]):
        return map(lambda p:f"{p}:{palavras.count(p)}", palavras)

    def total_ocorrencias(palavras:List[str]) -> List[str]:

        palavras.sort(key=lambda w:w.split(":")[1], reverse=True)

        return palavras

    return {"gera_lista_palavras":gera_lista_palavras,
            "remove_duplicidade":remove_duplicidade,
            "conta_palavras":conta_palavras, 
            "total_ocorrencias":total_ocorrencias}

if __name__ == "__main__":

    fn_soneto = processa_soneto("soneto/soneto.txt")
    
    palavras = fn_soneto["total_ocorrencias"](fn_soneto["remove_duplicidade"]\
                                              (fn_soneto["conta_palavras"]\
                                               (fn_soneto["gera_lista_palavras"]())))
    
    for palavra in palavras:
        print(palavra)
