from tkinter import *
from tkinter import ttk
import awesometkinter as atk
from paises import list_pais
from tkinter import messagebox
from classe_user import User
from dao import *
from verif_user import senha_ver, email_ver
from criptografia import criptografar, verificar_hash


#----------------------FUNÇÕES DE MOSTRAR SENHA----------------------------------+#
def show_password():                                                            #|
    btn_sh_pass.config(image=hidde_p, bg='#2a1e8a'  ,command=hidde_password)    #|
    ipt_senha.config(show='')                                                   #|
    ipt_re_senha.config(show='')                                                #|
def hidde_password():                                                           #|
    btn_sh_pass.config(command=show_password, image=show_p, bg='#fff')          #|
    ipt_senha.config(show='*')                                                  #|
    ipt_re_senha.config(show='*')                                               #|
#--------------------------------------------------------------------------------+#

#--------------------------FUNÇÕES DE DESABILITA----------------------------------+#
def desabilitar():
    """
        Desabilita todos os campos necessários da tela 
    """
    ipt_nome.config(state='disabled')
    ipt_email.config(state='disabled')
    ipt_num.config(state='disabled')
    ipt_pais['state'] = 'disabled'
    var_gen.set(0)
    r1.config(state='disabled')
    r2.config(state='disabled')
    r3.config(state='disabled')
    ipt_senha.config(state='disabled')
    ipt_re_senha.config(state='disabled')

    btn_sh_pass.config(state='disabled', cursor='arrow')
    btn_canc.config(state='disabled',cursor='arrow')
    btn_salvar.config(state='disabled',cursor='arrow')
    btn_remove.config(state='disabled',cursor='arrow')

#--------------------------FUNÇÕES DE HABILITAR----------------------------------+#
def habilitar():
    ipt_nome.config(state='normal')
    ipt_email.config(state='normal')
    ipt_num.config(state='normal')
    ipt_pais['state'] = 'normal'
    r1.config(state='normal')
    r2.config(state='normal')
    r3.config(state='normal')
    ipt_senha.config(state='normal')
    ipt_re_senha.config(state='normal')

    btn_sh_pass.config(state='normal', cursor='hand2')
    btn_canc.config(state='normal',cursor='hand2')
    btn_salvar.config(state='normal',cursor='hand2')
    btn_remove.config(state='normal',cursor='hand2')

#--------------------------FUNÇÃO DE CANCELAR/LIMPAR----------------------------------+#
def cancel():
    var_nome.set('')
    var_email.set('')
    var_num.set('')
    var_gen.set(None)
    ipt_pais.set('')
    var_senha.set('')
    var_re_senha.set('')
    desabilitar()
#----------------------------FUNÇÕES DE SAIR--------------------------------------+#
def sair():                                                                      
    if messagebox.askyesno('Encerrar', 'Tem certeza??'):                         
        window.destroy()                                                        

#----------------------------FUNÇÕES DE CADASTRAR--------------------------------------+#
user = User()
def salvar():
    try:
        if var_nome.get() != '' and var_email.get() != '' and var_num.get() != '' and var_senha.get() !='' and var_senha.get() == var_re_senha.get() and var_pais.get() != '':
            hash_user = criptografar(var_senha.get())
        
            user.nome = var_nome.get()
            user.email = var_email.get()
            user.num = var_num.get()
            user.senha = hash_user
            user.pais = var_pais.get()
            if var_gen.get() == 1:
                user.gen = 'Masculino'
            elif var_gen.get() == 2:
                user.gen = 'Feminino'
            else:
                user.gen = 'Outro'
            
            if email_ver(var_email.get()) == True:
                if messagebox.askokcancel('Atualizar','Tem certeza que deseja atualizar o usuário?'):
                    atualizar(user)
                    messagebox.showinfo('Sucesso','Usuário atualizado com sucesso!')
            else:
                inserir(user)
                messagebox.showinfo('Sucesso', 'Cadastrado com sucesso!')
        else:
            if var_senha.get() != var_re_senha.get():
                messagebox.showwarning('Alerta', 'Senhas não compativeis!')
    except:
        messagebox.showerror('Atenção', 'Erro inesperado!')

#----------------------------FUNÇÕES DE EXCLUIR--------------------------------------+#
def remover() -> None:
    try:
        if var_senha.get() != '' and var_re_senha.get() != '' and var_senha.get() == var_re_senha.get():
            if verificar_hash(var_senha.get(), senha_ver(var_email.get())):
                if messagebox.askokcancel('Alerta', 'Deseja excluir este usuário??'):
                        excluir(var_email.get())
                        cancel()
            else:
                messagebox.showinfo('Alerta', 'Senha incorreta!')
        else:
            messagebox.showinfo('Alerta', 'Senha não informada!')
    except:
        messagebox.showerror('Alerta', 'Error inesperado')

def buscar(event=None):
    try:
        if email_ver(var_email.get()) == True:
            if var_senha.get() != '' and var_re_senha.get() != '':
                if var_senha.get() == var_re_senha.get():
                    if verificar_hash(var_senha.get(), senha_ver(var_email.get())):
                        print(senha_ver(var_email.get()))
                        lista = listar_bd(var_email.get())
                        var_nome.set(lista[0])
                        var_email.set(lista[1])
                        var_num.set(lista[3])
                        if lista[4] == 'Masculino':
                            r1.select()
                        elif lista[4] == 'Feminino':
                            r2.select()
                        else:
                            r3.select()
                        var_pais.set(lista[5])
                        btn_sh_pass.config(state='disabled')
                    else:
                        messagebox.showerror('Importante', 'Senha incorreta!')
                else:
                    messagebox.showinfo('Alerta', 'As senhas não correspondem!')
            else:
                if var_senha.get() == '':
                    messagebox.showinfo('Alerta', 'Senha não informada!')
                else:
                    messagebox.showinfo('Alerta', 'Confirme a senha')
        else:
            messagebox.showinfo('Alerta', 'Este email não esta cadastrado!')

    except:
        messagebox.showerror('Alerta', 'Error inesperado')

def login():
    window.destroy()
    janela = Tk()
    janela.mainloop()


window = Tk()
window.geometry('750x420')
window.resizable(False,False)
window.config(bg="#2a1e8a")
window.title('Cadastro Usuario')
#-------------------BG IMAGE-----------------------------#
bg_image = PhotoImage(file='img/bg_google.png')
fig1 = Label(image=bg_image, bg='#2a1e8a')
fig1.place(x=0,y=0)

#--------------------FRAME-------------------------------#
frame = atk.Frame3d(window, width=395, height=370, bg='white')
frame.place(x=340,y=20)

#-------------------IMAGE SHOW PASSWORD-----------------------------#
show_p = PhotoImage(file='img/sh_senha.png', master=frame)
show_p = show_p.subsample(2,2)

#-------------------IMAGE HIDDEN PASSWORD-----------------------------#
hidde_p = PhotoImage(file='img/hd_senha.png', master=frame)
hidde_p = hidde_p.subsample(2,2)

#-------------------IMAGE SEARCH BUTTON-----------------------------#
search = PhotoImage(file='img/loupe.png', master=frame)
search = search.subsample(2,2)

#--------------------NOME-------------------------------#
var_nome = StringVar(window)
lbl_nome = Label(frame, text='Nome',bg='#fff', fg='#2a1e8a', font='suse 8 bold').place(x=30,y=40)
ipt_nome = Entry(frame, textvariable=var_nome, width=38, fg='#2a1e8a')
ipt_nome.place(x=130,y=40)

#--------------------EMAIL-------------------------------#
var_email = StringVar(window)
lbl_email = Label(frame, text='Email',bg='#fff', fg='#2a1e8a', font='suse 8 bold').place(x=30,y=75)
ipt_email = Entry(frame, textvariable=var_email,width=34, fg='#2a1e8a')
ipt_email.bind('<Return>', buscar)
ipt_email.place(x=130,y=75)

#--------------------N° CONTATO-------------------------------#
var_num = StringVar(window)
lbl_num = Label(frame, text='Número',bg='#fff', fg='#2a1e8a', font='suse 8 bold').place(x=30,y=110)
ipt_num = Entry(frame, textvariable=var_num,width=38, fg='#2a1e8a')
ipt_num.place(x=130,y=110)

#--------------------GENERO-------------------------------#
var_gen = IntVar(window)
lbl_gen = Label(frame, text='Gênero',bg='#fff',fg='#2a1e8a', font='suse 8 bold').place(x=30,y=145)
r1 = Radiobutton(frame, text='Masculino', value=1, variable=var_gen, bg='#fff',fg='#2a1e8a',activebackground='#fff', activeforeground='#2a1e8a', cursor='hand2', font='suse 8 bold')
r1.place(x=125, y=145)
r2 = Radiobutton(frame, text='Feminino', value=2, variable=var_gen, bg='#fff',fg='#2a1e8a',activebackground='#fff', activeforeground='#2a1e8a',cursor='hand2', font='suse 8 bold')
r2.place(x=218, y=145)
r3 = Radiobutton(frame, text='Outro', value=3, variable=var_gen, bg='#fff',fg='#2a1e8a', activebackground='#fff', activeforeground='#2a1e8a',cursor='hand2', font='suse 8 bold')
r3.place(x=307, y=145)

#--------------------PAÍS-------------------------------
var_pais = StringVar(window)
lbl_pais = Label(frame, text='País', bg='#fff',fg='#2a1e8a', font='suse 8 bold').place(x=30,y=180)
ipt_pais = ttk.Combobox(frame,textvariable=var_pais,width=35, font='suse 8 bold',foreground='#2a1e8a')
ipt_pais['values'] = list_pais
ipt_pais.place(x=130,y=180)

#--------------------SENHA-------------------------------#
var_senha = StringVar(window)
lbl_senha = Label(frame, text='Senha',bg='#fff',fg='#2a1e8a',font='suse 8 bold').place(x=30,y=215)
ipt_senha = Entry(frame,textvariable=var_senha, show='*',width=34, fg='#2a1e8a')
ipt_senha.place(x=130,y=215)

#--------------------CONFIRMAÇÃO SENHA-------------------------------#
var_re_senha = StringVar(window)
lbl_re_senha = Label(frame, text='Confirmar Senha',bg='#fff',fg='#2a1e8a', font='suse 8 bold').place(x=30,y=250)
ipt_re_senha = Entry(frame,textvariable=var_re_senha, show='*',width=38, fg='#2a1e8a')
ipt_re_senha.place(x=130,y=250)

#--------------------BTN NOVO-------------------------------#
btn_novo = Button(text='Novo', width=8, cursor='hand2',font='suse 8 bold', bg='#2a1e8a', fg='#fff', command=habilitar)
btn_novo.place(x=360,y=320)

#--------------------BTN CANCEL-------------------------------#
btn_canc = Button(text='Cancelar', width=8, cursor='hand2',font='suse 8 bold', bg='#2a1e8a', fg='#fff', command=cancel)
btn_canc.place(x=432,y=320)

#--------------------BTN SALVAR-------------------------------#
btn_salvar = Button(text='Salvar', width=8, cursor='hand2',font='suse 8 bold', bg='#2a1e8a', fg='#fff', command=salvar)
btn_salvar.place(x=505,y=320)

#--------------------BTN REMOVER-------------------------------#
btn_remove = Button(text='Remover', width=8, cursor='hand2',font='suse 8 bold', bg='#2a1e8a', fg='#fff', command=remover)
btn_remove.place(x=577,y=320)

#--------------------BTN SAIR-------------------------------#
btn_sair = Button(text='Sair', width=8,cursor='hand2',font='suse 8 bold', bg='#2a1e8a', fg='#fff', command=sair)
btn_sair.place(x=650,y=320)

#--------------------BTN MOSTRAR SENHA----------------------#
btn_sh_pass = Button(frame, image=show_p, bg='#fff', cursor='hand2', command=show_password, width=14, height=14)
btn_sh_pass.place(x=346, y=215)

#--------------------BTN BUSCAR USER----------------------#
btn_buscar = Button(frame, image=search, bg='#fff', cursor='hand2', width=14, height=14, command=buscar)
btn_buscar.place(x=346, y=75)

# btn_login= Button(window, command=login).place(x=20,y=30)


#--------------CHAMADA DA FUNÇÃO DESABILTA-----------------#
desabilitar()


window.mainloop()

