user_login = str(input("Digite o nome de usuário: ")).capitalize().strip()
senha_login = int(input("Digite a senha: "))

user_login = "Admin"
senha_login = 1234

if user_login == "Admin" and senha_login == 1234:
    print("Login bem-sucedido!")
else:
    print("Login falhou. Verifique seu nome de usuário e senha.")