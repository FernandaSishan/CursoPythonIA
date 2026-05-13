lições = ["Conceitos de Python", "Estrutura de dados", "Loops", "Funções"]

for lição in lições:
    if lição == "Loops":
        continue #Pula a lição de Loops
    print(f"Estudando: {lição}")