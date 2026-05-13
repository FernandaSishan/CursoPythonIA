tarefas = ["Implementar login", "Testar API", "Deploy em produção"]

for tarefa in tarefas:
    if tarefa == "Deploy em produção":
        break # Interrompe o loop
    print(f"Concluindo {tarefa}")
else:
    print("Todas as tarefas foram concluídas com sucesso!")