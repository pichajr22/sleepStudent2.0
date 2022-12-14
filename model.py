import os
from keras.preprocessing import image
import matplotlib.pyplot as plt 
import numpy as np
from keras.utils.np_utils import to_categorical
import random,shutil
from keras.models import Sequential
from keras.layers import Dropout,Conv2D,Flatten,Dense, MaxPooling2D, BatchNormalization
from keras.models import load_model
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#Ubicar la ejecución en la carpeta actual del proyecto
print("UBICADO")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def generator(dir, gen=image.ImageDataGenerator(rescale=1./255), shuffle=True,batch_size=1,target_size=(24,24),class_mode='categorical' ):

    return gen.flow_from_directory(dir,batch_size=batch_size,shuffle=shuffle,color_mode='grayscale',class_mode=class_mode,target_size=target_size)

BS= 32
TS=(24,24)
train_batch= generator('data/train',shuffle=True, batch_size=BS,target_size=TS)
valid_batch= generator('data/test',shuffle=True, batch_size=BS,target_size=TS)
SPE= len(train_batch.classes)//BS
VS = len(valid_batch.classes)//BS
print(SPE,VS)
print("ADAWDADW")

img,labels= next(train_batch)
print("IMAGEN",img.shape)

model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='sigmoid', input_shape=(24,24,1)),
    MaxPooling2D(pool_size=(1,1)),
    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D(pool_size=(1,1)),
#32 filtros de convolución utilizados cada uno de tamaño 3x3
#again
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(1,1)),

 #Filtros de convolución 64 usados cada uno de tamaño 3x3
#elegir las mejores funciones a través de la agrupación
    
#enciende y apaga aleatoriamente las neuronas para mejorar la convergencia
    Dropout(0.25),
#usamos Flatten ya que demasiadas dimensiones, solo queremos una salida de clasificación
    Flatten(),
#Obteniendo datos relavantes
    Dense(128, activation='relu'),
    Dropout(0.5),
#Usamos softmax para la matriz en probabilidades de salida
    Dense(4, activation='softmax')
    
])
print("ENTRENANDO")
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
print("ENTRENANDOo")
model.fit_generator(train_batch, validation_data=valid_batch,epochs=15,steps_per_epoch=SPE ,validation_steps=VS)
print("ENTRENANDOssss")
model.save('models/CNNdeteccion.h5', overwrite=True)