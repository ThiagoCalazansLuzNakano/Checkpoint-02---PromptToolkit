import json
from src.prompt_builder import montar_prompt
from src.evaluator import enviar_e_medir
from src.llm_client import MODEL_NAME

def executar_testes_tecnicas(client, tarefa_key, tarefa_dict):
    # Carrega inputs reais
    with open("data/inputs.json", "r", encoding="utf-8") as f:
        inputs_data = json.load(f)
    
    # Carrega personas
    with open("prompts/system_prompts.json", "r", encoding="utf-8") as f:
        personas_data = json.load(f)
        
    inputs_reais = inputs_data.get(tarefa_key, [])
    persona_texto = personas_data.get(tarefa_dict['persona_chave'], "")
    
    tecnicas = ["Zero-Shot", "Few-Shot", "Chain of Thought", "Persona"]
    tabela_resultados = []
    
    # Executa a matriz Técnica x Input
    for tecnica in tecnicas:
        print(f"   ⚙️ Avaliando tecnica: {tecnica}...")
        for idx, item in enumerate(inputs_reais, 1):
            prompt_final = montar_prompt(tecnica, tarefa_dict, item['input'], persona_texto)
            res = enviar_e_medir(client, MODEL_NAME, prompt_final, temperature=0.3)
            
            tabela_resultados.append({
                "tecnica": tecnica,
                "input_idx": idx,
                "input_texto": item['input'],
                "esperado": item['esperado'],
                "obtido": res['texto'],
                "tokens": res['tokens'],
                "tempo": res['tempo']
            })
            
    return tabela_resultados
