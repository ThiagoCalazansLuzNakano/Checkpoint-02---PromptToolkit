TAREFAS = {
    "classificacao_sentimento": {
        "nome": "classificacao_sentimento",
        "tipo": "classificacao",
        "instrucao": "Classifique o feedback do cliente.",
        "formato_output": "Responda APENAS com uma das opcoes: POSITIVO, NEGATIVO, NEUTRO ou MISTO.",
        "exemplos_fewshot": [
            {"input": "Adorei!", "output": "POSITIVO"},
            {"input": "Pessimo.", "output": "NEGATIVO"}
        ],
        "passos_cot": [
            "Identifique aspectos positivos no texto.",
            "Identifique aspectos negativos ou neutros.",
            "Compare o peso de cada aspecto e defina a classificacao final."
        ],
        "persona_chave": "analista_cx"
    },
    "extracao_dados": {
        "nome": "extracao_dados",
        "tipo": "extracao",
        "instrucao": "Extraia as entidades chaves do relato de defeito.",
        "formato_output": "Formato: produto: <nome>, preco: <valor>, defeito: <problema>.",
        "exemplos_fewshot": [
            {"input": "Fone Sony de R$400 parou de funcionar o lado esquerdo", "output": "produto: Fone Sony, preco: R$400, defeito: parou de funcionar o lado esquerdo"}
        ],
        "passos_cot": [
            "Localize o nome do produto comercial.",
            "Identifique o valor monetario mencionado.",
            "Isole a falha ou reclamacao descrita."
        ],
        "persona_chave": "engenheiro_suporte"
    },
    "geracao_email": {
        "nome": "geracao_email",
        "tipo": "geracao",
        "instrucao": "Escreva um e-mail curto para o cliente com base no contexto fornecido.",
        "formato_output": "Escreva o assunto e o corpo do e-mail de forma concisa.",
        "exemplos_fewshot": [
            {"input": "Cliente quer cancelar plano", "output": "Assunto: Sentimos sua falta! / Corpo: Ola, vimos seu pedido... Oferecemos 20% de desconto para voce ficar."}
        ],
        "passos_cot": [
            "Determine o objetivo central da mensagem.",
            "Adapte o tom de voz a situacao emocional do cliente.",
            "Gere uma chamada para acao limpa e direta."
        ],
        "persona_chave": "copywriter_vendas"
    }
}
