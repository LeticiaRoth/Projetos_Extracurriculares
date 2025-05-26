from operator import truediv

import customtkinter as ctk

ctk.set_appearance_mode('dark')

ARQUIVO_USUARIOS = 'usuarios.txt'


def salvar_usuario(usuario, senha):
    if usuario and senha:
        with open(ARQUIVO_USUARIOS, 'a') as f: #Adicionar o usuário e a senha, no arquivo com o a
            f.write(f'{usuario},{senha}\n') #Escreve usuario e senha e pla linha
        return True
    return False


def validar_login(usuario,senha): #Cria os parâmetros
    try: #Tratará o erro quando for abrir o arquivo para leitura
        with open(ARQUIVO_USUARIOS, 'r') as f: #Estou lendo as linhas do arquivo
            usuarios = f.readlines()
    except FileNotFoundError: #Se ainda não existir dará essa mensagem
        return False

    for linha in usuarios: #Formatação básica do txt
        user, pwd = linha.strip().split(',') #Remove os espaços e separa com vírgula
        if user == usuario and pwd == senha: #Verifico se a senha cadastrada é a mesma do login
            return True
    return False

"""
Anotações de estudo
-> INIT = inicializará a classe, quando criamos um objeto
-> SELF = vai acessar os atributos e métodos que eu passei, como digitar nos campos

"""



class JanelaRegistrar(ctk.CTk): #Subclasse de ctk,CTk vai receber os atributos
    def __init__(self): #Vai rodar e guardar todos que tem o self
        super().__init__() #Pegará os padrões colocados no ctk,CTk

        self.title("Registrar Usuário")
        self.geometry("400x300")

        self.label_usuario = ctk.CTkLabel(self, text="Novo Usuário - Bem Vindo") #Título da tela
        self.label_usuario.pack(pady=10)

        self.campo_usuario = ctk.CTkEntry(self, placeholder_text="Digite seu usuário")
        self.campo_usuario.pack(pady=5)

        self.label_senha = ctk.CTkLabel(self, text="Nova Senha")
        self.label_senha.pack(pady=10)

        self.campo_senha = ctk.CTkEntry(self, placeholder_text="Digite sua senha", show="*")
        self.campo_senha.pack(pady=5)

        self.label_resultado = ctk.CTkLabel(self, text="")
        self.label_resultado.pack(pady=10)

        self.botao_registrar = ctk.CTkButton(self, text="Registrar", command=self.registrar_usuario)
        self.botao_registrar.pack(pady=10)


#Mensagens para caso de erro
    def registrar_usuario(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        if usuario and senha: #Se tiver preenchido cai na condição
            if salvar_usuario(usuario, senha):
                self.label_resultado.configure(text="Usuário registrado com sucesso!", text_color="green")
                self.after(1500, self.abrir_login)
            else:
                self.label_resultado.configure(text="Erro ao registrar usuário.", text_color="red")
        else:
            self.label_resultado.configure(text="Preencha usuário e senha!", text_color="red")



#Destroi a tela de registro, para rodar com o mainloop a tela de login
    def abrir_login(self):
        self.destroy()
        login = JanelaLogar()
        login.mainloop()


#Janela do login usando orientação a objeto
class JanelaLogar(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x300")

        self.label_usuario = ctk.CTkLabel(self, text="Usuário")
        self.label_usuario.pack(pady=10)

        self.campo_usuario = ctk.CTkEntry(self, placeholder_text="Digite seu usuário")
        self.campo_usuario.pack(pady=5)

        self.label_senha = ctk.CTkLabel(self, text="Senha")
        self.label_senha.pack(pady=10)

        self.campo_senha = ctk.CTkEntry(self, placeholder_text="Digite sua senha", show="*")
        self.campo_senha.pack(pady=5)

        self.label_resultado = ctk.CTkLabel(self, text="")
        self.label_resultado.pack(pady=10)

        self.botao_login = ctk.CTkButton(self, text="Login", command=self.fazer_login)
        self.botao_login.pack(pady=10)

    def fazer_login(self):
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        if validar_login(usuario, senha):
            self.label_resultado.configure(text="Login realizado com sucesso!", text_color="green")
        else:
            self.label_resultado.configure(text="Usuário ou senha incorretos.", text_color="red")

#Para executar a tela de registro antes do login
if __name__ == "__main__": #Para executar o resgistrotro, name é o nome do arquivo atual
    registro = JanelaRegistrar()
    registro.mainloop()
