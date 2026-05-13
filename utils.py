def exibir_cabecalho(tarefa):
    print(f"\n" + "="*50)
    print(f"🛠️ TOOLKIT DE PROMPTING | Tarefa: {tarefa}")
    print("="*50)

def exibir_resultados(resultados):
    for tecnica, resposta in resultados.items():
        print(f"\n▶ TÉCNICA: {tecnica}")
        print(f"RESPOSTA: {resposta}")
        print("-" * 30)
