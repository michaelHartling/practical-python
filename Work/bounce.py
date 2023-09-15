# bounce.py
#
# Exercise 1.5
counter = 1
height = 100
bounce_back_rate = 0.6
bounce_back_height = 0

while counter <= 10:
    bounce_back_height = height * bounce_back_rate
    print(counter, round(bounce_back_height,4))
    height = bounce_back_height
    counter += 1
