# Minimum Öklid Mesafesinin Hesaplanması.

import math

def euclidean_distance(point1, point2):

  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
  # Noktaları tanımlayalım.
  points = [(1, 2), (4, 5), (3, 1), (6, 7)]

  # Mesafeleri hesaplayın
  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclidean_distance(points[i], points[j])
      distances.append(distance)

  # Minimum mesafeyi bulmak için.
  min_distance = min(distances)

  # çıktıyı ekrana yazdıralım.
  print("Minimum Öklid mesafesi:", min_distance)

if __name__ == "__main__":
  main()