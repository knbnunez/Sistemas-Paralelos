from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from time import time


def convert_to_grayscale(image, gray):
    for x in range(H):
        for y in range(W):
            r, g, b = image[x][y]
            gray[x][y] = round((r+g+b)/3)
    return gray
    

if __name__ == '__main__':
    # No me fue posible hacerlo funcionar correctamente en un Foreach, no lograba terminar de calcular completo la imagen de 2000x1000
    # IMAGE_PATHS = ['image_500x500.jpg', 'image_2000x1000.jpg']
    
    # Comentar y descomentar la línea correspondiente
    # IMAGE_PATHS = ['image_500x500.jpg']
    IMAGE_PATHS = ['image_2000x1000.jpg']

    for ip in IMAGE_PATHS:
        init = time()
        
        image = Image.open(ip) # Leer y almacenar la imagen
        image = np.array(image) # Convertirlo a array
        H, W, _ = image.shape # Obtener el ancho y alto de la imagen
        gray = np.zeros((H, W), dtype=np.uint8) # Inicializar la matriz de la imagen en escala de grises
        gray = convert_to_grayscale(image, gray)
        
        end = time() - init

        print(f"Para {ip}, tiempo:", end)

        # Imagen original
        plt.imshow(image)
        plt.title('Imagen Original')
        plt.show()

        # Imagen en escala de grises
        plt.imshow(gray, cmap='gray')
        plt.title('Imagen en escala de grises')
        plt.show()