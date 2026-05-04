# 📑 Atividade 2: Framework "LLM-as-a-Judge" e Persistência Relacional

## 1. Contexto e Objetivo

O objetivo desta etapa é implementar uma solução sofisticada para auditar as respostas geradas pelos modelos na Atividade 1. Utilizaremos o paradigma LLM-as-a-Judge para avaliar a acurácia técnica e a fundamentação jurídica, armazenando todo o ciclo de vida dos dados em um banco de dados PostgreSQL para garantir rastreabilidade profissional.

## 2. Escopo da Equipe 4 (Jurídico)

Datasets: maritaca-ai/oab-bench (Questões Abertas) e eduagarcia/oab_exams (Múltipla Escolha).
Foco: Fidelidade à legislação brasileira e detecção de "alucinações normativas" (leis inventadas).

## 3. Arquitetura do Banco de Dados (PostgreSQL)

A infraestrutura deve armazenar o dataset original, as respostas da Atividade 1 e as avaliações do Juiz. Abaixo, o esquema DDL sugerido:


```sql
-- Metadados dos Modelos
CREATE TABLE modelos (
    id_modelo SERIAL PRIMARY KEY,
    nome_modelo VARCHAR(100) NOT NULL,
    versao VARCHAR(50),
    parametro_precisao VARCHAR(20)
);

-- Datasets Utilizados
CREATE TABLE datasets (
    id_dataset SERIAL PRIMARY KEY,
    nome_dataset VARCHAR(100) NOT NULL,
    dominio VARCHAR(50) NOT NULL
);

-- Perguntas e Gabaritos (Resposta Ouro)
CREATE TABLE perguntas (
    id_pergunta SERIAL PRIMARY KEY,
    id_dataset INTEGER REFERENCES datasets(id_dataset),
    enunciado TEXT NOT NULL,
    resposta_ouro TEXT NOT NULL,
    metadados JSONB 
);

-- Respostas Geradas na Atividade 1
CREATE TABLE respostas_atividade_1 (
    id_resposta SERIAL PRIMARY KEY,
    id_pergunta INTEGER REFERENCES perguntas(id_pergunta),
    id_modelo INTEGER REFERENCES modelos(id_modelo),
    texto_resposta TEXT NOT NULL,
    tempo_inferencia_ms FLOAT,
    data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Avaliações do Juiz-IA (Atividade 2)
CREATE TABLE avaliacoes_juiz (
    id_avaliacao SERIAL PRIMARY KEY,
    id_resposta_ativa1 INTEGER REFERENCES respostas_atividade_1(id_resposta),
    id_modelo_juiz INTEGER REFERENCES modelos(id_modelo),
    nota_atribuida INTEGER CHECK (nota_atribuida BETWEEN 1 AND 5),
    chain_of_thought TEXT NOT NULL,
    data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
````

## 4. Configuração do Juiz Jurídico

O modelo Juiz deve assumir a persona de um Desembargador e Professor Doutor em Direito.

Rubrica de Avaliação (1 a 5):
Nota 1: Resposta incorreta, cita leis inexistentes ou confunde institutos básicos.
Nota 2: Conclusão correta, mas fundamentação vaga ou cita artigos errados.
Nota 3: Correta e fundamentada, mas sem clareza ou omite detalhes do gabarito.
Nota 4: Excelente, alinhada ao gabarito e com fundamentação legal precisa.
Nota 5: Excepcional, cita jurisprudência relevante (STF/STJ) e demonstra raciocínio mestre.

## 5. Análise Estatística

Utilizaremos o Coeficiente de Correlação de Spearman (ρ) para medir o alinhamento entre o Juiz-IA e o Gabarito Humano.
0.7 a 1.0: Forte alinhamento.
Abaixo de 0.3: Discordância frontal (requer análise de erro detalhada).

## 6. Entrega (Deadline: 14/05/2026 às 12h00)

Repositório GitHub: Scripts Python, prompts e backup do banco (.sql).
Tutorial PDF: Instruções de restore do banco, queries de exemplo e metodologia.
Vídeo (10-20 min): Demonstração da engenharia do banco e calibração do Juiz por todos os membros.

--------------------------------------------------------------------------------
Nota: Certifique-se de testar o comando pg_dump para gerar o backup e validar o processo de psql restore em um ambiente limpo antes da entrega
