### **Relatório de Status: Framework de Auditoria OAB**

Este documento resume o estado atual da pipeline de avaliação baseada no paradigma **LLM-as-a-Judge**.

#### **1. Composição da Banca Examinadora**
A banca foi estabilizada utilizando modelos de alta performance via Groq, garantindo diversidade de arquitetura e consistência técnica:
*   **Juiz 1 (Meta):** Llama 3.3 (70B) - *Veredito Técnico*
*   **Juiz 2 (Alibaba):** Qwen 2.5 (32B) - *Análise de Rubrica*
*   **Juiz 3 (Meta):** Llama 3.1 (70B) - *Revisão de Estabilidade*

#### **2. Resultados do Último Processamento**
Foram auditados **36 registros** jurídicos contidos no arquivo `respostas_discursivas_victor.csv`. Os dados foram salvos no arquivo final `consenso_triplo_final_corrigido_v2.csv`.

| Métrica | Valor | Observação |
| :--- | :--- | :--- |
| **Média Geral da Banca** | ~2.57 / 10.0 | Reflete o rigor técnico exigido nas fundamentações |
| **Modelos Avaliados** | Phi-3, Qwen 2.5, TinyLlama | Diferentes arquiteturas locais |
| **Status da API** | 100% Estável | Erros '404' e 'model_decommissioned' foram corrigidos |

#### **3. Próximos Passos (Sugestão)**
*   **Visualização de Divergência:** Gerar gráficos de calor (Heatmaps) para identificar em quais temas a banca mais discorda.
*   **Análise de Outliers:** Isolar questões com alto desvio padrão para auditoria humana específica.
*   **Exportação Final:** Preparar o backup do banco SQL para entrega conforme o Barema de Excelência.


---

# 📑 Detalhamento do Pipeline de Auditoria Jurídica (OAB)

Este documento detalha a arquitetura técnica, os resultados alcançados e as pendências críticas para a entrega final da Atividade 2.

## 1. Arquitetura da Banca (LLM-as-a-Judge)
Para garantir a validade científica do projeto, a banca foi desenhada para eliminar o viés de uma única família de modelos. Utilizamos o **Groq Cloud** para garantir latência zero e alta capacidade de processamento.

### ⚖️ Composição dos Juízes:
*   **Juiz Titular (Llama 3.3 70B):** Responsável pelo parecer técnico detalhado. É o modelo com maior capacidade de raciocínio jurídico da pipeline.
*   **Juiz de Diversidade (Qwen 2.5 32B):** Modelo da Alibaba utilizado para quebrar o viés da arquitetura Llama (Meta), focando estritamente na aplicação da rubrica.
*   **Juiz de Estabilidade (Llama 3.1 70B):** Atua como o revisor de segurança, garantindo que as notas não sofram flutuações por falhas momentâneas de contexto.

## 2. Critérios de Avaliação (Rubrica FGV)
As fundamentações geradas pelos modelos locais (**Phi-3-mini**, **Qwen 2.5-1.5B** e **TinyLlama**) foram auditadas sob três pilares fundamentais:
1.  **Acurácia Jurídica (0-4 pts):** Identificação correta dos institutos de Direito (ex: competência legislativa, rito processual).
2.  **Fundamentação Legal (0-3 pts):** Citação correta de Artigos da CF/88, Códigos e Súmulas dos Tribunais Superiores.
3.  **Lógica e Coerência (0-3 pts):** Nexo causal entre a exposição dos fatos e a conclusão jurídica.

## 3. Status da Execução e Integridade de Dados
*   **Lote Processado:** 36 registros (12 questões x 3 modelos).
*   **Consistência de API:** 100% de sucesso nas chamadas após a correção do erro `model_decommissioned` (substituição do Mixtral pelo Llama 3.1).
*   **Arquivo de Saída:** `consenso_triplo_final_corrigido_v2.csv` contém todas as notas individuais e a justificativa master.

## 4. Próximas Etapas e Pendências Críticas
Para atingir o **Barema de Excelência**, as seguintes tarefas serão executadas a seguir:

### 🔍 4.1 Análise de Divergência Jurídica
Identificar os registros onde o **Desvio Padrão > 2.5**. 
*   **Objetivo:** Isolar questões onde os juízes discordaram frontalmente (ex: um deu nota 8 e outro nota 2). Isso sinaliza que a resposta da IA local foi ambígua ou que o tema é juridicamente complexo.

### 📊 4.2 Visualização de Dados (Data Viz)
Gerar gráficos avançados para o relatório final:
*   **Heatmap de Correlação:** Mostrar o quanto os juízes concordam entre si.
*   **Boxplots de Rigor:** Comparar qual juiz foi mais 'severo' e qual modelo local foi mais resiliente.
*   **Radar Chart de Rubrica:** Comparar Acurácia vs. Fundamentação vs. Lógica.

### 🗄️ 4.3 Persistência SQL e Backup
*   Exportar o dataframe final para o banco de dados `oab_audit_victor.db`.
*   Gerar o script de backup `.sql` para inclusão no repositório GitHub da equipe.

## 5. Conclusão Parcial
Até o momento, a média geral da banca (~2.57) indica que os modelos locais menores têm extrema dificuldade em manter o rigor exigido pela OAB sem o uso de técnicas de **RAG (Retrieval Augmented Generation)**. O modelo **Phi-3-mini** destaca-se como o mais promissor entre os testados localmente.
