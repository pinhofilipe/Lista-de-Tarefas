import json

nome_arquivo = "tarefas.json"

def carregar_tarefas():
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
        return tarefas
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)