# 空域滤波器
---
   自动化钱61 柴嘉骏 2160405071
# 1. 低通滤波器
<br>分别使用高斯滤波器和中值滤波器平滑测试图像，并改变模板大小观察模板大小对于模糊效果的影响，测试的结果如下图所示</br>
## 1.1 Gaussian Filter
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test1_gaussian_3.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test1_gaussian_5.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test1_gaussian_7.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure1.1 Test1 Filted by Gaussian Filter </div>
<br></br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test2_gaussian_3.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test2_gaussian_5.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test2_gaussian_7.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure1.2 Test2 Filted by Gaussian Filter </div>
<br>上图中从左至右是由模板大小分别为3、5、7的高斯滤波器进行平滑处理后得到的图像，可以看到高斯滤波器的平滑效果就像“近视”一样，将图像的边缘信息进行模糊处理，但是对图像中存在的噪声并没有很好地解决。</br>

## 1.2 Median Filter
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test1_median_3.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test1_median_5.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test1_median_7.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure1.1 Test1 Filted by Median Filter </div>
<br></br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test2_median_3.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test2_median_5.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task6/test2_median_7.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure1.2 Test2 Filted by Median Filter </div>
<br>上图中从左至右是由模板大小分别为3、5、7的高斯滤波器进行平滑处理后得到的图像，图像经过中值滤波器的处理之后能够很好的将一些噪声去除掉，但是相应的，图像原本的信息也被模糊掉，图像的边缘严重模糊失真。</br>

<br>综上所述，高斯滤波器能够实现模糊图像的功能但是对于较大的噪声无能为力，而中值滤波器虽能滤除一定的噪声但是使得源图像信息严重失真。但是规律相同的是，随着模板大小的增加，滤波器的模糊效果也越来越好。</br>

# 2. 生成高斯滤波器
<br>利用固定方差 sigma=1.5产生高斯滤波器，模板大小分别选为3、5、7，处理的结果如下所示：</br>

<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task7/test1_gaussian_3.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task7/test1_gaussian_5.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task7/test1_gaussian_7.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure2 Test1 Filted by Gaussian Filter </div>

# 3. 高通滤波器
<br>本部分使用多种高通滤波器对图像进行测试，高通滤波器将会滤除掉图像中像素灰度值变化缓慢的部分，换句话说就是进行边缘检测。具体的方法包括：Unsharp Masking、Sobel Edge Detector、 Laplace Edge Detector 和 Canny Algorithm。</br>
## 3.1 Unsharp Masking
<br>非锐化掩蔽操作的步骤是先对原图像进行模糊处理，再将原图像减去模糊图像后得到的模板与原图像相加。非锐化掩蔽能够通过对原图像的模糊得到其边缘信息，并通过储存边缘信息的非锐化模板实现锐化操作。由于需要对原图像进行模糊处理，因此模糊使用的滤波器也将影响非锐化掩蔽的效果，在本次测试中使用了大小为5\*5的模板且\sigma=3，得到的结果如下图所示：</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_mask.jpg?raw=True" width="40%" height="40%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_mask.jpg?raw=True" width="40%" height="40%"/>
</div>
<div align="center"> Figure3.1 Unsharp Masking </div>

## 3.2 Sobel Edge Detector
<br>简单来讲，Sobel算子是对图像进行偏微分操作以达到边缘检测的目的，因此本次测试分别对图像的x方向和y方向进行Sobel边缘检测，在得到结果后发现效果并不理想，便对两幅边缘图像进行加和处理得到了效果更好的边缘检测结果。得到的结果如下图所示：</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_sobelx.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_sobely.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_sobel.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure3.2 Sobel Edge Detector for test3 </div>
<br></br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_sobelx.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_sobely.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_sobel.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure3.3 Sobel Edge Detector for test4 </div>
<br>以上图像从左至右分别是对图像的x方向和y方向进行Sobel边缘检测和二者加和的结果。</br>

## 3.3 Laplace Edge Detector
<br>与Sobel算子类似，Laplace算子是图像的二阶微分，而且是各向同性的滤波器，其响应与图像的突变方向无关。得到的结果如下图所示：</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_laplacian.jpg?raw=True" width="40%" height="40%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_laplacian.jpg?raw=True" width="40%" height="40%"/>
</div>
<div align="center"> Figure3.4 Sobel Edge Detector </div>

## 3.4 Canny Edge Detector
<br>Canny 的目标是找到一个最优的边缘检测算法，最优边缘检测的含义是：</br>
<br>(1)最优检测：算法能够尽可能多地标识出图像中的实际边缘，漏检真实边缘的概率和误检非边缘的概率都尽可能小；</br>
<br>(2)最优定位准则：检测到的边缘点的位置距离实际边缘点的位置最近，或者是由于噪声影响引起检测出的边缘偏离物体的真实边缘的程度最小；</br>
<br>(3)检测点与边缘点一一对应：算子检测的边缘点与实际边缘点应该是一一对应。</br>
<br>为了满足这些要求 Canny 使用了变分法（calculus of variations），这是一种寻找优化特定功能的函数的方法。最优检测使用四个指数函数项表示，且非常近似于高斯函数的一阶导数。在本次测试中使用了不同的像素上下限对，分别为25-75, 50-100和100-200，得到的结果如下图所示：</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_canny_25-75.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_canny_50-100.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test3_canny_100-200.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure3.5 Canny Edge Detector for test3 </div>
<br></br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_canny_25-75.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_canny_50-100.jpg?raw=True" width="30%" height="30%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task8/test4_canny_100-200.jpg?raw=True" width="30%" height="30%"/>
</div>
<div align="center"> Figure3.6 Canny Edge Detector for test4 </div>

<br>  根据上面的处理结果可以看到，随着上下限区间的不断增大，图像的细节变得越来越少，这是因为本算法将这些微小的像素变化视作不明显变化，不足以成为图像的边缘。</br>

# 4. 总结
<br>以上是本次实验的全部结果，本次实验的主要内容是使用空域滤波器对图像进行处理。其中低通滤波器对图像实现了模糊处理，而高通滤波器则实现了图像的边缘检测。在边缘检测的问题上，边缘检测主要依赖于图像的梯度信息，只是停留在图像的空域部分便能够得到很好的结果，对图像的频域处理应当会有更加出色的效果。</br>
