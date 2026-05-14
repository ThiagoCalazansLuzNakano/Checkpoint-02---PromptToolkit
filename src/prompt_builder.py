def montar_prompt(tecnica, tarefa_dict, input_usuario, persona_texto=None):
    base = f"Instrucao: {tarefa_dict['instrucao']}\nFormato de Saida: {tarefa_dict['formato_output']}\n"
    
    if tecnica == "Zero-Shot":
        return base + f"Entrada: {input_usuario}\nSaida:"
        
    elif tecnica == "Few-Shot":
        exemplos_str = ""
        for ex in tarefa_dict['exemplos_fewshot']:
            exemplos_str += f"Entrada: {ex['input']}\nSaida: {ex['output']}\n"
        return base + exemplos_str + f"Entrada: {input_usuario}\nSaida:"
        
    elif tecnica == "Chain of Thought":
        passos = "\n".join([f"- {p}" for p in tarefa_dict['passos_cot']])
        return base + f"Siga rigorosamente estes passos para pensar:\n{passos}\nEntrada: {input_usuario}\nSaida Pensada e Final:"
        
    elif tecnica == "Persona":
        prefixo = f"Contexto de Atuacao: {persona_texto}\n" if persona_texto else ""
        return prefixo + base + f"Entrada: {input_usuario}\nSaida:"
        
    return base + f"Entrada: {input_usuario}"
