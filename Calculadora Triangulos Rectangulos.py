from tkinter import *

root = Tk()
root.title("Calculadora Triangulos Rectangulos")
#python -m auto_py_to_exe
root.state("zoomed")

def home_page():
    lb = Label(main_frame, text="INICIO", font=("Arial black",25))
    lb.place(relx=0.50,rely=0.10,anchor=CENTER)
    lbdesc = Label(main_frame, font=("Arial black",25), text="Esta es una aplicación para calcular \nTriángulos Rectángulos, La forma de en la \nque trabaja esta aplicación es usando 2 \nnúmeros, con esos números se hacen todos \nlos calculos internos y obtenemos el \nresultado esperado.")
    lbdesc.place(relx=0.50,rely=0.50,anchor=CENTER)

def hipotenusa_page():
    lb = Label(main_frame, text="HIPOTENUSA", font=("Arial black",25))
    lb.place(relx=0.50,rely=0.10,anchor=CENTER)

    hipotenuse_btn = Button(main_frame, text="CALCULAR HIPOTENUSA", font=("Arial black", 18), bg="#FF6F61", fg='white',
                    cursor="hand2",command=lambda: pages(hipotenuse_op))
    hipotenuse_btn.place(rely=0.35,relx=0.50,width=380, height=100, anchor=CENTER)

    cateto_btn = Button(main_frame, text="CALCULAR CATETO", font=("Arial black", 18), bg="#FF6F61", fg='white',
                    cursor="hand2",command=lambda: pages(cateto_op))
    cateto_btn.place(rely=0.60,relx=0.50,width=380, height=100, anchor=CENTER)

    def hipotenuse_op():
        lb = Label(main_frame, text="HIPOTENUSA", font=("Arial black",25))
        lb.place(relx=0.50,rely=0.10,anchor=CENTER)

        def calculate_hipotenuse():
            cateto1 = float(e1.get())
            cateto2 = float(e2.get())
            hipotenusa = cateto1/cateto2
            e3.delete(0, "end")
            e3.insert(END, f'{hipotenusa}')
                
                            # Crear entradas y etiquetas
        label1 = Label(main_frame,font=("Arial black", 14), text="Cateto 1")
        label1.place(rely=0.27,relx=0.22,anchor=W)

        label2 = Label(main_frame,font=("Arial black", 14), text="Cateto 2")
        label2.place(rely=0.42,relx=0.22,anchor=W)

        label3 = Label(main_frame,font=("Arial black", 14), text="Hipotenusa")
        label3.place(rely=0.57,relx=0.22,anchor=W)

        e1 = Entry(main_frame,font=("Arial black", 14))
        e1.place(rely=0.27,relx=0.78,relheight=0.06,anchor=E)

        e2 = Entry(main_frame,font=("Arial black", 14))
        e2.place(rely=0.42,relx=0.78,relheight=0.06,anchor=E)

        e3 = Entry(main_frame,font=("Arial black", 14))
        e3.place(rely=0.57,relx=0.78,relheight=0.06,anchor=E)
        e3.config()

        bt_calculate = Button(main_frame, text="Calcular Tangente",cursor="hand2", command=calculate_hipotenuse,
                            font=("Arial black", 18), bg="#FF6F61", fg='white')
        bt_calculate.place(rely=0.75,relx=0.50, anchor=CENTER) 

    def cateto_op():
        lb = Label(main_frame, text="HIPOTENUSA", font=("Arial black",25))
        lb.place(relx=0.50,rely=0.10,anchor=CENTER)      

        def calculate_cateto():
            cateto1 = float(e1.get())
            hipotenusa = float(e2.get())
            cateto2 = cateto1/hipotenusa
            e3.delete(0, "end")
            e3.insert(END, f'{cateto2}')
            
                            # Crear entradas y etiquetas
        label1 = Label(main_frame,font=("Arial black", 14), text="Cateto 1")
        label1.place(rely=0.27,relx=0.22,anchor=W)

        label2 = Label(main_frame,font=("Arial black", 14), text="Hipotenusa")
        label2.place(rely=0.42,relx=0.22,anchor=W)

        label3 = Label(main_frame,font=("Arial black", 14), text="Cateto 2")
        label3.place(rely=0.57,relx=0.22,anchor=W)

        e1 = Entry(main_frame,font=("Arial black", 14))
        e1.place(rely=0.27,relx=0.78,relheight=0.06,anchor=E)

        e2 = Entry(main_frame,font=("Arial black", 14))
        e2.place(rely=0.42,relx=0.78,relheight=0.06,anchor=E)

        e3 = Entry(main_frame,font=("Arial black", 14))
        e3.place(rely=0.57,relx=0.78,relheight=0.06,anchor=E)
        e3.config()

        bt_calculate = Button(main_frame, text="Calcular Tangente",cursor="hand2", command=calculate_cateto,
                            font=("Arial black", 18), bg="#FF6F61", fg='white')
        bt_calculate.place(rely=0.75,relx=0.50, anchor=CENTER) 

def seno_page():
    lb = Label(main_frame, text="SENO", font=("Arial black",25))
    lb.place(relx=0.50,rely=0.10,anchor=CENTER)

    def calculate_seno():
        anguloOpuesto = float(e1.get())
        hipotenusa = float(e2.get())
        seno = anguloOpuesto/hipotenusa
        e3.delete(0, "end")
        e3.insert(END, f'{seno}')

    # Crear entradas y etiquetas
    label1 = Label(main_frame,font=("Arial black", 14), text="Ángulo Opuesto")
    label1.place(rely=0.27,relx=0.22,anchor=W)

    label2 = Label(main_frame,font=("Arial black", 14), text="Hipotenusa")
    label2.place(rely=0.42,relx=0.22,anchor=W)

    label3 = Label(main_frame,font=("Arial black", 14), text="Seno")
    label3.place(rely=0.57,relx=0.22,anchor=W)

    e1 = Entry(main_frame,font=("Arial black", 14))
    e1.place(rely=0.27,relx=0.78,relheight=0.06,anchor=E)

    e2 = Entry(main_frame,font=("Arial black", 14))
    e2.place(rely=0.42,relx=0.78,relheight=0.06,anchor=E)

    e3 = Entry(main_frame,font=("Arial black", 14))
    e3.place(rely=0.57,relx=0.78,relheight=0.06,anchor=E)
    e3.config()


    # Crear botones
    bt_calculate = Button(main_frame, text="Calcular Seno",cursor="hand2", command=calculate_seno,
                        font=("Arial black", 18), bg="#FF6F61", fg='white')
    bt_calculate.place(rely=0.75,relx=0.50, anchor=CENTER) 

def coseno_page():
    lb = Label(main_frame, text="COSENO", font=("Arial black",25))
    lb.place(relx=0.50,rely=0.10,anchor=CENTER)

    def calculate_coseno():
        anguloAdyacente = float(e1.get())
        hipotenusa = float(e2.get())
        coseno = anguloAdyacente/hipotenusa
        e3.delete(0, "end")
        e3.insert(END, f'{coseno}')

    # Crear entradas y etiquetas
    label1 = Label(main_frame,font=("Arial black", 14), text="Ángulo Opuesto")
    label1.place(rely=0.27,relx=0.22,anchor=W)

    label2 = Label(main_frame,font=("Arial black", 14), text="Hipotenusa")
    label2.place(rely=0.42,relx=0.22,anchor=W)

    label3 = Label(main_frame,font=("Arial black", 14), text="Coseno")
    label3.place(rely=0.57,relx=0.22,anchor=W)

    e1 = Entry(main_frame,font=("Arial black", 14))
    e1.place(rely=0.27,relx=0.78,relheight=0.06,anchor=E)

    e2 = Entry(main_frame,font=("Arial black", 14))
    e2.place(rely=0.42,relx=0.78,relheight=0.06,anchor=E)

    e3 = Entry(main_frame,font=("Arial black", 14))
    e3.place(rely=0.57,relx=0.78,relheight=0.06,anchor=E)
    e3.config()


    # Crear botones
    bt_calculate = Button(main_frame, text="Calcular Coseno",cursor="hand2", command=calculate_coseno,
                        font=("Arial black", 18), bg="#FF6F61", fg='white')
    bt_calculate.place(rely=0.75,relx=0.50, anchor=CENTER) 


def tangente_page():
    lb = Label(main_frame, text="TANGENTE", font=("Arial black",25))
    lb.place(relx=0.50,rely=0.10,anchor=CENTER)

    def calculate_tangente():
        anguloOpuesto = float(e1.get())
        anguloAdyacente = float(e2.get())
        tangente = anguloOpuesto/anguloAdyacente
        e3.delete(0, "end")
        e3.insert(END, f'{tangente}')

    # Crear entradas y etiquetas
    label1 = Label(main_frame,font=("Arial black", 14), text="Ángulo Opuesto")
    label1.place(rely=0.27,relx=0.22,anchor=W)

    label2 = Label(main_frame,font=("Arial black", 14), text="Ángulo Adyacente")
    label2.place(rely=0.42,relx=0.22,anchor=W)

    label3 = Label(main_frame,font=("Arial black", 14), text="Tangente")
    label3.place(rely=0.57,relx=0.22,anchor=W)

    e1 = Entry(main_frame,font=("Arial black", 14))
    e1.place(rely=0.27,relx=0.78,relheight=0.06,anchor=E)

    e2 = Entry(main_frame,font=("Arial black", 14))
    e2.place(rely=0.42,relx=0.78,relheight=0.06,anchor=E)

    e3 = Entry(main_frame,font=("Arial black", 14))
    e3.place(rely=0.57,relx=0.78,relheight=0.06,anchor=E)
    e3.config()

    # Crear botones
    bt_calculate = Button(main_frame, text="Calcular Tangente",cursor="hand2", command=calculate_tangente,
                        font=("Arial black", 18), bg="#FF6F61", fg='white')
    bt_calculate.place(rely=0.75,relx=0.50, anchor=CENTER) 


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def pages(page):
    delete_pages()
    page()

def hoverActive(boton):
	boton.configure(bg="#FF6F61")
	def fuera(e):
		boton.configure(bg="#FF6F61")
	def dentro(e):
		boton.configure(bg="red")
	def activo(e):
		boton.configure(fg="white")

	boton.bind("<Enter>", dentro)
	boton.bind("<Leave>", fuera)
	boton.bind("<ButtonPress-1>", activo)

options_frame = Frame(root,bg="#c3c3c3")
options_frame.pack(side=LEFT)
options_frame.configure(width=400, height=1080)

home_button = Button(options_frame, text="INICIO", font=("Arial Black",18),fg='white',
                    cursor="hand2",command=lambda: (pages(home_page)))
home_button.place(x=50, y=130,width=300,height=70)
hoverActive(home_button)

op1_button = Button(options_frame, text="CALCULAR \n LA HIPOTENUSA", font=("Arial Black",18),fg='white',
                    cursor="hand2",command=lambda: (pages(hipotenusa_page)))
op1_button.place(x=50, y=300,width=300, height=70)
hoverActive(op1_button)

op2_button = Button(options_frame, text="CALCULAR\nSENO", font=("Arial Black",18),fg='white',
                    cursor="hand2",command=lambda: (pages(seno_page)))
op2_button.place(x=50, y=470,width=300, height=70)
hoverActive(op2_button)

op3_button = Button(options_frame, text="CALCULAR\nCOSENO", font=("Arial Black",18),fg='white',
                    cursor="hand2",command=lambda: (pages(coseno_page)))
op3_button.place(x=50, y=640,width=300, height=70)
hoverActive(op3_button)

op4_button = Button(options_frame, text="CALCULAR\nTANGENTE", font=("Arial Black",18),fg='white',
                    cursor="hand2",command=lambda: (pages(tangente_page)))
op4_button.place(x=50, y=810,width=300, height=70)
hoverActive(op4_button)

main_frame = Frame(root)
main_frame.pack()
main_frame.pack_propagate(False)
main_frame.configure(height=1920, width=1080)


#Inicio Programa
root.mainloop()