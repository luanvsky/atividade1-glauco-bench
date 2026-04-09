
# ATIVIDADE 1 - TÓPICOS AVANÇADOS (CURADORIA E INFERÊNCIA)
# SCRIPT DE VALIDAÇÃO OFICIAL - EQUIPE 4 JURÍDICO

import pandas as pd
import os

def validar_resultados():
    print('--- Iniciando Validação Técnica dos Resultados ---')
    
    modelos = {
        'Gemini 2.5-Flash': 'relatorio_final_victor_equipe4.csv',
        'Llama-3-8B': 'relatorio_final_llama_equipe4.csv',
        'Qwen 2.5-3B': 'relatorio_final_qwen_equipe4.csv',
        'Objetivas (Qwen)': 'performance_objetivas_qwen.csv'
    }

    for nome, path in modelos.items():
        if os.path.exists(path):
            df = pd.read_csv(path)
            if 'BERTScore_F1' in df.columns:
                score = df['BERTScore_F1'].mean()
                print(f'[OK] {nome}: Média BERTScore F1 = {score:.4f} ({len(df)} questões)')
            elif 'is_correct' in df.columns:
                acc = df['is_correct'].mean() * 100
                print(f'[OK] {nome}: Acurácia = {acc:.2f}% ({len(df)} questões)')
        else:
            print(f'[AVISO] Arquivo {path} não encontrado no diretório atual.')

    print('\n--- Amostra de Fundamentação (Gemini) ---')
    if os.path.exists('relatorio_final_victor_equipe4.csv'):
        df_g = pd.read_csv('relatorio_final_victor_equipe4.csv')
        print(f'Questão: {df_g.iloc[0]["question_id"]}')
        # Tenta pegar os primeiros 300 caracteres de resposta
        try:
            res_col = 'response' if 'response' in df_g.columns else 'Resposta Gemini'
            print(f'Resposta IA: {df_g.iloc[0][res_col][:300]}...')
        except: pass

if __name__ == "__main__":
    validar_resultados()
