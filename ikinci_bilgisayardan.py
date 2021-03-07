#2.olarak yolladığım scriptim olacak.
#basit bir şekilde 0 ile 1000 arasındaki sayılardan rastegele bir dizi oluşturup bunu sıralar.

import random

sirasiz= []
for sd in range(0,10):
    n=random.randint(0,100)
    sirasiz.append(n)

print(f" dizinin sırasız hali: \n {sirasiz} ")

siralı=[]
sirali=sorted(sirasiz)
print(f" dizinin sıralı hali: \n {sirali} ")
