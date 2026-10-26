from __future__ import unicode_literals
import yt_dlp
import time

def insertar_link():
    while True:
        link = input("Insereix Link: ").strip()
        if link:
            return link
        print("No has posat cap enllaç, si us plau torna a posar el link")
        print("")
        time.sleep(1)

link = insertar_link()


print("Quin format vols descarregar?")
print("")
print("1. MP3")
print("2. MP4")

opcio = input("Nomes hi pots escollir 1 o 2:  ").strip()

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
}

if opcio == '1':
    ydl_opts.update({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  
        }]
    })

    format_escollit = "MP3"

elif opcio == '2':
    ydl_opts.update({
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
    })
    format_escollit = "MP4"

try:
    print("Descarregant...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)
        print("Descarrega finalitzada")
except:
    print("Error, no s'ha pogut descargar bro")