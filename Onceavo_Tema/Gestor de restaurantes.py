from tkinter import *
operador=''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.insert(END,operador)
#Iniciar tkinter
aplicacion = Tk()


#Tamaño de la ventana
aplicacion.geometry('1200x630+0+0')

#Evitar maximizar pestaña
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title('Restaurante - Sistema de Facturación')

#color fondo pantalla
'''aplicacion.config(bg='')
'''

#PANEL SUPERIOR
panelSup = Frame(aplicacion, bd = 1, relief = FLAT )
panelSup.pack(side = TOP)
#titulo
etiqueta_titulo = Label(panelSup, text='Sistema de Facturacion', fg='azure4',
                        font = ('Dosis', 58), bg= 'burlywood',width = 27)
etiqueta_titulo.grid(row= 0, column = 0)


#PANEL IZQUIERO
panelIzq = Frame(aplicacion, bd = 1, relief = FLAT)
panelIzq.pack(side = LEFT)
#PANEL costos
panel_costos = Frame(panelIzq, bd = 1, relief = FLAT,bg='azure4',padx=65)
panel_costos.pack(side = BOTTOM)
#PANEL comidas
panel_comida = LabelFrame(panelIzq,text= 'Comida',font = ('Dosis',19,'bold'),
                          bd = 1, relief = FLAT, fg = 'azure4')
panel_comida.pack(side = LEFT)
#PANEL bebidas
panel_bebidas = LabelFrame(panelIzq,text= 'Bebidas',font = ('Dosis',19,'bold'),
                          bd = 1, relief = FLAT, fg = 'azure4')
panel_bebidas.pack(side = LEFT)
#PANEL postres
panel_Postres = LabelFrame(panelIzq,text= 'Postres',font = ('Dosis',19,'bold'),
                          bd = 1, relief = FLAT, fg = 'azure4')
panel_Postres.pack(side = LEFT)

#PANEL DERECHA
panel_derecha = Frame(aplicacion, bd= 1, relief = FLAT)
panel_derecha.pack(side = RIGHT)
#Panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1, relief = FLAT, bg = 'burlywood')
panel_calculadora.pack()
#Panel recibo
panel_recibo = Frame(panel_derecha,bd=1, relief = FLAT, bg = 'burlywood')
panel_recibo.pack()
#Panel botones
panel_botones = Frame(panel_derecha,bd=1, relief = FLAT, bg = 'burlywood')
panel_botones.pack()

#Lista de productos
lista_comida= ['hamburguesas','pizza','hotdogs','tacos','enchiladas','nuggets','papas fritas','banderillas']
lista_bebidas = ['agua','soda', 'jugos','piña colada','coca-cola','cerveza','vino','mezcal']
lista_postres=['helado','fruta','brownies','flan','pay','pastel1','pastel2','pastel3']
#Generar items comida
variables_comida =[]
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comida:
    #crear checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida =Checkbutton(panel_comida,
                        text=comida.title(),
                        font = ('Dosis',19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable = variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)

    #Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador]= StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comida,
                                     font =('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador+= 1
# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
     variables_bebida.append('')
     variables_bebida[contador] = IntVar()
     bebida = Checkbutton(panel_bebidas,
                          text=bebida.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_bebida[contador])
     bebida.grid(row=contador,
                 column=0,
                 sticky=W)
     # Crear cuadros de entrada
     cuadros_bebida.append('')
     texto_bebida.append('')
     texto_bebida[contador] = StringVar()
     texto_bebida[contador].set('0')
     cuadros_bebida[contador] = Entry(panel_bebidas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_bebida[contador])
     cuadros_bebida[contador].grid(row=contador,
                                   column=1)

     contador += 1
# Generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
     variables_postres.append('')
     variables_postres[contador] = IntVar()
     postres = Checkbutton(panel_Postres,
                           text=postres.title(),
                           font=('Dosis', 19, 'bold'),
                           onvalue=1,
                           offvalue=0,
                           variable=variables_postres[contador])
     postres.grid(row=contador,
                  column=0,
                  sticky=W)
     # Crear cuadros de entrada
     cuadros_postres.append('')
     texto_postres.append('')
     texto_postres[contador] = StringVar()
     texto_postres[contador].set('0')
     cuadros_postres[contador] = Entry(panel_Postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
     cuadros_postres[contador].grid(row=contador,
                                   column=1)
     contador += 1



#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()
#Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text ='Costo Comida',
                              font = ('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,
                           column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width =10,
                           state='readonly',
                           textvariable= var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=41)
#
etiqueta_costo_bebida = Label(panel_costos,
                              text ='Costo Bebida',
                              font = ('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,
                           column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width =10,
                           state='readonly',
                           textvariable= var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=41)
#
etiqueta_costo_postres = Label(panel_costos,
                              text ='Costo Postres',
                              font = ('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2,
                            column=0)
texto_costo_postres = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width =10,
                           state='readonly',
                           textvariable= var_costo_postres)
texto_costo_postres.grid(row=2,column=1,padx=41)
#
etiqueta_subtotal = Label(panel_costos,
                              text ='Subtotal',
                              font = ('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0,
                           column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width =10,
                           state='readonly',
                           textvariable= var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=41)
#
etiqueta_impuesto = Label(panel_costos,
                              text ='Impuesto',
                              font = ('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1,
                           column=2)
texto_impuesto = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width =10,
                           state='readonly',
                           textvariable= var_impuesto)
texto_impuesto.grid(row=1,column=3,padx=41)
#
etiqueta_total = Label(panel_costos,
                              text ='Total',
                              font = ('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2,
                           column=2)
texto_total = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width =10,
                           state='readonly',
                           textvariable= var_total)
texto_total.grid(row=2,column=3,padx=41)

#botones
botones =['Total','Recibo','Guardar','Resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',14,'bold'),
                   fg= 'Black',
                   bg='azure4',
                   bd =2,
                   width=9)
    boton.grid(row=0,
               column=columnas)
    columnas+=1
#area de recibo
texto_recibo = Text(panel_recibo,
                    font= ('Dosis',12,'bold'),
                    bd =1,
                    width =42,
                    height =10)
texto_recibo.grid(row=0,column=0)

#calculadora
visor_calculadora=Entry(panel_calculadora,
                        font=('Dosis',16,'bold'),
                        width =32,
                        bd=1)
visor_calculadora.grid(row=1,column=0,
                       columnspan=4)

botones_calculadora =['7','8','9','+','4','5','6','-',
                      '1','2','3','x','R','B','0','/']
botones_guardados = []
fila = 1
columna =0
for boton in botones_calculadora:
    boton= Button(panel_calculadora,
                  text=boton.title(),
                  font=('Dosis',16,'bold'),
                  fg='black',
                  bg='azure4',
                  bd=1,
                  width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila +=1
    columna+=1
    if columna == 4:
        columna= 0


botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))












#Evitar que se cierre
aplicacion.mainloop()


