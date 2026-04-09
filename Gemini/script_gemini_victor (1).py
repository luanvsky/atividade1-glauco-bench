
import google.generativeai as genai
# Configuração Gemini 2.5-Flash
genai.configure(api_key='SUA_API_KEY')
model = genai.GenerativeModel('models/gemini-2.5-flash')
def run_inferencia(texto):
    return model.generate_content(f'Analise juridicamente: {texto}').text
