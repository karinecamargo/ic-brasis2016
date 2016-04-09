import mnist
import numpy as np
from scipy import signal
from scipy import misc
import os
from matplotlib import pyplot as plt
import cv2

arquivo = open ('./Paloma/Filtro/covolution.txt', 'w')
#m = [[1,1,1],[1,-8,1],[1,1,1]]
m = [[0,-1,0],
	 [-1,4,-1],
	 [0,-1,0]]

mndata = mnist.MNIST('./Paloma/MNIST_data')
#X, y = mndata.load_training()
training, label = mndata.load_training()
testing = mndata.load_testing()
novo_arq=[]
final_arq=[]
cont=0
#pra cada foto na pasta de treino

for image in training:
	image=np.array(image)
	image=image.reshape((28,28))
	

	conved_image = signal.convolve2d(image, m, boundary='symm', mode='same')
	new_image = []
	for line in conved_image:
		for pixel in line:
			if(pixel < 0):
				new_image.append(1)
			else:
				new_image.append(0)
	new_image = np.array(new_image)
	# new_image = new_image.reshape((28,28))

	
	# for linha in image:
	# 	for pixel in linha:
	# 		print "%2d" %(pixel/10.0),
	# 	print 

	# print "-"*20
	# print new_image
	#cv2.imshow('image',image)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
	
	# imgplot = plt.imshow(new_image,cmap=plt.cm.binary)
	# plt.plot("teste", imgplot)
	# plt.show()
	
	

	#exit(0)
	#coloca a foto que foi filtrada e binarizada no arquivo final
	#final_arq.append(nova_foto)
	new_image = list(new_image)
	new_image = str(new_image)
	arquivo.write(new_image.replace('[','').replace(']','')+'\n')
	if cont%1000==0:
		arquivo.flush()
	print 'li' + str(cont) + 'fotos'
	cont +=1


arquivo.close()
