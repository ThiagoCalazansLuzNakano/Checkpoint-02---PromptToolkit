import os
from src.llm_client import setup_ambiente, MODEL_NAME
from src.tasks import TAREFAS
from src.techniques import executar_testes_tecnicas
from src.report import salvar_csv_e_exibir, avaliar_e_escolher_vencedora
from src.prompt_builder import montar_prompt
from src.evaluator import enviar_e_medir

def main():
    # Garantir pasta de saídas
    os.makedirs("output/graficos", exist_ok=True)
    
    client = setup_ambiente()
    print("="*60)
    print("🚀 INICIANDO ENGINE MULTI-TAREFAS DO PROMPTTOOLKIT")
    print("="*60)

    for chave_tarefa, dados_tarefa in TAREFAS.items():
        print(f"\n🎯 [TAREFA] -> {dados_tarefa['nome'].upper()}")
        
        # Executa as 4 técnicas para os 5 inputs desta tarefa
        logs_execucao = executar_testes_tecnicas(client, chave_tarefa, dados_tarefa)
        
        # Salva planilhas com métricas individuais
        salvar_csv_e_exibir(chave_tarefa, logs_execucao)
        
        # Juiz avalia de forma dinâmica quem ganhou essa tarefa
        tecnica_vencedora = avaliar_e_escolher_vencedora(client, chave_tarefa, logs_execucao)
        print(f"🏆 Tecnica vencedora para {chave_tarefa}: {tecnica_vencedora.upper()}")
        
        # EXECUÇÃO DO LABORATÓRIO DE TEMPERATURAS NA VENCEDORA
        print(f"🌡️ Disparando Laboratorio de Temperatura na tecnica campea...")
        temperaturas = [0.1, 0.5, 1.0]
        input_teste = logs_execucao[0]["input_texto"] # Pega o primeiro input como caso de teste
        
        prompt_vencedor = montar_prompt(tecnica_vencedora, dados_tarefa, input_teste)
        
        for temp in temperaturas:
            res_temp = enviar_e_medir(client, MODEL_NAME, prompt_vencedor, temperature=temp)
            print(f"    -> Temp {temp} | Tokens: {res_temp['tokens']} | Saida: {res_temp['texto'][:100]}...")

    print("\n🏁 Pipeline executado com sucesso para todas as tarefas!")

if __name__ == "__main__":
    main()
