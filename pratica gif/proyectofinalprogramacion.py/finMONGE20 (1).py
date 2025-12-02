import pandas
from pandas import Series
import matplotlib.pyplot as plt
from colorama import Style, Fore, Back, init
from modulospros import empleados
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
import threading
trabajdores = 'trabajadoressuid.csv'
stocksito = 'iostockinventar.csv'
ventaproducto='ventaproducto.csv'
# df es el dataframe principal que ordena a panda leer un archivo csv llamado "iostockinverntar.cvs"

df = pandas.read_csv(stocksito)
if os.path.exists(trabajdores):
    df_temp = pandas.read_csv(trabajdores, index_col=0, dtype=str)
    trabajadores_uid = df_temp.to_dict(orient='index')
    trabajadores_uid_limpio = {}
    for uid, datos in trabajadores_uid.items():
        uid_str = str(uid).strip()
        datos_limpios = {k: v for k, v in datos.items() if pandas.notna(v) and v is not None}
        trabajadores_uid_limpio[uid_str] = datos_limpios
    trabajadores_uid = trabajadores_uid_limpio
if os.path.exists(ventaproducto):
    df_ventas = pandas.read_csv(ventaproducto)

def entrada_trabajador(force_cli=False):
    """Solicita el UID del trabajador. If force_cli True, uses CLI fallback even if GUI is present."""
    try:
        gui_active = (tk._default_root is not None) and (not force_cli)
    except Exception:
        gui_active = False

    if gui_active:
        uid_entrada = simpledialog.askstring('Ingreso', 'Ingresa tu UID:', parent=tk._default_root)
        if uid_entrada is None:
            return
        uid_entrada_str = str(uid_entrada).strip()

        if uid_entrada_str == "171007":
            # administrador: mostrar menú GUI con permisos
            gui_show_menu()
            return
        elif 'trabajadores_uid' in globals() and uid_entrada_str in trabajadores_uid:
            nombre_empleado = trabajadores_uid.get(uid_entrada_str, {}).get('nombre', 'Usuario')
            messagebox.showinfo('Bienvenido', f'Bienvenido {nombre_empleado}', parent=tk._default_root)
            gui_show_menu()
            return
        else:
            messagebox.showerror('Error', 'Ingrese un UID válido', parent=tk._default_root)
            return
    else:
        # fallback CLI
        uid_entrada = input(Fore.WHITE + "            ingresa tu uid :" + Style.RESET_ALL).strip()
        uid_entrada_str = str(uid_entrada)
        if uid_entrada == "171007":
            print("")
            # admin CLI menu (use existing mostrar_menu fallback)
        elif 'trabajadores_uid' in globals() and uid_entrada_str in trabajadores_uid:
            nombre_empleado = trabajadores_uid.get(uid_entrada_str, {}).get('nombre', 'Usuario')
            print(Fore.GREEN + Style.BRIGHT + f"Bienvenido {nombre_empleado}" + Style.RESET_ALL)

        else:
            print(Fore.RED + "ingrese un UID valido" + Style.RESET_ALL)
            entrada_trabajador(force_cli=True)

def graficar_venta_productos():
    print("Generando gráfica de stock por producto...")
    plt.figure(figsize=(12, 8))
    plt.bar(df_ventas['producto'], df_ventas['ventas_acumuladas'], color='skyblue')
    plt.title('Venta Por Producto', fontsize=16)
    plt.ylabel('Cantidad de venta')
    plt.xlabel('Productos')
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

verduras_venta = 0
carne_vetas = 0
jugo_venta = 0
lacteos_ventas = 0
abarrotes_ventas = 0
limpieza_venta = 0
venta_turno = 0

def venta_producto():
    """Interfaz de venta usando diálogos Tkinter. Diseñada para ejecutarse en el hilo principal."""
    global verduras_venta, carne_vetas, jugo_venta, lacteos_ventas, abarrotes_ventas, limpieza_venta, venta_turno, df

    # Recolectar ventas en este flujo
    cuenta = 0.0
    ticket_lines = []

    while True:
        # preguntar si desea vender
        continuar = messagebox.askyesno('Venta', '¿Deseas vender un producto?')
        if not continuar:
            break

        # Mostrar categorías disponibles
        categorias = [str(x) for x in df['categoria'].dropna().unique()]
        categorias_text = '\n'.join(categorias) if categorias else 'Sin categorías'
        categoria = simpledialog.askstring('Categoría', f'Categorías disponibles:\n{categorias_text}\n\nIngresa la categoría:')
        if not categoria:
            continue
        cat_norm = categoria.strip().lower()

        prod_df = df[df['categoria'].astype(str).str.lower().str.strip() == cat_norm]
        if prod_df.empty:
            prod_df = df[df['categoria'].astype(str).str.lower().str.contains(cat_norm)]
        if prod_df.empty:
            messagebox.showerror('Error', 'No hay productos para esa categoría')
            continue

        productos_text = '\n'.join([f"{r['producto']} (Stock: {r['stock']})" for _, r in prod_df.iterrows()])
        producto = simpledialog.askstring('Producto', f'Productos en {categoria}:\n{productos_text}\n\nIngresa el nombre exacto del producto:')
        if not producto:
            continue
        producto = producto.strip()

        # buscar producto (case-insensitive)
        match = df[df['producto'].astype(str).str.lower().str.strip() == producto.lower()]
        if match.empty:
            producto_title = producto.title()
            match = df[df['producto'] == producto_title]
        if match.empty:
            messagebox.showerror('Error', 'Producto no encontrado')
            continue

        prod_name = match.iloc[0]['producto']
        stock_actual = int(match.iloc[0]['stock'])
        cantidad = simpledialog.askinteger('Cantidad', f'Stock actual de {prod_name}: {stock_actual}\n¿Cuántas unidades vender?', minvalue=1, maxvalue=stock_actual)
        if cantidad is None:
            continue

        # actualizar stock
        df.loc[df['producto'] == prod_name, 'stock'] -= cantidad
        df.to_csv(stocksito, index=False)

        precio_unitario = float(df.loc[df['producto'] == prod_name, 'precios'].values[0])
        total = precio_unitario * cantidad
        cuenta += total
        ticket_lines.append(f"{prod_name} - Cantidad: {cantidad} - Total: {total:.2f}")

        # actualizar totales por categoría
        cat_actual = str(df.loc[df['producto'] == prod_name, 'categoria'].values[0]).lower()
        if 'verd' in cat_actual:
            verduras_venta += total
        elif 'carne' in cat_actual:
            carne_vetas += total
        elif 'jug' in cat_actual:
            jugo_venta += total
        elif 'lact' in cat_actual:
            lacteos_ventas += total
        elif 'abar' in cat_actual:
            abarrotes_ventas += total
        elif 'limp' in cat_actual:
            limpieza_venta += total

        venta_turno += 1
        messagebox.showinfo('Ticket parcial', '\n'.join(ticket_lines))

    # resumen final
    iva = cuenta * 0.16
    resumen = f"Total: {cuenta:.2f}\nIVA (16%): {iva:.2f}\n\nTicket:\n" + ('\n'.join(ticket_lines) if ticket_lines else 'Sin ventas')
    messagebox.showinfo('Resumen de venta', resumen)


def agregar_stock():
    producto_agregar_stock = input("A que producto deseas agregar?: ").strip().title()
    if producto_agregar_stock in df['producto'].values:
        cuant_desea_agregar = input("cuanto stock agregar? (no letras) ")
        try:
            cuant_desea_agregar = int(cuant_desea_agregar)
            if cuant_desea_agregar > 0:
                df.loc[df['producto'] == producto_agregar_stock, 'stock'] += cuant_desea_agregar
                df.to_csv('iostockinventar.csv', index=False)
                stock_producto = df.loc[df['producto'] == producto_agregar_stock, 'stock'].values[0]
                print(Fore.GREEN + Style.BRIGHT + "SE HA AGREGADO EL PRODUCTO" + Style.RESET_ALL)
                print(f"Stock actualizado Nuevo stock de {producto_agregar_stock} es: {stock_producto}")
            else:
                print("La cantidad debe ser mayor que cero.")
                agregar_stock()
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "ingrese solo números enteros" + Style.RESET_ALL)
            agregar_stock()
    else:
        print(Fore.RED + Style.BRIGHT + "Producto no encontrado" + Style.RESET_ALL)
        agregar_stock()

def graficar_stock_productos():
    plt.figure(figsize=(12, 8))
    plt.bar(df['producto'], df['stock'], color='skyblue')
    plt.title('Inventario de Stock por Producto', fontsize=16)
    plt.ylabel('Cantidad en Stock')
    plt.xlabel('Productos')
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def graficar_por_categoria_venta():
    print("Generando gráfica de ventas totales por categoría...")
    categorias = ['Verduras', 'Carne', 'Jugo', 'Lácteos', 'Abarrotes', 'Limpieza']
    totales_ventas = (
        verduras_venta,
        carne_vetas,
        jugo_venta,
        lacteos_ventas,
        abarrotes_ventas,
        limpieza_venta
    )
    if sum(totales_ventas) == 0:
        print(Fore.YELLOW + "Aún no hay ventas para graficar." + Style.RESET_ALL)
        return
    plt.figure(figsize=(10, 6))
    colores = ['#4CAF50', '#FF5722', '#FFC107', '#03A9F4', '#9C27B0', '#795548']
    plt.bar(categorias, totales_ventas, color=colores)
    plt.title('Ventas Totales ($) por Categoría', fontsize=16)
    plt.ylabel('Total Vendido ($)')
    plt.xlabel('Categoría')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()    

def terminar_turno():
       print("--------------terminastes tu turno-------------")
       print(f"tus ventas fueron {venta_turno}")
       print(Fore.BLACK+"-"*40+Style.RESET_ALL)

def cambiar_de_usuario():
    entrada_trabajador()

def mostrar_productos():

    print(df[['producto','stock']])

def mostrar_precio():

    print(df[['producto','precios']])

def agregar_nuevo_producto():
    global df
    
    print(Fore.BLUE+"         AGREGAR UN NUEVO PRODUCTO            ")
    nombre_del_nuevo_producto=input("Ingresa el nombre del nuevo producto: ")
    if nombre_del_nuevo_producto in df["producto"].values :
        print(Fore.RED+Style.BRIGHT+" ESTE PRODUCTO YA ESTA ")
        return
    print
    print(Fore.GREEN+"                CATEGORIAS DISPONIBLES"+Style.RESET_ALL)
    print(Fore.GREEN+"  Verdura | Carne | Jugo | Lacteos | Abarrotes | Limpieza"+Style.RESET_ALL)
    categoria=input("ingrese su categoria: ")
    try:
        precio = float(input("Ingresa el precio: "))
        stock = int(input("Ingresa el stock inicial: "))
        if precio <= 0 or stock < 0:
            print(Fore.RED + "El precio debe ser positivo y el stock no puede ser negativo." + Style.RESET_ALL)
            return
    except ValueError:
        print(Fore.RED + "Error: Asegúrate de ingresar números válidos para precio y stock." + Style.RESET_ALL)
        return

    nuevo_registro = pandas.DataFrame({
            'producto': [nombre_del_nuevo_producto], 
            'categoria': [categoria],               
            'stock': [stock],                      
            'precios': [precio]                     
        })
    #crear una lista del producto
    
    df = pandas.concat([df, nuevo_registro], ignore_index=True)
    df.to_csv('iostockinventar.csv', index=False)
    #el index es para evitar el 0 en el archivo y el concat es para concatenar      

def gui_mostrar_texto(titulo, texto):
    win = tk.Toplevel()
    win.title(titulo)
    st = ScrolledText(win, width=80, height=20)
    st.pack(fill=tk.BOTH, expand=True)
    st.insert(tk.END, texto)
    st.config(state=tk.DISABLED)

def gui_mostrar_productos():
    texto = df[['producto','stock']].to_string(index=False)
    gui_mostrar_texto('Productos', texto)

def gui_mostrar_precios():
    texto = df[['producto','precios']].to_string(index=False)
    gui_mostrar_texto('Precios', texto)

def gui_agregar_stock():
    """Interfaz de inventario usando diálogos Tkinter. Diseñada para ejecutarse en el hilo principal."""
    global verduras_venta, carne_vetas, jugo_venta, lacteos_ventas, abarrotes_ventas, limpieza_venta, venta_turno, df
    cuenta = 0.0
    ticket_lines = []

    while True:
        # preguntar si desea vender
        continuar = messagebox.askyesno('Stock', '¿Deseas agregar un producto?')
        if not continuar:
            break
        categorias = [str(x) for x in df['categoria'].dropna().unique()]
        categorias_text = '\n'.join(categorias) if categorias else 'Sin categorías'
        categoria = simpledialog.askstring('Categoría', f'Categorías disponibles:\n{categorias_text}\n\nIngresa la categoría:')
        if not categoria:
            continue
        cat_norm = categoria.strip().lower()

        prod_df = df[df['categoria'].astype(str).str.lower().str.strip() == cat_norm]
        if prod_df.empty:
            prod_df = df[df['categoria'].astype(str).str.lower().str.contains(cat_norm)]
        if prod_df.empty:
            messagebox.showerror('Error', 'No hay productos para esa categoría')
            continue

        productos_text = '\n'.join([f"{r['producto']} (Stock: {r['stock']})" for _, r in prod_df.iterrows()])
        producto = simpledialog.askstring('Producto', f'Productos en {categoria}:\n{productos_text}\n\nIngresa el nombre exacto del producto:')
        if not producto:
            continue
        producto = producto.strip()

        # buscar producto (case-insensitive)
        match = df[df['producto'].astype(str).str.lower().str.strip() == producto.lower()]
        if match.empty:
            producto_title = producto.title()
            match = df[df['producto'] == producto_title]
        if match.empty:
            messagebox.showerror('Error', 'Producto no encontrado')
            continue

        prod_name = match.iloc[0]['producto']
        stock_actual = int(match.iloc[0]['stock'])
        cantidad = simpledialog.askinteger('Cantidad', f'Stock actual de {prod_name}: {stock_actual}\n¿Cuántas unidades desea agregar?', minvalue=1, maxvalue=1000000)
        if cantidad is None:
            continue
            # actualizar stock
        df.loc[df['producto'] == prod_name, 'stock'] += cantidad
        df.to_csv(stocksito, index=False)

        messagebox.showinfo('Stock actualizado', f'Nuevo stock de {prod_name}' )
     
def gui_agregar_nuevo_producto():
    global df
    nombre = simpledialog.askstring('Nuevo producto', 'Nombre del producto:')
    if not nombre:
        return
    nombre = nombre.strip().title()
    if nombre in df['producto'].values:
        messagebox.showerror(Style.BRIGHT+Fore.RED+'Error', 'Este producto ya existe'+Style.RESET_ALL)
        return
    categoria = simpledialog.askstring('Nuevo producto', 'Categoria:')
    try:
        precio = simpledialog.askfloat('Nuevo producto', Style.NORMAL+Fore.BLACK+'Precio:'+Style.RESET_ALL)
        stock = simpledialog.askinteger('Nuevo producto', 'Stock inicial:', minvalue=0)
    except Exception:
        messagebox.showerror('Error', 'Valores inválidos')
        return
    if precio is None or stock is None:
        return
    nuevo = pandas.DataFrame({'producto':[nombre], 'categoria':[categoria], 'stock':[stock], 'precios':[precio]})
    df = pandas.concat([df, nuevo], ignore_index=True)
    df.to_csv(stocksito, index=False)
    messagebox.showinfo('Éxito', f'Producto {nombre} agregado')

def gui_abrir_cli():
    # Ejecuta la interfaz CLI en un hilo para no bloquear la GUI.
    # Force CLI mode so we don't call tkinter dialogs from a worker thread.
    t = threading.Thread(target=lambda: entrada_trabajador(force_cli=True), daemon=True)
    t.start()

def gui_show_menu():
    win = tk.Toplevel()
    win.title('Menú - Usuario')
    frm = tk.Frame(win)
    frm.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    b1 = tk.Button(frm, text='Mostrar productos', width=18, command=gui_mostrar_productos)
    b1.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    b2 = tk.Button(frm, text='Mostrar precios', width=18, command=gui_mostrar_precios)
    b2.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
    def venta_thread():
        # Usar interfaz de venta basada en diálogos (se ejecuta en hilo principal)
        venta_producto()
    b3 = tk.Button(frm, text='Venta de producto', width=18, command=venta_thread)
    b3.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

    def solicitar_admin_y_agregar():
        try:
            filtro = simpledialog.askinteger('Administrador', 'Ingrese UID del Administrador:')
        except Exception:
            filtro = None
        if filtro == 171007:
            gui_agregar_stock()
        else:
            messagebox.showerror('Error', 'UID de administrador inválido')

    b4 = tk.Button(frm, text='Agregar stock (admin)', width=18, command=solicitar_admin_y_agregar)
    b4.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

    b5 = tk.Button(frm, text='Graficar stock', width=18, command=graficar_stock_productos)
    b5.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
    b6 = tk.Button(frm, text='Graficar ventas', width=18, command=graficar_por_categoria_venta)
    b6.grid(row=1, column=2, padx=5, pady=5, sticky='ew')

    def terminar():
        messagebox.showinfo('Turno', f'Terminas tu turno. Ventas realizadas: {venta_turno}')
        win.destroy()

    b7 = tk.Button(frm, text='Terminar turno', width=18, command=terminar)
    b7.grid(row=2, column=0, padx=5, pady=10, sticky='ew')

    def cambiar_usuario():
        win.destroy()
        entrada_trabajador()

    b8 = tk.Button(frm, text='Cambiar usuario', width=18, command=cambiar_usuario)
    b8.grid(row=2, column=1, padx=5, pady=10, sticky='ew')

def agregar_empleado_thread():
    """
    Versión mejorada que usa diálogos tkinter en lugar de input/print.
    Compatible con GUI y CLI.
    """
    try:
        gui_active = tk._default_root is not None
    except Exception:
        gui_active = False
    
    if gui_active:
        # Usar interfaz gráfica con tkinter (no crear hilos que llamen a diálogos)
        resultado = messagebox.askyesno('Agregar empleado', '¿Deseas agregar un nuevo empleado?', parent=tk._default_root)
        if not resultado:
            messagebox.showinfo('Cancelado', 'Operación cancelada por el usuario', parent=tk._default_root)
            return
        try:
            empleados.agregar_nuevo_empleado(parent=tk._default_root)
            messagebox.showinfo('Éxito', 'Empleado agregado correctamente', parent=tk._default_root)
        except Exception as e:
            messagebox.showerror('Error', f'Error al agregar empleado: {str(e)}', parent=tk._default_root)
    else:
        # Interfaz CLI (para fallback)
        agregar_empleado = input("desea agregar un empleado? si/no: ").strip().lower()
        if agregar_empleado == "si":
            try:
                empleados.agregar_nuevo_empleado()
                print(Fore.GREEN + Style.BRIGHT + "EMPLEADO AGREGADO CON EXITO" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"Error: {str(e)}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + Style.BRIGHT + "OPERACION CANCELADA POR EL USUARIO" + Style.RESET_ALL)

def eliminar_empleado_thread():
    """
    Interfaz mejorada para eliminar empleados.
    Compatible con GUI y CLI.
    """
    try:
        gui_active = tk._default_root is not None
    except Exception:
        gui_active = False
    
    if gui_active:
        # Usar interfaz gráfica: pedir UID y eliminar sin bloquear la GUI
        resultado = messagebox.askyesno('Eliminar empleado', '¿Deseas eliminar un empleado?', parent=tk._default_root)
        if not resultado:
            messagebox.showinfo('Cancelado', 'Operación cancelada', parent=tk._default_root)
            return
        uid = simpledialog.askstring('Eliminar empleado', 'UID del empleado a eliminar:', parent=tk._default_root)
        if not uid:
            return
        uid = str(uid).strip()
        try:
            if uid == '171007':
                messagebox.showerror('Error', 'No se puede eliminar el administrador', parent=tk._default_root)
                return
            if uid in empleados.trabajadores_uid:
                del empleados.trabajadores_uid[uid]
                empleados.guardar_empleados_csv()
                messagebox.showinfo('Éxito', f'Empleado {uid} eliminado correctamente', parent=tk._default_root)
            else:
                messagebox.showerror('Error', 'UID no encontrado', parent=tk._default_root)
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar empleado: {str(e)}', parent=tk._default_root)
    else:
        # Interfaz CLI (para fallback)
        resultado = input("¿Deseas eliminar un empleado? (si/no): ").strip().lower()
        if resultado == "si":
            try:
                empleados.eliminar_nuevo_empleado()
                print(Fore.GREEN + Style.BRIGHT + "EMPLEADO ELIMINADO CON EXITO" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"Error: {str(e)}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + Style.BRIGHT + "OPERACION CANCELADA" + Style.RESET_ALL)

def launch_tkinter_gui():
    root = tk.Tk()
    root.title('Interfaz - HUEVOS CORP')
    root.geometry('480x320')
    # --- Login frame (visible al inicio) ---
    login_frame = tk.Frame(root)
    login_frame.pack(padx=10, pady=10, fill=tk.BOTH)

    tk.Label(login_frame, text='Ingrese su UID:', font=('Arial', 12)).grid(row=0, column=0, sticky='w')
    uid_entry = tk.Entry(login_frame, width=25, font=('Arial', 12))
    uid_entry.grid(row=0, column=1, padx=5, pady=5)

    info_label = tk.Label(login_frame, text='', fg='green')
    info_label.grid(row=1, column=0, columnspan=2, sticky='w')

    # --- Main menu frame (oculto hasta login exitoso) ---
    frame = tk.Frame(root)

    # Arrange buttons in 3 columns (create but don't pack the frame yet)
    btn_products = tk.Button(frame, text='Mostrar productos', width=18, bg="#C5E8F3",command=gui_mostrar_productos)
    btn_products.grid(row=0, column=0, padx=5, pady=5, sticky='ew',)

    btn_prices = tk.Button(frame, text='Mostrar precios', width=18,bg="#C5E8F3", command=gui_mostrar_precios)
    btn_prices.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    btn_add_stock = tk.Button(frame, text='Agregar stock', width=18,bg="#C5E8F3", command=gui_agregar_stock)
    
    btn_add_stock.grid(row=0, column=2, padx=5, pady=5, sticky='ew')

    btn_plot_stock = tk.Button(frame, text='Graficar stock', width=18,bg="#C5E8F3", command=graficar_stock_productos)
    
    btn_plot_stock.grid(row=1, column=1, padx=5, pady=5, sticky='ew')


    btn_add_product = tk.Button(frame, text='Agregar nuevo producto', width=18,bg="#F0C2EC",command=gui_agregar_nuevo_producto)
    btn_add_product.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
    # Botones de empleados (solo admin)
    btn_add_employee = tk.Button(frame, text='Agregar empleado', width=18,bg="#F0C2EC", command=agregar_empleado_thread)
    btn_add_employee.grid(row=2, column=0, padx=5, pady=10, sticky='ew')
    
    btn_delete_employee = tk.Button(frame, text='Eliminar empleado', width=18, bg="#F0C2EC",command=eliminar_empleado_thread)
    btn_delete_employee.grid(row=2, column=1, padx=5, pady=10, sticky='ew')

    btn_venta = tk.Button(frame, text='Venta de producto', width=18, bg="#9EC0FE",command=venta_producto)
    btn_venta.grid(row=2, column=2, padx=5, pady=10, sticky='ew')

    # CLI button spans all three columns
    btn_plot_sales = tk.Button(frame, text='Graficar ventas(categoria)', width=18,bg="#C5E8F3", command=graficar_por_categoria_venta)
    btn_plot_sales.grid(row=1, column=2, padx=5, pady=5, sticky='ew')
    btn_graficar_venta_por_producto = tk.Button(frame, text='Graficar la ventas por productos', width=60,bg="#C5E8F3", command=graficar_venta_productos)
    btn_graficar_venta_por_producto.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky='ew')

    # cerrar sesión button
    def do_logout():
        frame.pack_forget()
        uid_entry.delete(0, tk.END)
        info_label.config(text='')
        login_frame.pack(padx=10, pady=10, fill=tk.BOTH)

    btn_logout = tk.Button(frame, text='Cerrar sesión', width=60,bg="#898989", command=do_logout)
    btn_logout.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky='ew')

    botones_admin = [btn_add_product, btn_add_employee, btn_delete_employee]

    def show_main(admin=False, nombre=None):
        # ocultar login y mostrar el menú
        login_frame.pack_forget()
        if nombre:
            info_label.config(text=f'Bienvenido {nombre}')
        # muestra las herramientas de admin
        for w in botones_admin:
            if admin:
                w.grid()
            else:
                w.grid_remove()
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def submit_uid():
        uid = uid_entry.get().strip()
        if uid == '171007':
            show_main(admin=True, nombre='Administrador')
        elif 'trabajadores_uid' in globals() and uid in trabajadores_uid:
            nombre = trabajadores_uid.get(uid, {}).get('nombre', 'Usuario')
            show_main(admin=False, nombre=nombre)
        else:
            messagebox.showerror('Error', 'UID inválido')
            uid_entry.delete(0,tk.END)

    btn_ingresar = tk.Button(login_frame, text='Ingresar', command=submit_uid)
    btn_ingresar.grid(row=0, column=2, padx=5)

    # 
    def on_enter(event):
        submit_uid()
    uid_entry.bind('<Return>', on_enter)

    root.mainloop()

launch_tkinter_gui()