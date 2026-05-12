senha_correta = "1234"
tentativas = 0

while tentativas < 3:
    senha = input("Digite uma senha: ")
    if senha == senha_correta:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
        tentativas += 1

else:
# Este bloco executa se o while terminar sem o "break"
    print("Número máximo de tentativas excedido. Conta bloqueada")

