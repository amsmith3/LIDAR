import numpy as np


def pol2cart(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


with open('cordinates.txt') as file:
    cordinate_list = file.read().splitlines()

    f = open('cart_cord.txt', 'w')
    for cord in cordinate_list:
        polar_cord = cord.split(" ")

        theta = int(polar_cord[0])
        r = int(polar_cord[1])
        z = int(polar_cord[2])

        cart = pol2cart(r, theta)

        string = str(cart[0]) + ' ' + str(cart[1]) + ' ' + str(z) + '\n'

        f.write(string)

    f.close()
