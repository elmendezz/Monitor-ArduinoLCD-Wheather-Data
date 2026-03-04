import time
import serial
import psutil   
import requests 
# Para Usarse Necesitas Hacer "pip install psutil requests pyserial"

# --- CONFIGURACIÓN ---
PUERTO = 'COM#' 
BAUD = 9600

# Tecate
URL_CLIMA = "https://api.open-meteo.com/v1/forecast?latitude=32.56&longitude=-116.63&current_weather=true"

# Variables para controlar tiempos
ultimo_check_clima = 0
texto_clima = "Cargando..."

def obtener_clima():
    try:
        r = requests.get(URL_CLIMA, timeout=5).json()
        temp = r['current_weather']['temperature']
        return f"Tecate: {temp}C"
    except:
        return "Tecate: Err"

def formato_velocidad(bytes_sec):
    # Convierte números ilegibles a KB o MB legibles
    if bytes_sec < 1024:
        return f"{bytes_sec}B"
    elif bytes_sec < 1024 * 1024:
        return f"{bytes_sec/1024:.0f}KB"
    else:
        return f"{bytes_sec/(1024*1024):.1f}MB"

try:
    print(f"🔌 Conectando a {PUERTO}...")
    arduino = serial.Serial(PUERTO, BAUD, timeout=1)
    time.sleep(2)
    print("✅ Sistema Iniciado. Abre algo para ver cómo suben los números de Carga Y Descarga De Datos.")

    # Lectura inicial de datos
    net_old = psutil.net_io_counters()
    
    while True:
        # 1. ACTUALIZAR CLIMA CADA 60 SEGUNDOS / UN MINUTO
        if time.time() - ultimo_check_clima > 60:
            texto_clima = obtener_clima()
            ultimo_check_clima = time.time()

        # 2. CALCULAR VELOCIDAD DE INTERNET
        time.sleep(1)
        net_new = psutil.net_io_counters()
        
        # Restamos lo nuevo menos lo viejo = Bytes por segundo
        bytes_bajada = net_new.bytes_recv - net_old.bytes_recv
        bytes_subida = net_new.bytes_sent - net_old.bytes_sent
        
        # Actualizamos la referencia para la siguiente vuelta
        net_old = net_new
        
        # Formateamos (Ejemplo : "D:5.2MB U:0.1MB")
        vel_bajada = formato_velocidad(bytes_bajada)
        vel_subida = formato_velocidad(bytes_subida)
        texto_red = f"D:{vel_bajada} U:{vel_subida}"

        # 3. ENVIAR AL ARDUINO
        mensaje = f"#{texto_clima}|{texto_red}\n"
        arduino.write(mensaje.encode())
        
        print(f"Enviando: {texto_clima} | {texto_red}")

except serial.SerialException:
    print("❌ Error: Arduino desconectado.")
except KeyboardInterrupt:
    if 'arduino' in locals() and arduino.is_open:
        arduino.close()
