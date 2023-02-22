from re import sub
from typing import Callable, List
from collections import OrderedDict


def processa_soneto(file: str) -> tuple:

    def gera_lista_palavras() -> List[str]:

        pattern = "[^A-Za-z\\s]"

        with open(file, "r") as f:
            return sub(pattern, "", f.read().lower()).split()

    def remove_duplicidade(palavras: map):
        return list(OrderedDict.fromkeys(palavras))

    def conta_palavras(palavras: List[str]):
        return map(lambda p: f"{p}:{palavras.count(p)}", palavras)

    def total_ocorrencias(palavras: List[str]) -> List[str]:

        palavras.sort(key=lambda w: w.split(":")[1], reverse=True)

        return palavras

    return total_ocorrencias, \
        remove_duplicidade, \
        conta_palavras, \
        gera_lista_palavras


if __name__ == "__main__":

    total_ocorrencias, \
        remove_duplicidade, \
        conta_palavras, \
        gera_lista_palavras = processa_soneto(
            "soneto/soneto_de_fidelidade.txt")

    palavras = total_ocorrencias(remove_duplicidade(
        conta_palavras(gera_lista_palavras())))

    for palavra in palavras:
        palavra_, total = palavra.split(':')

        if int(total) > 1:
            print(f"Palavra: {palavra_:13} = {total}")
