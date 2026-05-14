from src.llm_client import MODEL_NAME
from src.evaluator import chamar_llm_com_metricas

def imprimir_resultados(resultados_finais):
    print("\n" + "="*70)
    print("📈 RESULTADOS DA MATRIZ (TÉCNICA vs TEMPERATURA)")
    print("="*70)
    for tecnica, temps in resultados_finais.items():
        print(f"\n▶️ TÉCNICA: {tecnica.upper()}")
        for t_valor, dados in temps.items():
            label = "CONSERVADOR" if t_valor == 0.1 else "EQUILIBRADO" if t_valor == 0.7 else "CRIATIVO"
            print(f"[{t_valor} - {label}] | 📊 Tokens: {dados['tokens']}")
            print(f"RESPOSTA: {dados['texto'][:150]}...")
            print("." * 15)

def gerar_recomendacao(client, tarefa, resultados_finais):
    print("\n🤖 IA ANALISANDO A MELHOR COMBINAÇÃO...")
    resumo = ""
    for t_nome, t_dados in resultados_finais.items():
        resumo += f"\n- {t_nome} (Temp 0.7): {t_dados[0.7]['texto'][:200]}"
    
    prompt_juiz = f"Baseado nos resultados, recomende a melhor abordagem para '{tarefa}':\n{resumo}"
    veredito = chamar_llm_com_metricas(client, MODEL_NAME, prompt_juiz, temperature=0.2)
    
    print("\n🏆 RECOMENDAÇÃO FINAL:")
    print(veredito['texto'])
