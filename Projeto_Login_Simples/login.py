import customtkinter as ctk #CTK funciona como um apelido 

# Configuração da pareência
ctk.set_appearance_mode('dark')

#Criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login Simples")
app.geometry("300x300")

#Criação dos campos
#label - Texto acima (Usuário)
campo_usuario = ctk.CTkLabel(app,text="Usuário") #app=paramêtro principal,text= propriedade
campo_usuario.pack(pady=10) #Adiciona a aplicação 

#entry - Entrada de dados
#button - Botão




#Criação das funções de funcionalidade

#Iniciar a aplicação
app.mainloop() 