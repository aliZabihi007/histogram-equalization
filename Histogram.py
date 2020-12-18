import cv2 as cv
from matplotlib import pyplot as plt


# کلاس هستگرام تعریف میکنیم
class histogram:
    def __init__(self):
        self.count = []
        self.r = []

    # تعداد فراوانی های پیکسل را را حساب میکند  فراوانی بدست می آید
    def getImagePixel(self, image, row, col):
        for con in range(0, 256):
            print('%', round(con / 256, 2) * 100)
            self.r.append(con)
            num = 0
            for i in range(0, row):
                for j in range(0, col):
                    if (image[i, j] == con):
                        num += 1
            self.count.append(num)

        return (self.r, self.count)

    # نمودار تغییرات سطوح خاکستری را به صورت نمودار نشان میدهد
    def show(self, inten, number):
        plt.stem(inten, number)
        plt.xlabel('intensity value')
        plt.ylabel('number of pixels')
        plt.title('Histogram of the original image')
        plt.show()

    # histogram_stretching که باعث کشیده شدن نمودار می شود
    def histogram_stretching(self, image, Min, Max):
        constant = (Max - Min) / (image.max() - image.min())

        img_stretch = img * constant
        return img_stretch

    # histogram_shrink که باعث جمع شدن  تغییرات سطوح خاکستری می شود
    def histogram_shrink(self, image, Min, Max):
        constant = (Max - Min) / (image.max() - image.min())
        img2 = image - image.min()
        img_stretch = (img2 * constant) + Min
        return img_stretch

    # Histogram_Sliding مقادیر سطوح خاکستری در یک عدد ثابت جمع خواهد شد
    def Histogram_Sliding(self, image, number):
        return (image + number) % 256

    # شروع برنامه برای اجرا شدن


if __name__ == '__main__':
    reazult = 'Stretchedunnamed.png'
    hist = histogram()
    # read image
    img = cv.imread('unnamed.jpg', 0)

    roww, coll = img.shape

    intensity, numbers = hist.getImagePixel(image=img, row=roww, col=coll)
    hist.show(intensity, numbers)

    # select gray level and run algoritm

    # resultimage = hist.histogram_stretching(img, 0, 255)
    resultimage = hist.histogram_shrink(img, 30, 180)
    # resultimage = hist.Histogram_Sliding(img, 30)
    # ساختن تصویر
    cv.imwrite(reazult, resultimage)
