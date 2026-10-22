from __future__ import unicode_literals
import yt_dlp

print("Insereix Link")
link = input("")
if not link:
    print("No has posat cap enllaç")

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
