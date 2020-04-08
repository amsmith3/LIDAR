import numpy as np
import os


class Conversion:

    @staticmethod
    def get_cart_coordinates():

        def pol2cart(r, theta):
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return x, y



        while not os.path.exists('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/polar_coordinates.txt'):
            continue

        with open('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/polar_coordinates.txt') as file:
            coordinate_list = file.read().splitlines()

            while not coordinate_list:
                coordinate_list = file.read().splitlines()

            print('Starting Conversion')

            f = open('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/cart_cord.txt', 'w')
            for cord in coordinate_list:
                polar_cord = cord.split(" ")

                theta = int(polar_cord[0])
                r = int(polar_cord[1])
                z = int(polar_cord[2])

                cart = pol2cart(r, theta)

                string = str(cart[0]) + ' ' + str(cart[1]) + ' ' + str(z) + '\n'

                f.write(string)

            f.close()
