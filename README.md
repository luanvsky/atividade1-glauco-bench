# 

## Gemini

Eu faço parte da Equipe 4 (Domínio Jurídico) e fiquei responsável por:

Questões abertas: 107 a 118
Questões de múltipla escolha: 1108 a 1230

A atividade envolve:

Curadoria dos dados
Inferência com LLMs
Avaliação das respostas


### Objetivo

> Avaliação da qualidade de respostas jurídicas geradas por LLMs em exames da OAB

🧪 Metodologia

A atividade foi conduzida no domínio jurídico utilizando o dataset OAB Bench, conforme proposto na atividade. Cada integrante atuou como curador de um subconjunto de questões, sendo este trabalho referente às questões 107 a 118 e 1108 a 1230.
Inicialmente, foi realizada a curadoria das questões, classificando-as quanto ao nível de dificuldade, área jurídica e base normativa. Em seguida, as questões abertas foram submetidas a três modelos de linguagem distintos, com o objetivo de comparar suas capacidades de argumentação jurídica.

As respostas geradas foram avaliadas com base em critérios definidos nos guidelines, considerando:

- Correção jurídica
- Fundamentação legal
- Coesão e clareza
- Completude da resposta

Por fim, foi realizada uma análise comparativa entre os modelos, identificando padrões de desempenho e limitações.

**🚀 O que entregar**
✔ Respostas completas das questões 107 a 108 (abertas) e 1108 a 1230 (objetivas)
✔ Classificação (curadoria)
✔ Respostas simuladas (modelo ideal)
✔ Referências reais
✔ Base para comparar LLMs

*exemplo:*


✅ 1. CURADORIA DA QUESTÃO

📌 Classificação sugerida (Equipe 4 pode usar isso como padrão)

Nível de dificuldade: Alta

Área de especialidade: Direito Empresarial

Subárea: Recuperação Judicial e Falência

Tipo de questão: Peça prático-profissional

Base legal principal:

Lei nº 11.101/2005 (Lei de Recuperação Judicial e Falência)

✅ 2. IDENTIFICAÇÃO DO PROBLEMA JURÍDICO

A questão trata de uma empresa em crise econômico-financeira que deseja:

Evitar a falência

Reestruturar suas dívidas

Manter sua atividade empresarial

👉 Ou seja, o instituto jurídico central é:

✔ Recuperação Judicial

✅ 3. PEÇA PROCESSUAL ADEQUADA

📌 Resposta correta:

Petição Inicial de Recuperação Judicial_

✅ 4. MODELO DE RESPOSTA (PADRÃO OURO)
Você pode usar isso como gabarito ideal para comparar LLMs:

📝 PEÇA PRÁTICO-PROFISSIONAL
Excelentíssimo Senhor Doutor Juiz de Direito da Vara Única da Comarca de Caxambu/MG
Comercial e Exportadora Três Pontas S.A., sociedade empresária, já qualificada, por seu advogado (instrumento de mandato anexo), vem, respeitosamente, à presença de Vossa Excelência, com fundamento nos artigos 47 e seguintes da Lei nº 11.101/2005, propor:
PEDIDO DE RECUPERAÇÃO JUDICIAL pelos fatos e fundamentos a seguir expostos:
I – DOS FATOS
A requerente é sociedade empresária regularmente constituída, atuando no ramo de exportação de café.
Em razão da pandemia da COVID-19 e de eventos climáticos adversos (geada), sofreu grave impacto financeiro, com redução significativa de receitas e aumento do passivo, atualmente estimado em R$ 17.000.000,00. Apesar das dificuldades, a empresa demonstra viabilidade econômica, considerando:
Perspectiva de recuperação do mercado
Retorno de clientes internacionais
Alta do preço da commodity
II – DO DIREITO
A recuperação judicial tem como objetivo viabilizar a superação da crise econômico-financeira da empresa, preservando sua função social e estimulando a atividade econômica. A requerente preenche os requisitos legais para o pedido, uma vez que:
Exerce regularmente suas atividades há mais de 2 anos. Não é falida. Não obteve recuperação judicial recente. A aprovação em assembleia geral reforça a legitimidade do pedido.
III – DA NECESSIDADE DA RECUPERAÇÃO
A medida é necessária para:
Evitar a falência
Reorganizar o passivo
Manter empregos
Preservar a atividade empresarial
IV – DOS PEDIDOS
Diante do exposto, requer:
O deferimento do processamento da recuperação judicial. A suspensão das ações e execuções contra a empresa. A nomeação de administrador judicial. A apresentação do plano de recuperação no prazo legal. A intimação do Ministério Público. A concessão final da recuperação judicial. Termos em que,
Pede deferimento.
Local: ...
Data: ...
Advogado: ...
OAB: ..._


📌 Curadoria das Questões de Múltipla Escolha

As questões de múltipla escolha foram classificadas predominantemente como de nível médio, com base na exigência de interpretação simples da legislação e aplicação direta de dispositivos normativos.

Observou-se que a maioria das questões exigia conhecimento de lei seca, especialmente do Código Civil e da Lei de Recuperação Judicial, com baixa ambiguidade e foco em conceitos objetivos.

Algumas questões, entretanto, apresentaram maior complexidade, exigindo análise de casos práticos e integração de dispositivos legais, sendo classificadas como difíceis.




📊 Avaliação dos Modelos com Gabarito Oficial

Foi realizada a comparação entre dois modelos de linguagem (Deepseek e Qwen) utilizando como referência o gabarito oficial das questões.

A métrica principal adotada foi a acurácia, calculada com base na proporção de respostas corretas em relação ao total de questões analisadas.

Os resultados indicaram que o modelo `Qwen 2.5-3B` apresentou maior taxa de acerto, seguido pelo Claude e, por fim, o Gemini, que apresentou maior variabilidade nas respostas.

Essa análise evidencia que, embora os modelos de linguagem apresentem bom desempenho em questões objetivas, ainda existem diferenças significativas em sua capacidade de precisão jurídica.


✅ 5. COMO USEI ISSO NA ATIVIDADE

Agora posso:

✔ Comparar LLMs:
Para cada modelo (Deepseek, Gemini, Qwen, Llama etc.), avalie:
Correção da peça (acertou recuperação judicial?)
Estrutura jurídica
Fundamentação
Clareza

✔ Métrica sugerida:
Fácil a Muito Difícil para cada critério:
Correção jurídica
Fundamentação
Coesão
Completude

🧠 O QUE TENHO EM MÃOS

Download realizado no Hugging Face:

question.jsonl → 210 questões
guidelines.jsonl → critérios de correção por questão
judge_prompts.jsonl → prompts para avaliar respostas com LLMs

👉 Isso é exatamente o fluxo de um sistema de avaliação automatizada.

⚙️ PIPELINE DA ATIVIDADE

Eu precissei seguir essa lógica:

1. Selecionar as questões
107 a 118 e 1108 a 1230

2. Gerar respostas com 3 LLMs
Deepseek
Gemini
Qwen
Llama

Para cada questão: `Pergunta → enviar para 3 modelos → coletar respostas`

3. Aplicar o JUDGE (avaliação)
Aqui entra o judge_prompts.jsonl.
Você vai usar um modelo (ex: GPT) como avaliador.
Ele recebe:

- Pergunta
- Resposta do modelo
- Guideline

E devolve:

- Nota
- Justificativa
> Nota: não utilizado em substituição foi usado o Bertsocre.

4. Usar os GUIDELINES

O arquivo guidelines.jsonl é essencial.

Ele define:

- O que é uma resposta correta
- O que deve ser avaliado

👉 Isso evita avaliação subjetiva.


📊 ESTRUTURA FINAL

🔹 Tabela de Avaliação

🔹 Análise comparativa

📌 Análise dos Resultados

A análise das respostas geradas pelos modelos de linguagem revelou diferenças significativas em termos de desempenho jurídico.O modelo Gemini 2.5-Flash apresentou maior consistência na identificação do instituto jurídico adequado, especialmente em questões que exigiam 

a elaboração de peças processuais, como pedidos de recuperação judicial. Além disso, demonstrou maior capacidade de articulação normativa. 

O modelo Qwen apresentou respostas mais genéricas, com menor profundidade na fundamentação jurídica, embora tenha mantido boa clareza textual.

O modelo Llama-3-8B destacou-se pela organização e coesão das respostas, mas apresentou, em alguns casos, lacunas na aplicação correta de dispositivos legais específicos.

De forma geral, observa-se que modelos mais robustos tendem a apresentar melhor desempenho em tarefas que exigem raciocínio jurídico estruturado.


# 📊 Análise Comparativa: Pontos Fortes e Limitações

Esta análise resume o comportamento dos modelos testados no domínio jurídico (OAB).

### 1. Gemini 2.5-Flash (Google)
*   **Pontos Fortes:**
    *   **Maior Precisão Semântica:** Liderou o BERTScore (0.6670), demonstrando melhor uso de terminologia técnica jurídica.
    *   **Raciocínio Analítico:** Capaz de estruturar fundamentações legais complexas alinhadas à banca FGV.
*   **Limitações:**
    *   **Instabilidade de Cota:** Erros frequentes de limite de requisição (429) na versão gratuita, dificultando o processamento de grandes lotes.
    *   **Dependência de Nuvem:** Requer conexão constante e chaves de API válidas.

### 2. Qwen 2.5-3B (Alibaba - Local)
*   **Pontos Fortes:**
    *   **Versatilidade Local:** Rodou inteiramente na GPU do Colab sem limites de cota.
    *   **Surpresa em Objetivas:** Obteve a melhor acurácia em múltipla escolha (43.09%), superando modelos maiores em lógica direta.
    *   **Equilíbrio:** Segundo melhor em questões abertas (0.6144).
*   **Limitações:**
    *   **Concisão Excessiva:** Às vezes simplifica demais teses jurídicas que exigem maior exaustão de itens do espelho de correção.

### 3. Llama-3-8B (Meta)
*   **Pontos Fortes:**
    *   **Acesso via API:** Fácil integração através da Hugging Face API.
    *   **Fluidez Textual:** Gera textos naturais e bem estruturados.
*   **Limitações:**
    *   **Genérico:** Apresentou o menor BERTScore (0.5281), tendendo a respostas mais superficiais ou menos aderentes ao "juridiquês" específico do Brasil.

### 4. DeepSeek-R1-Distill-1.5B (Local)
*   **Pontos Fortes:**
    *   **Extrema Leveza:** Modelo ultraleve que ocupa pouquíssima memória VRAM.
    *   **Especialidade:** Focado em raciocínio (Chain of Thought).
*   **Limitações:**
    *   **Baixa Acurácia Objetiva:** Apenas 25.20% de acerto em múltipla escolha, indicando que o tamanho reduzido (1.5B) prejudica o armazenamento de conhecimento jurídico vasto.

--- 
**Conclusão da Equipe 4:** Para curadoria profissional, o **Gemini** é o padrão-ouro em qualidade, mas o **Qwen 2.5-3B** é a ferramenta mais eficiente para automação local e triagem de questões objetivas.


### 📊 Tabela Comparativa Detalhada: Desempenho no Domínio Jurídico

| Atributo | Gemini 2.5-Flash | Qwen 2.5-3B | Llama-3-8B | DeepSeek-R1-1.5B |
| :--- | :--- | :--- | :--- | :--- |
| **Média BERTScore (F1)** | **0.6670** (1º) | 0.6144 (2º) | 0.5281 (3º) | N/A |
| **Acurácia Objetivas** | N/A* | **43.09%** | N/A | 25.20% |
| **Tipo de Execução** | Cloud (API Google) | **Local (GPU T4)** | Cloud (API HF) | **Local (GPU T4)** |
| **Principais Temas** | D. Penal, Tributário | Geral / Objetivas | Geral | Raciocínio Lógico |
| **Estilo de Resposta** | Analítico / Extenso | Direto / Técnico | Fluido / Genérico | CoT (Pensamento) |
| **Confiabilidade** | Baixa (Erros 429) | **Alta (Sem limites)** | Média (Estabilidade) | **Alta (Sem limites)** |
| **Custo Computacional** | Zero Local | Baixo (3B Params) | Zero Local | **Mínimo (1.5B Params)** |

\* *O Gemini não concluiu o lote de objetivas devido a restrições severas de cota da API durante os testes.*

#### **Legenda de Destaques:**
*   **🥇 Gemini 2.5-Flash:** Vencedor em qualidade técnica e profundidade de fundamentação legal.
*   **🚀 Qwen 2.5-3B:** Vencedor em eficiência prática, sendo o mais equilibrado para uso automatizado sem interrupções.
*   **🧠 DeepSeek-R1:** Modelo experimental focado em "Cadeia de Pensamento", útil para triagem inicial rápida.



<img width="1374" height="784" alt="image" src="https://github.com/user-attachments/assets/b6cf5610-a847-4387-855e-16d96b0060b7" />



### 💡 Principais Insights 

**1. Superioridade Semântica (Questões Abertas)**
*   **Gemini 2.5-Flash (0.6670):** Consolidou-se como o modelo mais apto para o Direito Brasileiro. Sua capacidade de estruturar respostas analíticas longas e citar fundamentação legal específica o torna o padrão-ouro para petições e peças práticas.
*   **BERTScore vs Métricas Tradicionais:** O uso do BERTScore foi crucial. Ele permitiu validar respostas que usavam sinônimos jurídicos (ex: 'cerceamento de defesa' vs 'violação do contraditório'), o que métricas de contagem de palavras (BLEU/ROUGE) falhariam em capturar.

**2. A Eficiência do Processamento Local**
*   **Qwen 2.5-3B:** Foi a maior surpresa técnica. Mesmo sendo um modelo 'pequeno', superou o Llama-3-8B em aderência semântica (0.6144) e obteve a melhor acurácia em questões objetivas (43.09%). Isso prova que modelos de 3B parâmetros são viáveis para automação jurídica com custo zero de API.

**3. O Desafio das Peças Prático-Profissionais**
*   Identificamos que modelos menores (DeepSeek 1.5B) sofrem com a 'alucinação estrutural' em peças práticas. Eles entendem o direito, mas falham em seguir o formalismo exigido pela FGV (endereçamento, qualificação, pedidos), o que exige o uso de modelos maiores ou *Few-Shot Prompting*.

**4. Desempenho em Questões Objetivas**
*   A acurácia geral (~43%) reflete a alta complexidade do exame da OAB. Notamos que os modelos performam melhor em **Filosofia do Direito e Direitos Humanos** (temas mais universais) e encontram maior dificuldade em **Direito Processual** (prazos e ritos específicos da legislação brasileira).

**5. Conclusão de Engenharia de Prompt**
*   O uso de um **System Prompt** personificado ("Você faz parte da banca examinadora da FGV") foi determinante para elevar a qualidade das fundamentações, forçando os modelos a saírem de respostas genéricas para textos baseados em raciocínio jurídico analítico.



### 🛠️ Recomendações Técnicas para Estudos Futuros

Com base nas limitações e sucessos observados, as seguintes frentes de pesquisa são recomendadas:

**1. Implementação de RAG (Retrieval-Augmented Generation)**
*   **Problema:** Modelos às vezes alucinam fundamentos legais ou citam leis revogadas.
*   **Solução:** Integrar uma base de dados vetorial (Vector DB) contendo a legislação brasileira atualizada e jurisprudência do STF/STJ. Isso permitiria que o modelo consultasse o texto real da lei antes de gerar a resposta, elevando o BERTScore.

**2. Fine-tuning Específico em Peças Práticas**
*   **Problema:** Modelos locais (3B ou menores) falham no formalismo da OAB (endereçamento, pedidos).
*   **Solução:** Realizar o ajuste fino (Fine-tuning) de modelos como o Qwen ou Llama utilizando um dataset curado de espelhos de correção da FGV, focando especificamente na estrutura de petições.

**3. Exploração de Modelos Locais de Médio Porte (7B a 14B)**
*   **Observação:** O Qwen 3B teve excelente performance em objetivas, mas sofreu em subjetivas.
*   **Estudo:** Testar modelos como Mistral 7B ou Qwen 14B via quantização (GGUF/EXL2) para verificar se o ganho em lógica jurídica justifica o maior consumo de memória RAM/VRAM.

**4. Engenharia de Prompt Multi-Agente**
*   **Solução:** Utilizar uma arquitetura de agentes onde um modelo gera a tese jurídica e outro agente (IA) atua como 'revisor da banca', criticando a resposta com base em uma checklist de critérios da FGV antes de entregar o resultado final.

**5. Expansão de Métricas de Avaliação**
*   **Sugestão:** Além do BERTScore, incorporar o **G-Eval** (utilizar um modelo superior como o GPT-4o ou Gemini 1.5-Pro para dar notas de 1 a 5 em critérios específicos como 'Fundamentação Legal' e 'Coesão'), permitindo uma análise qualitativa automatizada mais rica.




















