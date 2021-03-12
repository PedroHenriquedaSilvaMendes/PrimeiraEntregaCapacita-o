import time
import winsound


espera = int(input('Forneça o tempo de espera: '))
qtd = int (input('Forneça quantas vezes o audio toca: '))
#som = str(input('Forneça o nome do audio: '))
som = 'audio_exercicio.wav'
def funcao (tempo, vezes):
    winsound.PlaySound(som, winsound.SND_FILENAME)
    time.sleep(tempo)
    for i in range(vezes):
        winsound.PlaySound(som, winsound.SND_FILENAME)

funcao(espera,qtd)
