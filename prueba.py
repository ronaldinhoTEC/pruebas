from tkinter import *

root = Tk()
#raiz.title('Mi app')
#raiz.geometry('330x200')
#raiz.config(bg='black')

#mi_frame= Frame()
#mi_frame.pack(fill='both', expand='True')
#mi_frame.config(bg='gold')
#mi_frame.config(width='450', height='250')
#mi_frame.config(relief='groove')

mi_frame= Frame(root, width=500, height=400)
mi_frame.pack()

nombre = input('Ingresa tu nombre por favor: \n')

frase= f'Hola {nombre} como estas maquinola'
nombres=['Ronal','Gabriel','Milagros','Cristina','Marcela']
for i in nombres:
    if nombre==i:
        Label(mi_frame, text=frase).place(x=10, y=10)
        print(frase)
        break
    else:
        print(f'{nombre} no esta registrado en nuestra base de datos \n'
              f'Logueate en nuestra base de datos')
        break


root.mainloop()


