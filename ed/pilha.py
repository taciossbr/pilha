
class Pilha:
    def __init__(self):
        self._pilha = []

    def vazia(self):
        return not len(self._pilha)

    def __len__(self):
        return len(self._pilha)

    def push(self, e):
        self._pilha.append(e)

    def pop(self):
        return self._pilha.pop()
