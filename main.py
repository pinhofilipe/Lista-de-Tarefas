from tarefas import adicionar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa

def exibir_menu():
    print("=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar status da tarefa")
    print("4. Excluir tarefa")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            prioridade = input("Prioridade (Baixa, Média, Alta): ")
            data_entrega = input("Data de entrega (DD-MM-YYYY): ")
            adicionar_tarefa(descricao, prioridade, data_entrega)
            print("Tarefa adicionada com sucesso!")
        elif opcao == "2":
            for tarefa in listar_tarefas():
                print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}, Data de Entrega: {tarefa['data_entrega']}")
        elif opcao == "3":
            id_tarefa = int(input("ID da tarefa a ser atualizada: "))   
            listar_tarefas() # Listar tarefas antes de atualizar    
            novo_status = input("Novo status (Pendente, Concluída): ").lower()
            status_validos = {
                              "concluida": "Concluída",
                              "concluída": "Concluída",
                              "pendente": "Pendente"
            }
            if novo_status in status_validos:
                atualizar_tarefa(id_tarefa, novo_status)
            else:
                print("Status inválido. Tente novamente.")
        elif opcao == "4":
            id_tarefa = int(input("ID da tarefa a ser excluída: "))
            excluir_tarefa(id_tarefa)
        elif opcao == "5":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()