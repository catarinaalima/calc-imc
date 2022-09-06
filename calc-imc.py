# Cálculo de IMC com TKinter.

from distutils.cmd import Command
from tkinter import *

# Criar variavel para identificar a janela.
root = Tk()
class imc():
    def __init__(self):
        self.root  = root
        self.janela()
        self.desenho()

        # Criando o loop.
        root.mainloop()
    def janela(self):
        self.root.title('Calculadora de Indice de Massa Corporal.')
        self.root.configure(background='#293259')
        self.root.geometry('500x500')
        self.root.resizable(True,True)
    def desenho(self):
        self.quilos = DoubleVar()
        self.lb_quilos = Label(text='Peso(em Kg)',font=('Verdana','10','bold'),
                                                    bg='#D3D3D3',fg='#000000')
        self.lb_quilos.place(relx=0.2, rely=0.05, relwidth=0.35,relheight=0.1)
        self.input_quilos = Entry(textvariable=self.quilos)
        self.input_quilos.place(relx=0.6, rely=0.05, relwidth=0.2,relheight=0.1)

        self.altura = DoubleVar()
        self.lb_altura = Label(text='Altura (em metros',font=('Verdana','10','bold'),
                                                    bg='#D3D3D3',fg='#000000')
        self.lb_altura.place(relx=0.2, rely=0.2,relwidth=0.35, relheight=0.1)
        self.input_altura = Entry(textvariable=self.altura)
        self.input_altura.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.1)

        self.bt_calcular = Button(text='Calcular o IMC',bg='#000000',fg='#f8f8ff',font=('Verdana',13, 'bold'),
                                                command=self.butaoclick1)
        self.bt_calcular.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.12)


        # Resultado
        self.imcfinal=StringVar()
        self.imcfinal1 = Label(textvariable=self.imcfinal)

        self.resultado1 = Label(textvariable=self.imcfinal)
        self.resultado1.place(relx=0.1, rely=0.65, relwidth=0.8,relheight=0.1)


    def butaoclick1(self):
        peso = self.quilos.get()
        altura = self.altura.get()
        
        altura2=altura*altura
        imc = peso/altura2
        imcArredondado = round(imc,2)

        if imc < 16:
            final = 'O seu IMC é de ' +str(imcArredondado)\
                + '.' + '\nMagreza grave. Cuide-se.'
        elif imc < 17:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nMagreza moderada. Cuide-se.'
        elif imc < 18.5:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nMagreza leve. Continue se cuidando.'
        elif imc < 25:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nVocê é saudável :)'
        elif imc < 30:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nSobrepeso. Cuide-se.'
        elif imc < 35:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nObesidade grau I. Cuide-se.'
        elif imc < 40:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nObesidade grau II(Severa). Cuide-se.'
        else:
            final = 'O seu IMC é de '+str(imcArredondado)\
                + '.' + '\nObesidade grau III(Mórbida). Cuide-se.'

        return self.imcfinal.set(final)


# Começando Calculadora.
imc()
