import csv

def urna_eletronica():
    candidatos = {'1': 'Candidato A', '2': 'Candidato B', '3': 'Candidato C', '0': 'Voto em Branco', 'N': 'Voto Nulo'}
    votos = {'Candidato A': 0, 'Candidato B': 0, 'Candidato C': 0, 'Voto em Branco': 0, 'Voto Nulo': 0}

    for i in range(1, 11):
        print(f"\nVoto {i}")
        print("Opções:")
        for opcao, candidato in candidatos.items():
            print(f"{opcao}: {candidato}")

        voto = input("Selecione o numero correspondente ao candidato (ou 0 para branco, N para nulo): ").upper()

        if voto in candidatos:
            votos[candidatos[voto]] += 1
            print(f"Voto registrado para {candidatos[voto]}.\n")
        else:
            print("Opção inválida. Voto nulo registrado.\n")
            votos['Voto Nulo'] += 1

 
    with open('resultados_eleicao.csv', 'w', newline='') as csvfile:
        fieldnames = ['Candidato', 'Votos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for candidato, voto in votos.items():
            writer.writerow({'Candidato': candidato, 'Votos': voto})

    print("\nResultado da eleição registrado em 'resultados_eleicao.csv'.")

if __name__ == "__main__":
    urna_eletronica()
