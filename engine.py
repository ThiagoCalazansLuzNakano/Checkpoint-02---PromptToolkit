def obter_prompts(tarefa):
    return {
        "Zero-Shot": f"Execute de forma direta: {tarefa}",
        "Few-Shot": f"Exemplo: Analisar dados -> Relatório. Tarefa: {tarefa}",
        "Chain of Thought": f"Tarefa: {tarefa}. Pense passo a passo.",
        "Persona": f"Aja como um CEO Sênior. Resolva: {tarefa}"
    }

def gerar_comparativo(tarefa, resultados):
    return f"""
    Analise as respostas para a tarefa '{tarefa}':
    1. Zero-Shot: {resultados['Zero-Shot']}
    2. Few-Shot: {resultados['Few-Shot']}
    3. CoT: {resultados['Chain of Thought']}
    4. Persona: {resultados['Persona']}
    
    Qual técnica foi melhor e por quê?
    """
