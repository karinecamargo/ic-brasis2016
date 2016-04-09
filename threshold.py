import mnist
import numpy as np
import shutil 
import os
import gzip

mndata = mnist.MNIST('./Paloma/MNIST_data')
#X, y = mndata.load_training()
training, label = mndata.load_training()
testing = mndata.load_testing()

#reshaped = np.array(X[0]).reshape(28,28)
limiar = 1
while limiar < 255:
    novo_arq=[]
    for foto in training:
        nova_foto=[]
        #reshaped = np.array(foto).reshape(28,28)
        #print reshaped.shape
        for pixel in foto:
            if pixel < limiar :
                nova_foto.append(0)
            else:
                nova_foto.append(1)
        novo_arq.append(nova_foto)
    arquivo = open('./Paloma/threshold/'+ str(limiar) +'_threshold.txt', 'w')

    for linha in novo_arq:
        arquivo.writelines(str(linha).replace('[','').replace(']','')+'\n')
    arquivo.close()
    with open('./Paloma/threshold/'+ str(limiar) +'_threshold.txt', 'r') as f_in, gzip.open('./Paloma/threshold/'+ str(limiar) +'_threshold.txt.gz', 'w') as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove('./Paloma/threshold/'+ str(limiar) +'_threshold.txt')
    limiar+=1
    print limiar
