import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3


root = Tk()
root.title("Lista de alunos")
width = 800
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


nome = StringVar()
av1 = StringVar()
av2 = StringVar()
av3 = StringVar()
avd = StringVar()
avds = StringVar()
media = StringVar()
situacao = StringVar()
SEARCH = StringVar()
updateWindow = None
id = None
newWindow = None


def database():
    conn = sqlite3.connect("trabalhoav2/alunos.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'alunoss' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                    nome TEXT,
                                                    av1 FLOAT,
                                                    av2 FLOAT,
                                                    av3 FLOAT,
                                                    avd FLOAT,
                                                    avds FLOAT,
                                                    media FLOAT,
                                                    situacao TEXT)"""
    cursor.execute(query)
    cursor.execute('SELECT * FROM alunoss ORDER BY nome')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def isnumber(value):
    try:
        float(value)
    except ValueError:
        if value == "":
            return False
        return True
    return False


def nota(value):
    if value >= 0 and value <= 10:
        return False
    else:
        return True


def submitData():
    if av1.get() == "":
        av1.set(0)
    if av2.get() == "":
        av2.set(0)
    if av3.get() == "":
        av3.set(0)
    if avd.get() == "":
        avd.set(0)
    if avds.get() == "":
        avds.set(0)
    if nome.get() == "":
        resultado = msb.showwarning("", "Por favor, digite o nome do aluno.", icon="warning")
    elif isnumber(av1.get()) or isnumber(av2.get()) or isnumber(av3.get()) or isnumber(avd.get()) or isnumber(avds.get()):
        resultado = msb.showwarning("", "ERRO, digite numeros.", icon="warning")
    elif nota(float(av1.get())) or nota(float(av2.get())) or nota(float(av3.get())) or nota(float(avd.get())) or nota(float(avds.get())):
        resultado = msb.showwarning("", "ERRO, digite notas de 0 a 10.", icon="warning")
    else:
        media = 0
        situacao = ""
        if avd.get() not in "0.0" or avds.get() not in "0.0":
            if av1.get() not in "0.0" and av2.get() not in "0.0" or av1.get() not in "0.0" and av3.get() not in "0.0" or av2.get() not in "0.0" and av3.get() not in "0.0":
                n1 = n2 = n3 = 0
                notas = [float(av1.get()), float(av2.get()), float(av3.get())]
                notas.sort()
                n1 = notas[2]
                n2 = notas[1]
                notas2 = [float(avd.get()), float(avds.get())]
                n3 = max(notas2)
                media = (n1+n2+n3) / 3
                situacao = "Recuperação"
                if media < 6:
                    situacao = "Reprovado"
                    if float(avds.get()) == 0:
                        situacao = "Recuperação"
                if float(avd.get()) < 4 and float(avds.get()) < 4:
                    situacao = "Reprovado"
                    if float(avds.get()) == 0:
                                situacao = "Recuperação"
                if n1 >= 4 and n2 >= 4 and n3 >= 4 and media >= 6:
                    situacao = "Aprovado"
                if float(av1.get()) >= 4 or float(av2.get()) >= 4 :
                    if float(av3.get()) == 0 and media < 6:
                        situacao = "Recuperação"
                        if float(avd.get()) < 4 and float(avds.get()) < 4:
                            situacao = "Reprovado"
                            if float(avds.get()) == 0:
                                situacao = "Recuperação"
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("trabalhoav2/alunos.db")
        cursor = conn.cursor()
        query = """ INSERT INTO 'alunoss' (nome, av1, av2, av3, avd, avds, media, situacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get().strip().capitalize()), str(av1.get()), str(av2.get()), str(av3.get()),
                             str(avd.get()), str(avds.get()), float("%.1f"%media), str(situacao)))
        conn.commit()
        cursor.execute('SELECT * FROM alunoss ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")


def updateData():
    if av1.get() == "":
        av1.set(0)
    if av2.get() == "":
        av2.set(0)
    if av3.get() == "":
        av3.set(0)
    if avd.get() == "":
        avd.set(0)
    if avds.get() == "":
        avds.set(0)
    if nome.get() == "":
        resultado = msb.showwarning("", "Por favor, digite o nome do aluno.", icon="warning")
    elif isnumber(av1.get()) or isnumber(av2.get()) or isnumber(av3.get()) or isnumber(avd.get()) or isnumber(avds.get()):
        resultado = msb.showwarning("", "ERRO, digite numeros.", icon="warning")
    elif nota(float(av1.get())) or nota(float(av2.get())) or nota(float(av3.get())) or nota(float(avd.get())) or nota(float(avds.get())):
        resultado = msb.showwarning("", "ERRO, digite notas de 0 a 10.", icon="warning")
    else:
        media = 0
        situacao = ""
        if avd.get() not in "0.0" or avds.get() not in "0.0":
            if av1.get() not in "0.0" and av2.get() not in "0.0" or av1.get() not in "0.0" and av3.get() not in "0.0" or av2.get() not in "0.0" and av3.get() not in "0.0":
                n1 = n2 = n3 = 0
                notas = [float(av1.get()), float(av2.get()), float(av3.get())]
                notas.sort()
                n1 = notas[2]
                n2 = notas[1]
                notas2 = [float(avd.get()), float(avds.get())]
                n3 = max(notas2)
                media = (n1+n2+n3) / 3
                situacao = "Recuperação"
                if media < 6:
                    situacao = "Reprovado"
                    if float(avds.get()) == 0:
                        situacao = "Recuperação"
                if float(avd.get()) < 4 and float(avds.get()) < 4:
                    situacao = "Reprovado"
                    if float(avds.get()) == 0:
                                situacao = "Recuperação"
                if n1 >= 4 and n2 >= 4 and n3 >= 4 and media >= 6:
                    situacao = "Aprovado"
                if float(av1.get()) >= 4 or float(av2.get()) >= 4 :
                    if float(av3.get()) == 0 and media < 6:
                        situacao = "Recuperação"
                        if float(avd.get()) < 4 and float(avds.get()) < 4:
                            situacao = "Reprovado"
                            if float(avds.get()) == 0:
                                situacao = "Recuperação"
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("trabalhoav2/alunos.db")
        cursor = conn.cursor()
        query = """ UPDATE 'alunoss' SET nome = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, avds = ?, media = ?, situacao = ? WHERE id = ?"""
        cursor.execute(query, (str(nome.get().strip().capitalize()), str(av1.get()), str(av2.get()), str(av3.get()),
                            str(avd.get()), str(avds.get()), float("%.1f"%media), str(situacao), int(id)))
        conn.commit()
        cursor.execute('SELECT * FROM alunoss ORDER BY nome')
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        updateWindow.destroy()


def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo["values"]
    id = selectedItem[0]
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    nome.set(selectedItem[1])
    av1.set(selectedItem[2])
    av2.set(selectedItem[3])
    av3.set(selectedItem[4])
    avd.set(selectedItem[5])
    avds.set(selectedItem[6])

    
    updateWindow = Toplevel()
    updateWindow.title("ATUALIZAR")
    width = 480
    heigth = 200
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    
    formTitle = Frame(updateWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(updateWindow)
    formContact.pack(side = TOP, pady = 10)
    

    lbl_title = Label(formTitle, text="Atualizar", font=('arial', 18), width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(formContact, text="Av1", font=('arial', 12))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2 = Label(formContact, text="Av2", font=('arial', 12))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(formContact, text="Av3", font=('arial', 12))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(formContact, text="Avd", font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(formContact, text="Avds", font=('arial', 12))
    lbl_avds.grid(row=5, sticky=W)

    
    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    av1Entry = Entry(formContact, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=1, column=1)
    av2Entry = Entry(formContact, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=2, column=1)
    av3Entry = Entry(formContact, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=3, column=1)
    avdEntry = Entry(formContact, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    avdsEntry = Entry(formContact, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=5, column=1)
    
    
    bttn_update = Button(formContact, text="Atualizar", width=50, command=updateData)
    bttn_update.grid(row=6, columnspan=2, pady=10)


def deletarData():
    if not tree.selection():
        resultado = msb.showwarning("", "Por favor, selecione um aluno.", icon="warning")
    else:
        resultado = msb.askquestion("", "Tem certeza que deseja deletar?")
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("trabalhoav2/alunos.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'alunoss' WHERE id = %d" % selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def inserirData():
    global newWindow
    nome.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")

    
    newWindow = Toplevel()
    newWindow.title("INSERINDO ALUNO")
    width = 480
    heigth = 200
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    
    formTitle = Frame(newWindow)
    formTitle.pack(side=TOP)
    formContact = Frame(newWindow)
    formContact.pack(side=TOP, pady=10)
    
    
    lbl_title = Label(formTitle, text="Inserindo aluno",
                      font=('arial', 18), width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text="Nome", font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_av1 = Label(formContact, text="Av1", font=('arial', 12))
    lbl_av1.grid(row=1, sticky=W)
    lbl_av2 = Label(formContact, text="Av2", font=('arial', 12))
    lbl_av2.grid(row=2, sticky=W)
    lbl_av3 = Label(formContact, text="Av3", font=('arial', 12))
    lbl_av3.grid(row=3, sticky=W)
    lbl_avd = Label(formContact, text="Avd", font=('arial', 12))
    lbl_avd.grid(row=4, sticky=W)
    lbl_avds = Label(formContact, text="Avds", font=('arial', 12))
    lbl_avds.grid(row=5, sticky=W)

    
    nomeEntry = Entry(formContact, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    av1Entry = Entry(formContact, textvariable=av1, font=('arial', 12))
    av1Entry.grid(row=1, column=1)
    av2Entry = Entry(formContact, textvariable=av2, font=('arial', 12))
    av2Entry.grid(row=2, column=1)
    av3Entry = Entry(formContact, textvariable=av3, font=('arial', 12))
    av3Entry.grid(row=3, column=1)
    avdEntry = Entry(formContact, textvariable=avd, font=('arial', 12))
    avdEntry.grid(row=4, column=1)
    avdsEntry = Entry(formContact, textvariable=avds, font=('arial', 12))
    avdsEntry.grid(row=5, column=1)


    bttn_inserir = Button(formContact, text="Inserir",
                        width=50, command=submitData)
    bttn_inserir.grid(row=6, columnspan=2, pady=10)


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("trabalhoav2/alunos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `alunoss` WHERE `nome` LIKE ? OR `media` LIKE ?",
                       ('%'+str(SEARCH.get())+'%', '%'+str(SEARCH.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    conn = sqlite3.connect("trabalhoav2/alunos.db")
    cursor = conn.cursor()
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM `alunoss` ORDER BY `nome` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    SEARCH.set("")


top = Frame(root, width=500, bd=1,relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500)
mid.pack(side=TOP)
midLeft = Frame(mid, width=100)
midLeft.pack(side=LEFT)
midLeftPadding = Frame(mid, width=350)
midLeftPadding.pack(side=LEFT)
midRight = Frame(mid, width=100)
midRight.pack(side=RIGHT)
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargim = Frame(root, width=500)
tableMargim.pack(side=TOP)


lbl_title = Label(top, text="SISTEMA DE CADASTRO DE NOTAS DE ALUNOS", font=('arial', 20), width=500)
lbl_title.pack(fill=X)


lbl_alt = Label(bottom, text="Clique duas vezes para atualizar", font=('arial', 15), width=250)
lbl_alt.pack(fill=X)


search = Entry(midLeftPadding, textvariable=SEARCH)
search.pack(side=LEFT)


btn_search = Button(midLeftPadding, text="Pesquisar", command=Search)
btn_search.pack(side=LEFT)
btn_clean = Button(midLeftPadding, text="Limpar", command=Reset)
btn_clean.pack(side=LEFT)


bttn_add = Button(midLeft, text="Inserir", command=inserirData)
bttn_add.pack()
bttn_del = Button(midRight, text="Deletar", command=deletarData)
bttn_del.pack(side=RIGHT)


scrollbarX = Scrollbar(tableMargim, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargim, orient=VERTICAL)


tree = ttk.Treeview(tableMargim, columns=("ID", "Nome", "Av1", "Av2", "Av3", "Avd", "Avds", "Media", "Situação"), height=400, 
                    selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Av1", text="Av1", anchor=W)
tree.heading("Av2", text="Av2", anchor=W)
tree.heading("Av3", text="Av3", anchor=W)
tree.heading("Avd", text="Avd", anchor=W)
tree.heading("Avds", text="Avds", anchor=W)
tree.heading("Media", text="Media", anchor=W)
tree.heading("Situação", text="Situação", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=90)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=100)
tree.column('#6', stretch=NO, minwidth=0, width=90)
tree.column('#7', stretch=NO, minwidth=0, width=100)
tree.column('#8', stretch=NO, minwidth=0, width=100)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)


if __name__ == '__main__':
    database()
    root.mainloop()
