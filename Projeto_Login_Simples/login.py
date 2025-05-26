import customtkinter as ctk #CTK funciona como um apelido 

# Configuração da pareência
ctk.set_appearance_mode('dark')

#Criação das funções de funcionalidade
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #Verificação da senha, se o nome é Leticia e a senha 280813
    if usuario == 'Leticia' and senha == '280813':
        resultado_login.configure(text='Login realizado com sucesso', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')


#Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("400x300")

#Criação dos campos
#label - Texto acima (Usuário)
label_usuario = ctk.CTkLabel(app, text="Usuário") #app=paramêtro principal,text= propriedade
label_usuario.pack(pady=10) #Adiciona a aplicação

#entry - Entrada de dados
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário:')
campo_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)


campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha:', show='*')
campo_senha.pack(pady=5)


#button - Botão
botao_login = ctk.CTkButton(app, text='Login', command=validar_login)
botao_login.pack(pady=10)

#Campo de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

#Iniciar a aplicação
app.mainloop() 