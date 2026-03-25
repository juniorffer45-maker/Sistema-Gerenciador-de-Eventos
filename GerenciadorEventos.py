from datetime import datetime

class Evento:
    def __init__(self, id, nome, data, local, descricao):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.descricao = descricao

    def __repr__(self):
        return f"Evento(id={self.id}, nome='{self.nome}', data={self.data})"

class GerenciadorEventos:
    def __init__(self):
        self.eventos = []

    def cadastrar(self, evento): 
        if not isinstance(evento.data, datetime):
            raise TypeError("A data deve estar no formato datetime")
        
        if self.consultar_por_id(evento.id):
            raise ValueError("Já existe um evento com esse ID")
        
        self.eventos.append(evento)
        return "Evento cadastrado com sucesso"
        
    def listar_todos(self):
        return list(self.eventos)

    def consultar_por_id(self, id):
        return next((e for e in self.eventos if e.id == id), None)

    def atualizar(self, id, **dados):
        evento = self.consultar_por_id(id)
        if evento:
            for chave, valor in dados.items():
                if chave == "id": # Impede a mudança do ID
                    continue  

                if chave == "data" and not isinstance(valor, datetime):
                    raise TypeError("A data deve estar no formato datetime")
                
                if hasattr(evento, chave):
                    setattr(evento, chave, valor)
            return "Evento atualizado com sucesso"
        return "Evento não encontrado"

    def remover(self, id):
        evento = self.consultar_por_id(id)
        if evento:
            self.eventos.remove(evento)
            return "Evento removido com sucesso"
        return "Evento não encontrado"
