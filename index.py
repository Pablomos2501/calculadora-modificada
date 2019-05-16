from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 400
        
        #alto
        alto = 300
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('porgrama de calculadora by. Pablo Moscoso')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Sumar 2 valores')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'primer numero: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'segundo numero: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)
        
        #Creamos un boton para ejecutar la suma
        Button(frame, text = 'Sumar', command = self.sumar).grid(row = 3, columnspan = 2, sticky = W + E)

        #creo yo el boton de resta 
        Button(frame, text = 'Restar', command = self.Restar).grid(row = 4, columnspan = 2, sticky = W + E)

        #creo yo el boton de multiplicacion 
        Button(frame, text = 'multiplicar', command = self.Multiplicacion).grid(row = 5, columnspan = 2, sticky = W + E)

        #creo yo el boton de la division 
        Button(frame, text = 'dividir', command = self.dividir).grid(row = 6, columnspan = 2, sticky = W + E)
        

        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    # esta es la función que ejecuta la suma
    def sumar(self):
        if self.validation():
            resultado = float( self.var1.get() ) + float( self.var2.get() )
            self.message['text'] = 'La suma de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'
    
    # esta es la función que ejecuta la Resta
    def Restar(self):
        if self.validation():
            resultado = float( self.var1.get() ) - float( self.var2.get() )
            self.message['text'] = 'La Resta de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'
    
    # esta es la función que ejecuta la multiplicacion 
    def Multiplicacion(self):
        if self.validation():
            resultado = float( self.var1.get() ) // float( self.var2.get() )
            self.message['text'] = 'La Multiplicacion  de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'

            # esta es la función que ejecuta la multiplicacion 
    def dividir(self):
        if self.validation():
            resultado = float( self.var1.get() ) * float( self.var2.get() )
            self.message['text'] = 'La Division  de las 2 variables es: {}'.format(resultado)
        else:
            self.message['text'] = 'los campos son requeridos'

#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()