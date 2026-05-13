import config

def chamar_llm(client, prompt, temperature):
    try:
        response = client.chat(
            model=config.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temperature, "num_predict": 300},
            stream=False
        )
        return {
            "texto": response['message']['content'].strip(),
            "tokens": response.get('prompt_eval_count', 0) + response.get('eval_count', 0)
        }
    except Exception as e:
        return {"texto": f"Erro: {e}", "tokens": 0}

def obter_tecnicas(tarefa):
    return {
        "Zero-Shot": f"Tarefa: {tarefa}",
        "Few-Shot": f"Exemplo: Analisar custos -> Relatório financeiro. Tarefa: {tarefa}",
        "Chain of Thought": f"Tarefa: {tarefa}. Pense passo a passo.",
        "Persona": f"Aja como um Consultor Sênior. Resolva: {tarefa}"
    }

def executar_matriz(client, tarefa):
    tecnicas = obter_tecnicas(tarefa)
    temperaturas = [0.1, 0.7, 1.5]
    matriz_resultados = {}

    for nome, prompt_texto in tecnicas.items():
        matriz_resultados[nome] = {}
        for temp in temperaturas:
            res = chamar_llm(client, prompt_texto, temperature=temp)
            matriz_resultados[nome][temp] = res
    return matriz_resultados
