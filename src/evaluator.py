def chamar_llm_com_metricas(client, model, prompt, temperature):
    try:
        response = client.chat(
            model=model,
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
