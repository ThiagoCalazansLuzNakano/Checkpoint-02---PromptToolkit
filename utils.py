def imprimir_resultados(resultados_finais):
    print("\n" + "="*70)
    print("📈 RESULTADOS DA MATRIZ (TÉCNICA vs TEMPERATURA)")
    print("="*70)
    for tecnica, temps in resultados_finais.items():
        print(f"\n▶️ TÉCNICA: {tecnica.upper()}")
        print("-" * 30)
        for t_valor, dados in temps.items():
            label = "CONSERVADOR" if t_valor == 0.1 else "EQUILIBRADO" if t_valor == 0.7 else "CRIATIVO"
            print(f"[{t_valor} - {label}] | 📊 Tokens: {dados['tokens']}")
            print(f"RESPOSTA: {dados['texto'][:250]}...")
            print("." * 15)

def formatar_resumo_juiz(resultados_finais):
    resumo = ""
    for t_nome, t_dados in resultados_finais.items():
        resumo += f"\n- {t_nome} (Temp 0.7): {t_dados[0.7]['texto'][:300]}"
    return resumo
