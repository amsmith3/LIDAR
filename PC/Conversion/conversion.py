import numpy as np
import os
import time


class Conversion:

    @staticmethod
    def get_cart_coordinates():

        def pol2cart(r, theta, phi):
            x = r * np.cos(phi) * np.cos(theta)
            y = r * np.cos(phi) * np.sin(theta)
            z = r * np.sin(phi)
            # x = r * np.sin(phi) * np.cos(theta)
            # y = r * np.sin(phi) * np.sin(theta)
            # z = r * np.cos(phi)
            return int(x), int(y), int(z)

        while not os.path.exists('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/polar_coordinates.txt'):
            continue

        time.sleep(60)

        with open('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/polar_coordinates.txt') as file:
            coordinate_list = file.read().splitlines()

            while not coordinate_list:
                coordinate_list = file.read().splitlines()

            print('Starting Conversion')

            f = open('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/cart_cord.txt', 'w')
            for cord in coordinate_list:
                polar_cord = cord.split(" ")

                r = int(polar_cord[0])
                theta = float(polar_cord[2]) * 3.1415 / 180
                phi = float(polar_cord[1]) * 3.1415 / 180

                cart = pol2cart(r, theta, phi)

                string = str(cart[0]) + ' ' + str(cart[1]) + ' ' + str(cart[2]) + '\n'

                f.write(string)

            f.close()
