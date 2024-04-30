from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from time import time


def convert_to_grayscale(image):
    H, W, _ = image.shape # Obtener el ancho y alto de la imagen
    gray = np.zeros((H, W), dtype=np.uint8) # Inicializar la matriz de la imagen en escala de grises
    for x in range(H):
        for y in range(W):
            r, g, b = image[x][y]
            gray[x][y] = round((r+g+b)/3)
    return gray
    

if __name__ == '__main__':
    # Comentar y descomentar la línea correspondiente
    # image_path = 'image_500x500.jpg'
    image_path = 'image_2000x1000.jpg'
    
    image = Image.open(image_path) # Leer y almacenar la imagen
    
    init = time()
    image = np.array(image) # Convertir imagen en matriz (arreglo de arreglos)
    gray = convert_to_grayscale(image)
    end = time() - init

    print(f"Para {image_path}, tiempo:", end)

    # Imagen original
    plt.imshow(image)
    plt.title('Imagen Original')
    plt.show()

    # Imagen en escala de grises
    plt.imshow(gray)
    plt.title('Imagen en escala de grises')
    plt.show()