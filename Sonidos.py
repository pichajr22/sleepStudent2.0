import pygame,time

pygame.init()
sound= pygame.mixer.Sound('D:/University/Noveno Semestre/Minería de Datos/Proyecto/Drowsiness detection/alarm.wav')



nums = [4, 78, 9, 84]
for n in nums:
    print(n)
    sound.play()
    print("Reproduciendo")
    time.sleep(8)
    