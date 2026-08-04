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

def editar_prioridade(id_tarefa, nova_prioridade):
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["prioridade"] = nova_prioridade
    salvar_tarefas(tarefas)

def editar_data(id_tarefa, nova_data):
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["data_entrega"] = nova_data
    salvar_tarefas(tarefas)

def ordenar_por_prioridade():
    tarefas = carregar_tarefas()
    ordem_prioridade = {"Alta": 1, "Média": 2, "Baixa": 3}
    tarefas_ordenadas = sorted(tarefas, key=lambda x: ordem_prioridade.get(x["prioridade"], 4))
    return tarefas_ordenadas

def pesquisar_tarefas(termo_pesquisa):
    tarefas = carregar_tarefas()
    resultados = [tarefa for tarefa in tarefas if termo_pesquisa.lower() in tarefa["descricao"].lower()]
    return resultados