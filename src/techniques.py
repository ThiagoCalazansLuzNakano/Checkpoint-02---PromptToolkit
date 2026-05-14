from src.llm_client import MODEL_NAME
from src.evaluator import chamar_llm_com_metricas

def obter_prompts(tarefa):
    return {
        "Zero-Shot": f"Tarefa: {tarefa}",
        "Few-Shot": f"Exemplo: Analisar custos -> Relatório financeiro. Tarefa: {tarefa}",
        "Chain of Thought": f"Tarefa: {tarefa}. Pense passo a passo.",
        "Persona": f"Aja como um Consultor Sênior. Resolva: {tarefa}"
    }

def executar_matriz(client, tarefa):
    tecnicas = obter_prompts(tarefa)
    temperaturas = [0.1, 0.7, 1.5]
    matriz_resultados = {}

    for nome, prompt_texto in tecnicas.items():
        matriz_resultados[nome] = {}
        for temp in temperaturas:
            print(f"   📊 Processando {nome} | Temp {temp}...")
            res = chamar_llm_com_metricas(client, MODEL_NAME, prompt_texto, temp)
            matriz_resultados[nome][temp] = res
    return matriz_resultados
