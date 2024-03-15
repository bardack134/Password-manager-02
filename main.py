from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.ttk import Notebook
from PasswordGenerator import *
from decrypt import *
from encrypt import *
#modulo utilizado para copiar automaticamente el la password generada
import pyperclip
import json


TEAL="#76ABAE"
BEIGE="#F9E8C9"
PINK='#FFCAD4'
# Número de posiciones que se desplaza las letras y asignar su respuesta a constante llamada SHIFT.  
SHIFT=220#es como un codigo secreto para encryptar nuestros passwords
#contrasena secreta que se usa para poder obtener nuestras passwords del data.txt
SECRET_PASSWORD='mama'



# ------------------------------CALL PASSWORD-----------------------------------------
#TODO: LLAMAR O BUSCAR UNA PASSWORD ESPECIFICA DENTRO DE NUESTRO ARCHIVO .TXT file
def search_password():  
    
    #puede pasar que el archivo todavia no haya sido creado, por eso levantamos un 'try' y 'except'
    try:
        #llamamos al archivo que tiene guardada nuestras password
        with open('data.json', 'r') as file:
            
            #guardamos los datos del archivo en una variable, se guardan tipo diccionario
            data=json.load(file)
            
            
            # # Obtenemos la entrada del usuario y la convertimos a minúsculas
            data_to_search = website_entry_2.get().lower()
                
            
            #puede pasar que el dato que buscamos no exista dentro de nuestros datos, por eso levantamos 'try' y 'except'
            try:
                
                # #obtenemos el email 
                my_email_data=data[data_to_search]['email']       
                
                
                # #obtenemos la contrasena
                my_password_data=data[data_to_search]['password']       
            
            
            except KeyError:
                
                #mostramos al usuario un mensaje de error
                messagebox.showinfo("showinfo", 'Element not found') 
                
                
            else:          
                # #TODO: DESCIFRAREMOS LA CONTRASEÑA GUARDADA EN 'data.json'   
                #  Número de posiciones que se desplaza las letras y asignar su respuesta a una variable llamada shift.  
                shift = SHIFT
                # modificamos el 'SHIFT' para que no importa el numero que se escoja pueda correr y no muestre error "item out of   Range" 
                # #orque da un valor posicional de la lista mayor a la cantidad de items en nuestra lista 
                shift = shift % 27   
                    
            
                # #guardamos la password en una variable llamada text, que recibe nuestra funcion decrypt 
                text=my_password_data
            
            
                # #Llamamos a la funcion que decifra o descodifica nuestra password y la guardamos en una variable
                password_decrypted=decrypt(text, shift)
            
            
                # secret password para mostrar las contrasenas guardadas
                ask_secret_password=askstring(title='secret password', prompt='Introduce the secret password', show="*")
            
            
                #evaluamos si la contrasena secreta o maestra ingresada por el user es correcta o no 
                if ask_secret_password==SECRET_PASSWORD:
                
                    #insertamos la informacion encontrada en los entry para que el usuario la pueda ver
                    email_entry_2.insert(0, my_email_data)
                    
                    
                    password_entry_2.insert(0, password_decrypted)


                else:
                    
                    messagebox.showerror(title='opps', message="Your secret password is incorrect")
                    
                    
    except FileNotFoundError:
        
        messagebox.showerror(title='opps', message="There are no data saved yet")
       
                      
            
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#TODO: CREAMOS FUNCION QUE CREARA NUESTRAS PASSWORDS AL OPRIMIR EL BOTON "generate password"
#funcion que llama a la funcion password_create del archivo PasswordGenerator.py
def call_password_create():
    
    #TODO: VAMOS A CODIFICAR EL PASSWORD GENERADO POR NUESTRA FUNCION
    # Número de posiciones que se desplaza las letras y asignar su respuesta a una variable llamada shift.  
    shift = SHIFT
    #modificamos el 'SHIFT' para que no importa el numero que se escoja pueda correr y no muestre error "item out of   Range" 
    # porque da un valor posicional de la lista mayor a la cantidad de items en nuestra lista 
    shift = shift % 27   
    
    
    #guardamos la password en una variable llamada text, que recibe nuestra funcion decrypt 
    text=password_create()
    
    
    #llamamos a la funcion de encryptar y guardamos password encryptado en una nueva variable
    password_create_encrypted=encrypt(text, shift)
    
    
    #insertaremos nuestra password en el password entry
    password_entry.insert(0, password_create_encrypted)
    
    
    #funcion para copiar automaticamente la password generada
    pyperclip.copy(password_create())
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO: ALMACENAR LA INFORMACION INGRESADA POR EL USUARIO EN UN ARCHIVO TXT.file
def save_data():
    # Obteniendo los datos ingresados por el usuario
    website_data=website_entry.get().lower()
    
    
    email_data=email_entry.get()
    
    
    password_data=password_entry.get()
      
             
    #TODO: ENCRYPTAREMOS LA PASSWORD    
    # Número de posiciones que se desplaza las letras y asignar su respuesta a una variable llamada shift.  
    shift = SHIFT
    #modificamos el 'SHIFT' para que no importa el numero que se escoja pueda correr y no muestre error "item out of   Range" 
    # porque da un valor posicional de la lista mayor a la cantidad de items en nuestra lista 
    shift = shift % 27    
        
        
    #guardamos la password en una variable llamada text, que recibe nuestra funcion encrypt    
    text=password_data

    
    #llamamos a la funcion de encryptar y guardamos password encryptado en una nueva variable
    password_data_encrypted=encrypt(text, shift)
    
    
    #new_data es un diccionario que contiene diccionarios, donde almacenaran los datos de nuestras cuentas 'website'
    new_data={
        website_data:{
            "email": email_data,
            "password":password_data_encrypted,
        }
        
        }  
    
    
    #puedepasar que el usuario no ha ingresado informacion, miramos si el usuario ingreso o no informacion
    if len(website_data)==0 or len(email_data)==0 or len(password_data)==0:
        
        messagebox.showerror(title='opps', message="Please do not leave any fields empty")
    
    
    #es decir el usuario si ingreso informacion
    else:
        
        #preguntamos al usuario  si la informacion agregada es correcta
        yes_or_not=messagebox.askyesno(title=website_data, message=f"Email:{email_data} \nPassword:{password_data} \n\nIs it ok to save?" )
        
        
        if yes_or_not == True:
                      
            #puede pasar que intentemos leer el archivo sin haber sido creado primero            
            try:
                
                with open("data.json", "r") as file:
                    
                    # #cargamos los datos del  archivo data.jason y los guardamos en una variable
                    my_data=json.load(file)              
                                    
                                    
                    #TODO:MIRAR SI EL DATO QUE ESTOY AGREGANDO SE ENCUENTRA YA AGREGADO EN NUESTRO ARCHIVO .json
                    if website_data in my_data:
                        
                        #si ya se encuentra, preguntamos al usuario si lo desea sobre escribir o no
                        are_you_sure=messagebox.askyesno(title="are you sure?", message=f"{website_data} is already saved. Do you want to continue and overwrite the data?" )
                        
                        
                        if are_you_sure==True: 
                            
                            # #actualizamos los datos de la variable
                            my_data.update(new_data)
                

                            #volvemos abrir nuestro archivo pero en modo escritura para actualizar los datos
                            with open("data.json", "w") as file:    
                                
                                # actualizamos los datos que estan guardados en la variable my_data en el archivo data.json
                                json.dump(my_data, file, indent=6)
            
                                                        
                                # Borrando los datos ingresados en los campos de entrada
                                website_entry.delete(0, END)
                                
                                
                                password_entry.delete(0, END)
                                
                                
                                #mensaje indicando al usuario que la informacion fue guardada con exito
                                messagebox.showinfo("showinfo", "Information added correctly" )
                    
                    else:
                        # #actualizamos los datos de la variable
                        my_data.update(new_data)
                

                        #volvemos abrir nuestro archivo pero en modo escritura para actualizar los datos
                        with open("data.json", "w") as file:    
                            
                            # actualizamos los datos que estan guardados en la variable my_data en el archivo data.json
                            json.dump(my_data, file, indent=6)
        
                                                    
                            # Borrando los datos ingresados en los campos de entrada
                            website_entry.delete(0, END)
                            
                            
                            password_entry.delete(0, END)
                            
                            
                            #mensaje indicando al usuario que la informacion fue guardada con                           
                            messagebox.showinfo("showinfo", "Information added correctly" )
                            
                                
            #si el archivo no se encuentra, levantamos una excepcion y creamos el archivo    
            except FileNotFoundError:
                
                #lo abrimos en modo de escritura
                with open("data.json", "w") as file:
                    
                    #y guardamos los datos que estan en new_Data
                    json.dump(new_data, file, indent=6)


                    # Borrando los datos ingresados en los campos de entrada
                    website_entry.delete(0, END)
                    
                    
                    password_entry.delete(0, END)
                    
                    
                    #mensaje indicando al usuario que la informacion fue guardada con exito
                    messagebox.showinfo("showinfo", "Information added correctly" )        
  
#funcion para limpiar las casillas de nuestra window2
def clean():  
    # Borrando los datos ingresados en los campos de entrada
    email_entry_2.delete(0,END)
    website_entry_2.delete(0, END)
    password_entry_2.delete(0, END)    
    
    
# ---------------------------- UI SETUP ------------------------------- #
#TODO: CONFIGURACION INICIAL DE LA VENTANA
window=Tk()

window.config(padx=5, pady=5, bg=TEAL)

window.title('Password Manager') #titulo para nuestra ventana


#TODO:QUIERO QUE MI APP TENGA 2 TABS POR ESO USARE EL WIDGET NOTEBOOK
notebook=Notebook(window)


#pongo el widget Notebook dentro de mi ventana "window"
notebook.pack(padx = 5, pady = 5, expand = True)


#frame de mi primera tab, creo el frame en mi "Notebook"
frame1=Frame(notebook,   padx=50, pady=50,  bg="white")

#Empaqueto 'frame1' para que se expanda y llene todo el espacio disponible
frame1.pack(fill= BOTH, expand=True)


#  Creo un segundo Frame llamado 'frame2' en el notebook
frame2=Frame(notebook, padx=50, pady=50, bg='white')

# Empaquetar 'frame2' para que se expanda y llene todo el espacio disponible
frame2.pack(fill= BOTH, expand=True)


# El método 'add' es específico de la clase Notebook en el módulo ttk de Tkinter. Se utiliza para añadir un marco como una nueva pestaña en el 
# notebook. El argumento text proporciona la etiqueta que se mostrará para esa pestaña en la interfaz de usuario.
notebook.add(frame1, text = "SavePasswords")

# Añadir 'frame2' al notebook con la etiqueta "Window 2"
notebook.add(frame2, text = "SearchPasswords" )


#TODO: #CREAMOS AREA RECTANGULAR  EN NUESTRO 'FRAME1' CONOCIDA COMO 'CANVAS' PARA PONER NUESTRA FOTO ALLI 
#highlightthickness remove the light grey border around my Canvas widget?
canvas=Canvas(frame1, width=200, height=200,  bg="white",  highlightthickness=0)

canvas.grid(row=0, column=1)


#cargando imagen
filename=PhotoImage(file="logo.png")


#creamos la imagen en nuestra ventana, definimos la posicion 'x' y 'y' 100 respectivamente
imagen=canvas.create_image(100, 100, image=filename)


#TODO: CREANDO DEMAS ELEMTOS DE NUESTRA APP "LABELS WIDGET, ENTRY WIDGET, PARA NUESTRA PRIMERA VENTANA" 
#labels "website, email, password"
website_label=Label(frame1, text='Website:',  bg="white", pady=5, font=('helvetica', 12))

website_label.grid(row=1, column=0)


Email_label=Label(frame1, text='Email/Username:',  bg="white", pady=5, font=('helvetica', 12))

Email_label.grid(row=2, column=0)


password_label=Label(frame1, text='Password:',  bg="white", pady=5,  font=('helvetica', 12))

password_label.grid(row=3, column=0)


#VARIABLES DONDE SE ALMACENARA LOS DATOS INGRESADOS POR EL USUARIO WINDOW 1
#entry widgets para cada label
website_entry=Entry(frame1,  width=50, relief=SOLID)

website_entry.grid(row=1, column=1, columnspan=2)

#establesiendo el foco en nuestro website_entry, es decir al arrancar la app, el mause aparece inmediatamente ahi
website_entry.focus()


email_entry=Entry(frame1,  width=50, relief=SOLID)

email_entry.grid(row=2, column=1, columnspan=2)

email_entry.insert(0,'@gmail.com') #insertamos el sgt msj en el widget 'email_entry' para que se muestre apenas corre el programa


password_entry=Entry(frame1,  width=32, relief=SOLID)

password_entry.grid(row=3, column=1)


#BOTON GENERATE PASSWORD, ADD, SEARCH  WINDOW 1
generate_password_button=Button(frame1, text='Generate Password', relief=GROOVE, bg=BEIGE, command=call_password_create)

generate_password_button.grid(row=3, column=2)


add_button=Button(frame1, text='Add', width=43, relief=GROOVE, bg="white", command=save_data)

add_button.grid(row=4, column=1, columnspan=2)


# ---------------------------------SECOND WINDOW ----------------------------------------------------------------
#TODO: CREAMOS NUESTRA SEGUNDA VENTANA PARA QUE EL USUARIO BUSQUE SUS PASSWORDS
#highlightthickness remove the light grey border around my Canvas widget?
canvas_2=Canvas(frame2, width=200, height=200,  bg="white",  highlightthickness=0)

canvas_2.grid(row=0, column=1)


#creamos la imagen en nuestra ventana, en el segundo canvas, del frame 2
imagen=canvas_2.create_image(100, 100, image=filename)


#labels "website, email, password de nuestra  window2"
website_label_2=Label(frame2, text='Website:',  bg="white", pady=5, font=('helvetica', 12))

website_label_2.grid(row=1, column=0)


Email_label_2=Label(frame2, text='Email/Username:',  bg="white", pady=5, font=('helvetica', 12))

Email_label_2.grid(row=2, column=0)


password_label_2=Label(frame2, text='Password:',  bg="white", pady=5,  font=('helvetica', 12))

password_label_2.grid(row=3, column=0)


#entry widgets para cada label
website_entry_2=Entry(frame2, width=50, relief=SOLID)

website_entry_2.grid(row=1, column=1,  columnspan=2)


email_entry_2=Entry(frame2, width=50, relief=SOLID)

email_entry_2.grid(row=2, column=1, columnspan=2)


password_entry_2=Entry(frame2, width=50, relief=SOLID)

password_entry_2.grid(row=3, column=1, columnspan=2)


#Botones
search_button=Button(frame2, text='Search', width=43, relief=GROOVE, bg=BEIGE, command=search_password)

search_button.grid(row=4, column=1, columnspan=2 )


clean_button=Button(frame2, text='Clean', width=43, relief=GROOVE, bg=PINK, command=clean)

clean_button.grid(row=5, column=1, columnspan=2, pady=5 )


window.mainloop()