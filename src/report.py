import csv
from src.llm_client import MODEL_NAME
from src.evaluator import enviar_e_medir

def salvar_csv_e_exibir(tarefa_nome, logs):
    filename = f"output/resultados_{tarefa_nome}.csv"
    
    # Cria o arquivo CSV de métricas
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["tecnica", "input_idx", "tokens", "tempo"])
        writer.writeheader()
        for log in logs:
            writer.writerow({
                "tecnica": log["tecnica"],
                "input_idx": log["input_idx"],
                "tokens": log["tokens"],
                "tempo": log["tempo"]
            })
    print(f"   💾 Métricas de execucao salvas em: {filename}")

def avaliar_e_escolher_vencedora(client, tarefa_nome, logs):
    """Pede ao LLM analisar as execuções reais para eleger a melhor técnica para esta tarefa."""
    resumo_casos = ""
    for log in logs[:4]: # Pega uma amostra de cada técnica para avaliação rápida
        resumo_casos += f"\nTecnica: {log['tecnica']}\nEsperado: {log['esperado']}\nObtido: {log['obtido']}\n"
        
    prompt_juiz = f"""
    Como especialista em QA de IA, analise as amostras de execucao para a tarefa '{tarefa_nome}':
    {resumo_casos}
    
    Determine APENAS o nome da tecnica vencedora que demonstrou melhor aderencia ao esperado.
    Sua resposta deve conter estritamente apenas uma dessas palavras: Zero-Shot, Few-Shot, Chain of Thought ou Persona.
    """
    
    res = enviar_e_medir(client, MODEL_NAME, prompt_juiz, temperature=0.1)
    vencedora = res['texto'].strip()
    
    # Fallback caso a IA decida escrever um parágrafo
    for t in ["Zero-Shot", "Few-Shot", "Chain of Thought", "Persona"]:
        if t.lower() in vencedora.lower():
            return t
    return "Zero-Shot"
