from PIL import Image
import numpy as np
import cv2

# Transformando qualquer imagem em um quadrado com preenchimento preto
def get_square(image,square_size):
    height = image.shape[0]
    width = image.shape[1]
    if(height>width):
      differ=height
    else:
      differ=width
    differ+=4
    mask = np.zeros((differ,differ), dtype="uint8")   
    x_pos=int((differ-width)/2)
    y_pos=int((differ-height)/2)
    mask[y_pos:y_pos+height,x_pos:x_pos+width]=image[0:height,0:width]
    mask=cv2.resize(mask,(square_size,square_size),interpolation=cv2.INTER_AREA)
    return mask


# Para cortar a imagem quadrada em 3 faixas horizontais

def recort_t1(img, lista):
  img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
  altura = img2.shape[0] //3
  t1 = img2[:, (altura*2):(altura*3)]
  t1 = cv2.rotate(t1, cv2.ROTATE_90_COUNTERCLOCKWISE) 
  lista.append(t1)
  return lista

def recort_t2(img, lista):
  img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
  altura = img2.shape[0] //3
  t2 = img2[:, altura:(altura*2)]
  t2 = cv2.rotate(t2, cv2.ROTATE_90_COUNTERCLOCKWISE) 
  lista.append(t2)
  return lista

def recort_t3(img, lista):
  img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
  altura = img2.shape[0] //3
  t3 = img2[:, :altura]
  t3 = cv2.rotate(t3, cv2.ROTATE_90_COUNTERCLOCKWISE) 
  lista.append(t3)
  return lista


# Para cortar cada faixa horizontal em 3 blocos de tamanho igual

def bloco_1(img, lista_blocos):
  img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
  largura = img2.shape[0] //3 #100
  altura = img2.shape[1]
  p1 = img2[:largura, :altura]
  p1 = cv2.rotate(p1, cv2.ROTATE_90_COUNTERCLOCKWISE) 
  lista_blocos.append(p1)
  return lista_blocos

def bloco_2(img, lista_blocos):
  img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
  largura = img2.shape[0] //3 #100
  altura = img2.shape[1]
  p2 = img2[largura:(largura*2), :altura]
  p2 = cv2.rotate(p2, cv2.ROTATE_90_COUNTERCLOCKWISE) 
  lista_blocos.append(p2)
  return lista_blocos

def bloco_3(img, lista_blocos):
  img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
  largura = img2.shape[0] //3 #100
  altura = img2.shape[1]
  p3 = img2[(largura*2):(largura*3), :altura]
  p3 = cv2.rotate(p3, cv2.ROTATE_90_COUNTERCLOCKWISE) 
  lista_blocos.append(p3)
  return lista_blocos


# Corta uma imagem qualquer em 9 blocos (3x3) quadrados e retorna em lista

def corta3x3(img):
  img = get_square(img, 300)
  lista_faixas = []
  lista_blocos = []

  lista_faixas = recort_t1(img, lista_faixas)
  lista_faixas = recort_t2(img, lista_faixas)
  lista_faixas = recort_t3(img, lista_faixas)

  for i in range(3):
    lista_blocos = bloco_1(lista_faixas[i], lista_blocos)
    lista_blocos = bloco_2(lista_faixas[i], lista_blocos)
    lista_blocos = bloco_3(lista_faixas[i], lista_blocos)

  return lista_blocos


# Transformando uma lista de imagem cv2 para PIL
def cv2_to_PIL(lista_cv2):
  lista_PIL = []

  for i in range(len(lista_cv2)):
    imagem_cv2 = cv2.cvtColor(lista_cv2[i], cv2.COLOR_BGR2RGB)
    imagem_PIL = Image.fromarray(imagem_cv2)
    lista_PIL.append(imagem_PIL)

  return lista_PIL