from banco import carregar_tarefas, salvar_tarefas

def adicionar_tarefa(descricao, prioridade, data_entrega)
    tarefas = carregar_tarefas()

    if tarefas:
        proximo_id = max([tarefa["id"] for tarefa in tarefas]) + 1
    else:
        proximo_id = 1

    nova_tarefa = {
        "id": proximo_id,
        "status": "Pendente",
        "descricao": descricao,
        "prioridade": prioridade,
        "data_entrega": data_entrega
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)