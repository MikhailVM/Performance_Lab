import math


def check(circle, point):
  if math.sqrt((point[0] - circle[0])**2 + (point[1] - circle[1])**2) == circle[2]:
    print(0, '\n')
  elif math.sqrt((point[0] - circle[0])**2 + (point[1] - circle[1])**2) < circle[2]:
    print(1, '\n')
  else:
    print(2, '\n')


file_name1 = input('Введите имя файла с координатами окружности: ')
file_name2 = input('Введите имя файла с координатами точек: ')

circle_data = []
circle_file = open(file_name1, 'r')
for line in circle_file:
  temp = line.strip().split()
  for elem in temp:
    circle_data.append(float(elem))

points_data = []
point_file = open(file_name2, 'r')
for line in point_file:
  points_data.append([float(x) for x in line.split()])

for i_point in points_data:
  check(circle_data, i_point)
