# Task Manager

## Sobre o projeto 

O Task Manager é uma aplicação desenvolvida em Python para gerenciamento de tarefas através do terminal.

O projeto foi criado com o objetivo de praticar conceitos fundamentais da linguagem, como modularização, manipulação de arquivos JSON e organização de código.

## Funcionalidades
- Adicionar/Remover Tarefas
- Definir/editar prioridade de tarefas
- Adicionar data de entrega
- Listar tarefas (com possibilidade de filtrar por status)
- Ordenar tarefas por prioridade
- Pesquisar tarefa por palavra chave

## Tecnologias usadas
- Python
- JSON
- Git
- GitHub

## Como executar
1. Clone o repositório:
```bash
   git clone https://github.com/pinhofilipe/Lista-de-Tarefas
```

2. Entre na pasta do projeto:
```bash
   cd Lista-de-Tarefas
```

3. Execute o programa:
```bash
   python main.py
```

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação, responsável por interpretar os comandos digitados pelo usuário no terminal e acionar a função correspondente
- `tarefas.py`: contém a lógica principal do programa, incluindo as regras para adicionar, remover, editar e organizar as tarefas
- `banco.py`: camada responsável pela persistência dos dados, cuidando da leitura e escrita do arquivo `tarefas.json`
- `utils.py`: reúne funções auxiliares de validação e formatação, usadas pelos demais módulos
- `tarefas.json`: arquivo onde as tarefas são armazenadas em formato JSON