import yt_dlp
import os

def descargar_video():
    # Solicitar URL del video
    url = input("Introduce la URL del video de YouTube: ").strip()  # Quitar espacios en blanco
    
    # Solicitar nombre del archivo
    nombre_archivo = input("¿Cómo quieres llamar al archivo? (sin extensión): ").strip()

    # Establecer la ruta de descarga
    ruta_descarga = "C:\Users\joeli\OneDrive - Instituto Tecnológico de Las Américas (ITLA)\Documentos\Paginas wbs\Suplidor de Medicamentos e instrumentos\Pagina2\img\Videos"

    # Verificar si la ruta existe
    if not os.path.exists(ruta_descarga):
        print(f"La ruta {ruta_descarga} no existe. Por favor, verifica que la ruta es correcta.")
        return

    # Configuración de opciones para yt-dlp
    opciones = {
        'format': 'bestvideo[ext=mp4]',  # Descargar el mejor video en formato mp4
        'outtmpl': os.path.join(ruta_descarga, f"{nombre_archivo}.%(ext)s"),  # Ruta de salida
    }

    try:
        # Descargar el video
        with yt_dlp.YoutubeDL(opciones) as ydl:
            print(f"Descargando: {url}")
            ydl.download([url])
        
        print("Descarga completada!")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    descargar_video()
