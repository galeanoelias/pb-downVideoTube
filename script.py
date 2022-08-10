import pytube

try:

    url_download = str(input('Ingrese URL del video a descargar/ Enter URL of the download video: '))
    video = pytube.YouTube(url_download)

    for i in video.streams:
        print('Itag{}, | Formato: {} | Resolucion: {} '.format(i.itag,i.mime_type,i.resolution))

    itag = int(input('Digita el tag: '))
    video.streams.get_by_itag(itag)
    video.streams.first().download()

except:
    print("Error al descargar/ Error of download")