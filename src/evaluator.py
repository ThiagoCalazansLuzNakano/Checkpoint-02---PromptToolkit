import time

def enviar_e_medir(client, model, prompt, temperature=0.3):
    try:
        start = time.time()
        response = client.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": temperature, "num_predict": 300},
            stream=False
        )
        tempo = round(time.time() - start, 2)
        tokens = response.get('prompt_eval_count', 0) + response.get('eval_count', 0)
        
        return {
            "texto": response['message']['content'].strip(),
            "tokens": tokens,
            "tempo": tempo
        }
    except Exception as e:
        return {"texto": f"Erro: {e}", "tokens": 0, "tempo": 0}
