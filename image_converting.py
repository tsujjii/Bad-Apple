import cv2
import numpy as np

def calc_symbol(num_of_white: int, num_of_pixels: int) -> int:
    for i in range(10):
        if (i + 1) * num_of_pixels / 10 >= num_of_white:
            return i

def get_list(path: str, columns: int, rows: int) -> str:
    # Símbolos de brilho correspondentes a diferentes níveis de intensidade
    brightness_tuple = (' ', '*', '#', 'M', 'W', '8', '$', '&', '%', '@')

    # Lê a imagem e converte para escala de cinza
    image = cv2.imread(path, 0)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Dimensões da imagem
    height, width = image.shape

    # Calcula a altura e largura de cada bloco com base no número de linhas e colunas
    block_height, block_width = height // rows, width // columns
    block_pixels = block_height * block_width  # Número total de pixels em um bloco

    out = ''
    
    # Pré-compute as coordenadas de corte
    h_slices = [slice(i * block_height, (i + 1) * block_height) for i in range(rows)]
    w_slices = [slice(j * block_width, (j + 1) * block_width) for j in range(columns)]

    for i in range(rows):
        for j in range(columns):
            # Slice usando NumPy para evitar chamadas repetidas de OpenCV
            block = image[h_slices[i], w_slices[j]]

            # Calcula o número de pixels brancos no bloco
            count_non_zero = np.count_nonzero(block)

            # Obtém o símbolo de brilho correspondente ao bloco atual
            out += brightness_tuple[calc_symbol(count_non_zero, block_pixels)]

    return out
