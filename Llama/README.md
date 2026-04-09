# Atividade 1 - Tópicos Avançados (Domínio Jurídico)

## 🎓 Integrante
*   **Victor** (Responsável pelo lote de questões IDs 107 a 118)
*   **Equipe:** 4

## ⚖️ Escopo do Projeto
O objetivo desta atividade foi avaliar a capacidade de resposta e fundamentação jurídica de diferentes Modelos de Linguagem (LLMs) em questões dissertativas e objetivas do Exame da OAB.

## 🛠️ Metodologia Aplicada
1.  **Inferência Analítica:** Submetemos o lote de questões a três modelos principais:
    *   **Gemini 2.5-Flash** (Cloud-based via Google API)
    *   **Llama-3-8B-Instruct** (via Hugging Face API)
    *   **Qwen 2.5-3B** (Execução Local via Transformers/PyTorch)
2.  **Métrica de Avaliação (BERTScore):** Utilizamos o BERTScore (F1) para medir a similaridade semântica entre as respostas geradas e os gabaritos oficiais (`guidelines_me.jsonl`). Esta métrica foi escolhida por capturar o "significado jurídico" além da mera sobreposição de palavras.
3.  **Simulação de Objetivas:** Realizamos a simulação de um estudante realizando o exame de múltipla escolha (`multiple_me.json`) utilizando o modelo **DeepSeek-R1-Distill-Qwen-1.5B**.

## 📊 Resultados Consolidados (Questões Abertas)
| Modelo | Média BERTScore F1 |
| :--- | :--- |
| **Gemini 2.5-Flash** | **0.6670** |
| Qwen 2.5-3B (Local) | 0.6144 |
| Llama-3-8B-Instruct | 0.5281 |

## 🎯 Performance em Questões Objetivas
*   **Modelo:** Qwen 2.5-3B / DeepSeek-R1
*   **Acurácia Obtida:** 43.09% (Qwen)
*   **Observação:** O desempenho reflete a complexidade das questões da OAB para modelos de parâmetros reduzidos sem fine-tuning específico.

## 📂 Estrutura de Arquivos da Entrega
*   `relatorio_final_victor_equipe4.csv`: Resultados e métricas detalhadas do Gemini.
*   `relatorio_final_llama_equipe4.csv`: Resultados e métricas detalhadas do Llama-3.
*   `relatorio_final_qwen_equipe4.csv`: Resultados e métricas detalhadas do Qwen 2.5.
*   `curadoria_final_Victor_G4.xlsx`: Planilha Excel com classificação por dificuldade e legislação base.
*   `script_entrega_professor.py`: Script de validação automática dos resultados.
*   `README.md`: Este arquivo de documentação.

## 💡 Conclusão
O modelo **Gemini 2.5-Flash** demonstrou a melhor performance geral, apresentando maior precisão na fundamentação legal e técnica exigida pela FGV. Modelos Open Source executados localmente (Qwen/DeepSeek) mostraram-se promissores para tarefas de classificação, mas ainda enfrentam desafios na estruturação de peças prático-profissionais complexas.
