from datetime import datetime

class Evento:
    def __init__(self, id, nome, data, local, descricao):
        self.id = id
        self.nome = nome
        self.data = data # Armazene como objeto date/datetime
        self.local = local
        self.descricao = descricao

class GerenciadorEventos:
    def __init__(self):
        self.eventos = []

    def cadastrar(self, evento):
        # Validação: evitar IDs duplicados
        self.eventos.append(evento)

    def listar_todos(self):
        return self.eventos

    def consultar_por_id(self, id):
        return next((e for e in self.eventos if e.id == id), None)

    def atualizar(self, id, **dados):
        evento = self.consultar_por_id(id)
        if evento:
            for chave, valor in dados.items():
                setattr(evento, chave, valor)
            return True
        return False

    def remover(self, id):
        evento = self.consultar_por_id(id)
        if evento:
            self.eventos.remove(evento)
            return True
        return False
