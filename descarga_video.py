from pytube import YouTube

# URL del video de YouTube que deseas descargar
url = "https://www.youtube.com/watch?v=4d3SpXumIRE"

# Crea un objeto YouTube
video = YouTube(url)

# Selecciona la mejor calidad disponible
stream = video.streams.get_highest_resolution()

# Descarga el video
stream.download()

print("Video descargado exitosamente.")
