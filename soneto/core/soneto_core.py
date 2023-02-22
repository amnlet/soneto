from re import sub

from typing import Callable, List, Iterable
from collections import OrderedDict

Soneto = tuple[Callable[[list[str]], list[str]],
               Callable[[Iterable[str]], list[str]],
               Callable[[list[str]], Iterable[str]],
               Callable[[], list[str]]]


def processa_soneto(file: str) -> Soneto:

    def gera_lista_palavras() -> List[str]:

        pattern = "[^A-Za-z\\s]"

        with open(file, "r") as f:
            return sub(pattern, "", f.read().lower()).split()

    def remove_duplicidade(palavras: Iterable[str]) -> List[str]:
        return list(OrderedDict.fromkeys(palavras))

    def conta_palavras(palavras: List[str]) -> Iterable[str]:
        return map(lambda p: f"{p}:{palavras.count(p)}", palavras)

    def total_ocorrencias(palavras: List[str]) -> List[str]:

        palavras.sort(key=lambda w: w.split(":")[1], reverse=True)

        return palavras

    return total_ocorrencias, \
        remove_duplicidade, \
        conta_palavras, \
        gera_lista_palavras
