# Sistema de Gerenciamento de Eventos 

Este projeto consiste em um MVP desenvolvido para a **Avaliação Final (AF)**. A aplicação integra os três pilares fundamentais da disciplina: **Programação Orientada a Objetos (POO)**, **Projeto de Banco de Dados** e **Interface Humano-Computador (IHC)**.

---

## I. Descrição do Projeto

O **SGE** é uma ferramenta voltada para a organização simplificada de eventos, permitindo que o usuário tenha controle total sobre o ciclo de vida de cada registro (CRUD).

### Tecnologias Utilizadas:
* **Linguagem:** Python 3.10+
* **Banco de Dados:** PostgreSQL 14
* **Prototipagem:** Figma / Whimsical (Wireframes)

---

## II. Explicação das Classes (POO)

A arquitetura do sistema foi pensada para garantir o baixo acoplamento e a alta coesão, utilizando os princípios da Orientação a Objetos.

### 1. Classe `Evento`
Representa a entidade de dados. É responsável por encapsular as informações básicas de um evento.
* **Atributos:** `id`, `nome`, `data`, `local`, `descricao`.
* **Responsabilidade:** Garantir que os dados do evento sejam válidos e consistentes.

```py
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
```

### 2. Classe `GerenciadorEventos`
Atua como a camada de serviço/lógica de negócio.
* **Métodos:** `cadastrar()`, `listar_todos()`, `consultar_por_id()`, `atualizar()` e `remover()`.
* **Responsabilidade:** Intermediar a comunicação entre os objetos de domínio e o armazenamento (memória ou banco de dados).

```py
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
```

---

## III. Projeto Físico do Banco de Dados

O banco de dados foi modelado para suportar as operações de CRUD com integridade referencial e performance.

### Estrutura da Tabela `eventos`:
```sql
CREATE TABLE eventos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    data TIMESTAMP NOT NULL,
    local VARCHAR(255) NOT NULL,
    descricao TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## IV. Wireframe

Wireframe construido com base nos requisitos do Entregavel

![Tela Inicial/Dashboard]()


Link: https://www.figma.com/board/CVrt5Vr4rMl4LFaSqT7A8q/FigJam-basics?node-id=0-1&t=Jiwa06ddnvQOMqvR-1
