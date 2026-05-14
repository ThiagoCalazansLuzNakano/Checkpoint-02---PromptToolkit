from src.llm_client import setup_ambiente
from src.techniques import executar_matriz
from src.report import imprimir_resultados, gerar_recomendacao

def main():
    # 1. Inicializa o cliente
    client = setup_ambiente()
    TAREFA_TESTE = "Plano de expansão para uma pequena manufatura de móveis sustentáveis"
    
    print(f"🚀 Iniciando PromptToolkit Avançado...")
    
    # 2. Executa a matriz de testes (Técnicas vs Temperaturas)
    resultados = executar_matriz(client, TAREFA_TESTE)
    
    # 3. Exibe o relatório no console
    imprimir_resultados(resultados)
    
    # 4. Gera o veredito final
    gerar_recomendacao(client, TAREFA_TESTE, resultados)

if __name__ == "__main__":
    main()
