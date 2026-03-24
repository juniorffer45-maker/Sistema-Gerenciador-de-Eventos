CREATE TABLE eventos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    data_evento TIMESTAMP NOT NULL,
    local VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índice para busca rápida por nome
CREATE INDEX idx_nome_evento ON eventos(nome);

-- Restrição: Não permitir eventos com nomes vazios
ALTER TABLE eventos ADD CONSTRAINT check_nome_valido CHECK (LENGTH(nome) > 0);
