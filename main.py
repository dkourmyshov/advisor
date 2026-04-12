import math

database = [
  # Название, жанр, рейтинг, координаты embedding
  ["Harry Potter", "fantasy", 9, [1, 5]]
  ["Star Wars", "space opera", 8, [2, 3]]
]

print("Прототип поисковой системы")

print("Для поиска введите координаты x, y (числа от 1 до 10) через запятую:")
x, y = map(int, input().split(","))

min_distance = 20 # заведомо больше расстояния между любыми точками в квадрате 10x10
candidate = None # специальное значение, обозначающее отсутствие чего-либо

for current_item in database:
  current_distance = math.dist([x, y], current_item[3])
  if current_distance < min_distance:
      min_distance = current_distance
      candidate = current_item

print("Запись с координатами, ближайшими к заданной точке:")
print(candidate)
