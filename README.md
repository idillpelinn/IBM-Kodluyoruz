# IBM-Kodluyoruz
The CyberStart program's second-week exercise, conducted in collaboration between IBM and Kodluyoruz.
# Öklid Mesafesi Hesaplama Programı

Resimdeki formül:
\[ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \]

Öklid mesafesi, Öklid uzayındaki iki nokta arasındaki "sıradan" düz çizgi mesafesidir. Bu formül ile, düzlemde veya üç boyutlu uzayda iki nokta arasındaki mesafeyi bulabilirsiniz.

## Göreviniz

Python'da fonksiyonlar ve döngüler kavramlarını kullanarak aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

### 1. Noktaların Tanımlanması

`points` adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, `(x, y)` noktası bir demet olarak `(x, y)` şeklinde temsil edilecektir.

### 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma

`euclideanDistance` adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

### 3. Mesafelerin Hesaplanması

Bir döngü kullanarak, `points` listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri `distances` adında başka bir listede saklayın.

### 4. Minimum Mesafenin Bulunması

`distances` listesinden minimum mesafeyi bulun ve yazdırın.

