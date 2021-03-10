from PIL import Image
from numpy.fft import fft2, fftshift
import matplotlib.pyplot as plt

import numpy as np

def calculate_psd(imgPath):
	srcIm = Image.open(imgPath).convert('L')
	# 图像的功率谱
	fd_Im = fftshift(fft2(srcIm))
	#FFT后，原点不在中心，通过fftshift将原点(DC)放在中心
	psd = abs(fd_Im) ** 2
	return psd


path = 'Bridson.jpg'
psd = calculate_psd(path)
# 通过对数变换，便于观察
psd = 10 * np.log10(psd)
psd[128,128] = 0 #去掉DC分量

plt.imshow(psd,cmap=plt.cm.gray)
plt.savefig('Bridson_spectrum.jpg')
plt.show()


path = 'Random.jpg'
psd = calculate_psd(path)
# 通过对数变换，便于观察
psd = 10 * np.log10(psd)
psd[128,128] = 00 #去掉DC分量

plt.imshow(psd,cmap=plt.cm.gray)
plt.savefig('Random_spectrum.jpg')
plt.show()
