import mnist
import numpy as np
from scipy import misc
import os

arquivo = open ('./Paloma/Filtro/covolution.txt', 'w')

mndata = mnist.MNIST('./Paloma/MNIST_data')
#X, y = mndata.load_training()
training, label = mndata.load_training()
testing = mndata.load_testing()
novo_arq=[]
final_arq=[]
cont=0
#pra cada foto na pasta de treino
for foto in training:
    nova_foto=[]
    foto=np.array(foto)
    #foto=foto.reshape((28,28))
    
    linha=[]
    for pixel in foto:
        #print pixel
        novo_pixel = 255 - pixel
        num_termometro= int(novo_pixel*10/255.0)
        termometro=[0,0,0,0,0,0,0,0,0,0]
        for i in range(num_termometro):
            termometro[i]=1
        linha += termometro
    #print len(linha)
    #print termometro

    final_arq.append(linha)

arquivo = open ('./Paloma/termometro', 'w')    

#pra cada foto dentro do arquivo final troca [ e ] por ''(vulgo nada)
for linha in final_arq:
    arquivo.writelines(str(linha).replace('[','').replace(']','')+'\n')

    arquivo.close()
