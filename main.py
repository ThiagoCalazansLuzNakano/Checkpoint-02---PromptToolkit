import config
import engine
import utils

def main():
    tarefa = "Desenvolver um plano de fidelização para uma petshop"
    client = config.get_client()
    
    utils.exibir_cabecalho(tarefa)
    
    # 1. Aplica técnicas
    prompts = engine.obter_prompts(tarefa)
    resultados = {}
    
    for nome, p in prompts.items():
        print(f"⏳ Processando {nome}...")
        response = client.chat(model=config.MODEL_NAME, messages=[{"role": "user", "content": p}])
        resultados[nome] = response['message']['content'].strip()
    
    # 2. Mostra detalhes
    utils.exibir_resultados(resultados)
    
    # 3. Recomendação
    print("\n🏆 ANALISANDO MELHOR ABORDAGEM...")
    prompt_final = engine.gerar_comparativo(tarefa, resultados)
    recomendacao = client.chat(model=config.MODEL_NAME, messages=[{"role": "user", "content": prompt_final}])
    
    print("\n--- RECOMENDAÇÃO FINAL ---")
    print(recomendacao['message']['content'].strip())

if __name__ == "__main__":
    main()
