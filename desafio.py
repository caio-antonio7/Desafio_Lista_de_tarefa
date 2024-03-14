import json

def carregar_tarefas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(tarefas, arquivo)

def adicionar_tarefa(tarefas, descricao):
    tarefas.append({'descricao': descricao, 'concluida': False})

def remover_tarefa(tarefas, indice):
    del tarefas[indice]

def atualizar_tarefa(tarefas, indice):
    tarefas[indice]['concluida'] = not tarefas[indice]['concluida']

def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = 'concluída' if tarefa['concluida'] else 'pendente'
            print(f"{i + 1}. [{status}] {tarefa['descricao']}")

def main():
    nome_arquivo = 'tarefas.json'
    tarefas = carregar_tarefas(nome_arquivo)

    while True:
        print("\n=== Lista de Tarefas ===")
        mostrar_tarefas(tarefas)
        print("\n1. Adicionar Tarefa")
        print("2. Atualizar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif escolha == '2':
            indice = int(input("Digite o índice da tarefa para atualizar: ")) - 1
            atualizar_tarefa(tarefas, indice)
        elif escolha == '3':
            indice = int(input("Digite o índice da tarefa para remover: ")) - 1
            remover_tarefa(tarefas, indice)
        elif escolha == '4':
            salvar_tarefas(tarefas, nome_arquivo)
            print("Tarefas salvas. Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

