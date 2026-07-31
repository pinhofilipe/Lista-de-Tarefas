from banco import carregar_tarefas, salvar_tarefas

def adicionar_tarefa(descricao, prioridade, data_entrega):
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

def listar_tarefas(status="Todas"):
    tarefas = carregar_tarefas()

    if status == "Concluída":
        return [tarefa for tarefa in tarefas if tarefa["status"] == "Concluída"]
    elif status == "Pendente":
        return [tarefa for tarefa in tarefas if tarefa["status"] == "Pendente"]
    else: 
        return tarefas

def concluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "Concluída"
    salvar_tarefas(tarefas)

def atualizar_tarefa(id_tarefa, status):
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = status
    salvar_tarefas(tarefas)

def excluir_tarefa(id_tarefa):
    tarefas = carregar_tarefas()
    lista_atualizada = [tarefa for tarefa in tarefas if tarefa["id"] != id_tarefa]
    salvar_tarefas(lista_atualizada)