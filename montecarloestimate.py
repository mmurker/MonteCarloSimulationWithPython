import random
iteration = 1000   
circlepoints = 0   #random number hitting the area under of the quarter circle 
squarepoints = 0  #random number hitting the area of the square

for i in range(iteration**2):
    x = random.random()
    y = random.random()
    cal_dimension = (x ** 2) + (y ** 2) 
    if cal_dimension <=1:
        circlepoints += 1
    squarepoints += 1

pi = 4*circlepoints/squarepoints

print(pi)