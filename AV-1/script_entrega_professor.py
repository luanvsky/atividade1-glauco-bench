
# ATIVIDADE 1 - TÓPICOS AVANÇADOS (CURADORIA E INFERÊNCIA)
# EQUIPE 4 - JURÍDICO | INTEGRANTE: VICTOR

import pandas as pd
import numpy as np
from bert_score import score
import time

def carregar_e_avaliar():
    print("--- Iniciando Validação de Resultados ---")
    
    try:
        # 1. Carregamento dos dados reais do lote
        df_resultados = pd.read_csv('relatorio_final_victor_equipe4.csv')
        
        # 2. Recálculo da Média F1 para Prova de Conceito
        media_f1 = df_resultados['BERTScore_F1'].mean()
        
        print(f"Lote processado: {len(df_resultados)} questões.")
        print(f"Média BERTScore F1 obtida: {media_f1:.4f}")
        
        # 3. Exibição de amostra de fundamentação
        print("
Exemplo de Resposta IA vs Gabarito:")
        amostra = df_resultados.iloc[0]
        print(f"ID: {amostra['question_id']}")
        print(f"Resposta IA (Resumo): {amostra['response'][:100]}...")
        print(f"Gabarito (Resumo): {amostra['gabarito_oficial'][:100]}...")
        
    except FileNotFoundError:
        print("Erro: Arquivos CSV de resultados não encontrados no diretório.")

if __name__ == '__main__':
    carregar_e_avaliar()
