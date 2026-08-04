from tarefas import adicionar_tarefa, excluir_tarefa, listar_tarefas, atualizar_tarefa, editar_prioridade, editar_data, ordenar_por_prioridade, pesquisar_tarefas

def exibir_menu():
    print("=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Excluir tarefa")
    print("3. Listar tarefas")
    print("4. Atualizar status da tarefa")
    print("5. Editar prioridade da tarefa")
    print("6. Editar data de entrega da tarefa")
    print("7. Ordenar tarefas por prioridade")
    print("8. Pesquisar tarefas")
    print("9. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1": #Adicionar Tarefa
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Baixa, Média, Alta): ")
            data_entrega = input("Data de entrega (DD-MM-YYYY): ")
            prioridades_validas = {
                "baixa": "Baixa",
                "media": "Média",
                "média": "Média",
                "alta": "Alta"
            }
            if prioridade.lower() not in prioridades_validas:
                print("Prioridade inválida. Tente novamente.")
                continue
            prioridade = prioridades_validas[prioridade.lower()]
            adicionar_tarefa(descricao, prioridade, data_entrega)
            print("Tarefa adicionada com sucesso!")
        elif opcao == "2": #Excluir Tarefa
            id_tarefa = int(input("ID da tarefa a ser excluída: "))
            excluir_tarefa(id_tarefa)
            print("Tarefa excluída com sucesso!")
        elif opcao == "3": #Listar Tarefas
            for tarefa in listar_tarefas():
                print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}, Data de Entrega: {tarefa['data_entrega']}")
        elif opcao == "4": #Atualizar Status da Tarefa
            id_tarefa = int(input("ID da tarefa a ser atualizada: "))   
            for tarefa in listar_tarefas():
                print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Data de Entrega: {tarefa['data_entrega']}")
            novo_status = input("Novo status (Pendente, Concluída): ").lower()
            status_validos = {
                              "concluida": "Concluída",
                              "concluída": "Concluída",
                              "pendente": "Pendente"
            }
            if novo_status in status_validos:
                atualizar_tarefa(id_tarefa, status_validos[novo_status])
                print("Status da tarefa atualizado com sucesso!")
            else:
                print("Status inválido. Tente novamente.")
        elif opcao == "5": #Editar Prioridade da Tarefa
            id_tarefa = int(input("ID da tarefa a ser editada: "))              
            nova_prioridade = input("Nova prioridade (Baixa, Média, Alta): ")
            prioridades_validas = {
                "baixa": "Baixa",
                "media": "Média",
                "média": "Média",
                "alta": "Alta"
            }
            if nova_prioridade.lower() in prioridades_validas:
                nova_prioridade = prioridades_validas[nova_prioridade.lower()]
                editar_prioridade(id_tarefa, nova_prioridade)
                print("Prioridade da tarefa atualizada com sucesso!")
            else:
                print("Prioridade inválida. Tente novamente.")
            
        elif opcao == "6": #Editar Data de Entrega da Tarefa
            id_tarefa = int(input("ID da tarefa a ser editada: "))
            nova_data = input("Nova data de entrega (DD-MM-YYYY): ")
            editar_data(id_tarefa, nova_data)
            print("Data de entrega da tarefa atualizada com sucesso!")

        elif opcao == "7": #Ordenar Tarefas por Prioridade
            tarefas_ordenadas = ordenar_por_prioridade()
            for tarefa in tarefas_ordenadas:
                print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}, Data de Entrega: {tarefa['data_entrega']}")
        elif opcao == "8": #Pesquisar Tarefas
            termo_pesquisa = input("Termo de pesquisa: ")
            resultados = pesquisar_tarefas(termo_pesquisa)
            for tarefa in resultados:
                print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}, Data de Entrega: {tarefa['data_entrega']}")
        elif opcao == "9":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()