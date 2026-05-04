# 📑 Resumo: Atividade 1 - Seleção e Teste de Modelos (Domínio Jurídico)

## 1. Objetivo Central
O foco da primeira atividade foi a seleção, configuração e teste de modelos de linguagem (LLMs) para responder a questões complexas do Direito brasileiro.
O objetivo era coletar respostas brutas para posterior avaliação de acurácia técnica.

## 2. Escopo da Equipe 4 (Jurídico)
A sua equipe trabalhou especificamente com os seguintes recursos:
Datasets Utilizados:
maritaca-ai/oab-bench: Para questões de resposta aberta (discursivas).
eduagarcia/oab_exams: Para questões de múltipla escolha.
Tarefa: Submeter esses enunciados aos modelos selecionados para gerar uma base de dados de respostas.

## 3. Execução Técnica e Metadados
Durante a Atividade 1, não bastava apenas gerar o texto; era necessário registrar informações técnicas que agora são fundamentais para o banco de dados da Atividade 2:
Identificação do Modelo: Nome (ex: Llama-3-8B) e versão.
Parâmetros de Precisão: Registro se o modelo rodou em INT4, FP16 ou outras quantizações.
Performance: Coleta do tempo de inferência (em milissegundos) para cada resposta gerada.
Armazenamento: Os resultados foram inicialmente organizados em arquivos locais (como JSON ou CSV) antes de serem migrados para o PostgreSQL.

## 4. Resultados Obtidos
O "produto" final da Atividade 1, que agora serve de input para o seu "Juiz-IA", consistiu em:
Texto da Resposta: A explicação ou alternativa escolhida pelo modelo.
Referência (Gabarito): A resposta correta (Resposta Ouro) que serve de base para a comparação atual.
Diversidade de Modelos: Testes com modelos de diferentes capacidades para comparar o desempenho entre eles.
