
from transformers import pipeline
import torch
# Modelo Qwen 2.5-3B ou DeepSeek-R1-Distill-Qwen-1.5B
pipe = pipeline('text-generation', model='Qwen/Qwen2.5-3B-Instruct', torch_dtype=torch.bfloat16, device_map='auto')
def run_local(prompt):
    return pipe(prompt, max_new_tokens=512)[0]['generated_text']
