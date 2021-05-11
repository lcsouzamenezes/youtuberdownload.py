from pytube import YouTube
import moviepy.editor as mp
import os
import re

# Digite o link do vídeo e o local que deseja salvar o mp3 #
link = input("Digite o link do vídeo que deseja baixar, ex: https://www.youtube.com/watch?v=XUycW8u65Rc: ")
path = input("Digite o diretório que deseja salvar o vídeo: ")
youtube = YouTube(link)

# Começa o Download #
print("Baixando..")
youtube = youtube.streams.filter(only_audio=True).first().download(path)
print("Download completo!")

# Converte mp4 para mp3 #
print('Convertendo arquivo...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Sucesso!')
