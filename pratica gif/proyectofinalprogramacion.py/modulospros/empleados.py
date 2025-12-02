import pandas
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from colorama import Style, Fore,Back,init
import os
import tkinter as tk
from tkinter import simpledialog, messagebox


trabajadores_uid={
        '0321':{
            'nombre':'Omar'},
        '8149':{
            'nombre':'Monge'},
        '281818':{
            'nombre':'Isaias'},
        '371442':{
            'nombre':'Akzel'},
        '171007':{
            'nombre':"Chris"
        }
}
trabajdores='trabajadoressuid.csv'
if os.path.exists(trabajdores):
    df_temp = pandas.read_csv(trabajdores, index_col=0, dtype=str)
    trabajadores_uid = df_temp.to_dict(orient='index')
    trabajadores_uid_limpio = {}
    for uid, datos in trabajadores_uid.items():
        uid_str = str(uid) 
        datos_limpios = {k: v for k, v in datos.items() if pandas.notna(v) and v is not None}
        trabajadores_uid_limpio[uid_str] = datos_limpios
    trabajadores_uid = trabajadores_uid_limpio
else:

    df_temp = pandas.DataFrame.from_dict(trabajadores_uid, orient='index')
    df_temp.to_csv(trabajdores, index_label='uid')

def eliminar_nuevo_empleado():
    global trabajadores_uid, trabajdores
    print("-"*50)
    a_quien_vamos_a_eliminar=input("Que empleado vamos a eliminar: (uid) ").strip()
    if a_quien_vamos_a_eliminar in trabajadores_uid:
        if a_quien_vamos_a_eliminar=="171007":
            print(Fore.RED+Style.BRIGHT+"no se puede eliminar el admin"+Style.RESET_ALL)
            return
        del trabajadores_uid[a_quien_vamos_a_eliminar]
        guardar_empleados_csv()
        print(Fore.RED+"se ha eliminado de manera correcta")
        print(trabajadores_uid)
    else:
        print("invalido")
        input("enter para continuar ")
        eliminar_nuevo_empleado()
def guardar_empleados_csv():
    global trabajadores_uid, trabajdores
    df_guardar = pandas.DataFrame.from_dict(trabajadores_uid, orient='index')
    df_guardar.to_csv(trabajdores, index_label='uid')
    print(Fore.CYAN + " se han guardado los datos chaval" + Style.RESET_ALL)

def agregar_nuevo_empleado(parent=None):
    global trabajadores_uid, trabajdores
    nombre_nuevo_empleado=simpledialog.askstring('Nuevo empleado', 'Nombre del nuevo usuario:', parent=parent) #input(Fore.WHITE+"cual es el nombre del nuevo usuario: ").upper()
    if not nombre_nuevo_empleado:
                messagebox.showinfo('Cancelado', 'Operación cancelada por el usuario')
                return
    uid_nuevo_empleado= simpledialog.askstring('Nuevo empleado', 'UID del nuevo usuario:', parent=parent)   #input(Fore.WHITE+"cual es el uid del nuevo usuario: ").upper()
    if uid_nuevo_empleado in trabajadores_uid:
        messagebox.showerror('Error', 'UID ya existe', parent=parent) #print("-------------ESTE YA ESTA-----------")
        return 
    trabajadores_uid[uid_nuevo_empleado] = {'nombre': nombre_nuevo_empleado}
    guardar_empleados_csv()
    #print("/"*60)
    messagebox.showinfo('Éxito', f'Empleado {nombre_nuevo_empleado} agregado correctamente', parent=parent) #print(Fore.GREEN+Style.BRIGHT+"SE HA AGREGADO EXITOSAMENTE"+Style.RESET_ALL)
    #print(trabajadores_uid)
    return trabajadores_uid



#    def agregar_nuevo_empleado(parent=None)
#try:
#        gui_active = tk._default_root is not None
#    except Exception:
#        gui_active = False
#    
#    if gui_active:
#        # Usar interfaz gráfica con tkinter
#        resultado = messagebox.askyesno('Agregar empleado', '¿Deseas agregar un nuevo empleado?')
#        if not resultado:
#            messagebox.showinfo('Cancelado', 'Operación cancelada por el usuario')
#            return
#        
#        # Ejecutar en hilo para no bloquear la GUI
#        def agregar_en_hilo():
#            try:
#                empleados.agregar_nuevo_empleado()
#                messagebox.showinfo('Éxito', 'Empleado agregado correctamente')
#            except Exception as e:
#                messagebox.showerror('Error', f'Error al agregar empleado: {str(e)}')
#        
#        t = threading.Thread(target=agregar_en_hilo, daemon=True)
 #       t.start()
#    else:
  #      # Interfaz CLI (para fallback)
   #     agregar_empleado = input("desea agregar un empleado? si/no: ").strip().lower()
    #    if agregar_empleado == "si":
     #       try:
      #          empleados.agregar_nuevo_empleado()
    #            print(Fore.GREEN + Style.BRIGHT + "EMPLEADO AGREGADO CON EXITO" + Style.RESET_ALL)
    #        except Exception as e:
    #            print(Fore.RED + Style.BRIGHT + f"Error: {str(e)}" + Style.RESET_ALL)
    #    else:
    #        print(Fore.YELLOW + Style.BRIGHT + "OPERACION CANCELADA POR EL USUARIO" + Style.RESET_ALL)


#def agregar_nuevo_empleado(parent=None):
#    """Agregar un nuevo empleado usando diálogos tkinter. Devuelve el diccionario actualizado o None si se canceló."""
#    if simpledialog is None:
#        raise RuntimeError('tkinter no está disponible en este entorno')
#
#    nombre = simpledialog.askstring('Nuevo empleado', 'Nombre del nuevo usuario:', parent=parent)
#    if not nombre:
#        return None
#    uid = simpledialog.askstring('Nuevo empleado', 'UID del nuevo usuario:', parent=parent)
#    if not uid:
#        return None
#
#    nombre = nombre.strip()
#    uid = str(uid).strip()
#    if uid in trabajadores_uid:
#        messagebox.showerror('Error', 'UID ya existe', parent=parent)
#        return None
#
#    trabajadores_uid[uid] = {'nombre': nombre}
#    guardar_empleados_csv()
#    messagebox.showinfo('Éxito', f'Empleado {nombre} agregado correctamente', parent=parent)
#    return trabajadores_uid



