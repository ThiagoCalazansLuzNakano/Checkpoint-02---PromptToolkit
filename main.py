import config
import engine
import utils

def main():
    # 1. Setup
    client = config.setup_ambiente()
    TAREFA_TESTE = "Plano de expansão para uma pequena manufatura de móveis sustentáveis"
    
    # 2. Execução da Matriz
    print(f"🚀 Iniciando Matriz de Teste para: {TAREFA_TESTE}\n")
    resultados = engine.executar_matriz(client, TAREFA_TESTE)
    
    # 3. Exibição
    utils.imprimir_resultados(resultados)
    
    # 4. Recomendação (Juiz)
    print("\n🤖 IA ANALISANDO A MELHOR COMBINAÇÃO...")
    resumo = utils.formatar_resumo_juiz(resultados)
    
    prompt_juiz = f"""
    Com base nas variações abaixo, recomende qual técnica e temperatura 
    é a mais profissional para a tarefa: '{TAREFA_TESTE}'.
    {resumo}
    """
    
    veredito = engine.chamar_llm(client, prompt_juiz, temperature=0.2)
    
    print("\n" + "🏆" * 15)
    print("RECOMENDAÇÃO FINAL:")
    print(veredito['texto'])
    print("🏆" * 15)

if __name__ == "__main__":
    main()
