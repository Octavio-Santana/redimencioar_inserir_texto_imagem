import os
import shutil
import cv2


def read_img(path_img):
    return cv2.imread(path_img)

def resize_img(img, resize=(512,512)):
    return cv2.resize(img, resize)

def marca_d_agua(img, img_a):
    return cv2.addWeighted(img, 0.7, img_a, 0.3, 0.0)

def save_image(img, filename):
    return cv2.imwrite(filename, img)

def run(path_dir, filename_d_agua):
    # Criar um novo diretprio com as imagens com marca d'água
    path_dir_dagua = f'{path_dir}_dagua'
    try:
        os.mkdir(path_dir_dagua)
    except:
        shutil.rmtree(path_dir_dagua)
        os.mkdir(path_dir_dagua)

    # Ler todas as imagens do diretorio
    img_list = os.listdir(path_dir)

    # Ler imagem que será a marca d'água
    img_a = cv2.imread(filename_d_agua)
    img_a = resize_img(img_a, resize=(512,512))

    for img_name in img_list:
        path_img = '/'.join([path_dir, img_name])
        img = read_img(path_img)
        img = resize_img(img, resize=(512,512))
        img_dagua = marca_d_agua(img, img_a)
        save_image(img_dagua, '/'.join([path_dir_dagua, img_name]))


if __name__ == '__main__':
    run(path_dir='imagens', filename_d_agua='logo.png')