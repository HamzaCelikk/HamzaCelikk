# Minimum Öklid Mesafesinin Hesaplanması.

import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]  

# Öklid Mesafesi için fonksiyon
def euclideanDistance(point1, point2):
#Öklid formülünü makinenin anlayacağı şekilde yazdık ( d = √(x₂-x₁)²+(y₂-y₁)² ).
  return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Mesafelerin hesaplanması(Bir boş liste ve iç içe for döngüsü oluşturduk).
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"En kısa Öklid mesafesi: {min_distance}")
