import cv2
import numpy as np
import re
import matplotlib.pyplot as plt


r = r'\.[a-zA-Z0-9]+'


def spatial_filter(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/fourth/{}'.format(image_name)
    image = cv2.imread(image_path)
    global r
    image_name = re.sub(r, '', image_name)
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Median filtering
    plt.figure('Spatial Filter')
    plt.title('Sptial Filter')
    img_median_3 = cv2.medianBlur(image, 3)
    img_median_5 = cv2.medianBlur(image, 5)
    img_median_7 = cv2.medianBlur(image, 7)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task6/{}_median_3.jpg'.format(image_name),
                img_median_3)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task6/{}_median_5.jpg'.format(image_name),
                img_median_5)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task6/{}_median_7.jpg'.format(image_name),
                img_median_7)

    # Gaussian Filtering
    img_gassian_3 = cv2.GaussianBlur(image, (3, 3), 0)
    img_gassian_5 = cv2.GaussianBlur(image, (5, 5), 0)
    img_gassian_7 = cv2.GaussianBlur(image, (7, 7), 0)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task6/{}_gaussian_3.jpg'.format(image_name),
                img_gassian_3)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task6/{}_gaussian_5.jpg'.format(image_name),
                img_gassian_5)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task6/{}_gaussian_7.jpg'.format(image_name),
                img_gassian_7)

def gassian_filter(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/fourth/{}'.format(image_name)
    image = cv2.imread(image_path)
    global r
    image_name = re.sub(r, '', image_name)
    img_gassian_3 = cv2.GaussianBlur(image, (3, 3), 1.5)
    img_gassian_5 = cv2.GaussianBlur(image, (5, 5), 1.5)
    img_gassian_7 = cv2.GaussianBlur(image, (7, 7), 1.5)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task7/{}_gaussian_3.jpg'.format(image_name),
                img_gassian_3)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task7/{}_gaussian_5.jpg'.format(image_name),
                img_gassian_5)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task7/{}_gaussian_7.jpg'.format(image_name),
                img_gassian_7)

def high_past_filter(image_name):
    image_path = '/home/hero/Documents/DIP-Homework/Homework2/Requirement/fourth/{}'.format(image_name)
    image = cv2.imread(image_path)
    global r
    image_name = re.sub(r, '', image_name)
    # Unsharp Masking
    k = 1
    img_gassian = cv2.GaussianBlur(image, (3, 3), 1)
    gmask = cv2.subtract(image, img_gassian)
    gxy = cv2.add(image, k*img_gassian)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_mask.jpg'.format(image_name),
                gxy)

    # Sobel edge detector
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel = cv2.add(sobelx, sobely)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_sobelx.jpg'.format(image_name),
                sobelx)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_sobely.jpg'.format(image_name),
                sobely)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_sobel.jpg'.format(image_name),
                sobel)

    # Laplace edge detection
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_laplacian.jpg'.format(image_name),
                laplacian)

    # Canny Algorithm
    canny_25_75 = cv2.Canny(image, 25, 75, edges=5, L2gradient=True)
    canny_50_100 = cv2.Canny(image, 50, 100, edges=5, L2gradient=True)
    canny_100_200 = cv2.Canny(image, 100, 200, edges=5, L2gradient=True)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_canny_25-75.jpg'.format(image_name),
                canny_25_75)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_canny_50-100.jpg'.format(image_name),
                canny_50_100)
    cv2.imwrite('/home/hero/Documents/DIP-Homework/Homework2/Content/task8/{}_canny_100-200.jpg'.format(image_name),
                canny_100_200)


if __name__ == '__main__':
    # task6
    spatial_filter('test1.pgm')
    spatial_filter('test2.tif')

    # task7
    gassian_filter('test1.pgm')
    gassian_filter('test2.tif')

    # task8
    high_past_filter('test3.pgm')
    high_past_filter('test4.tif')

