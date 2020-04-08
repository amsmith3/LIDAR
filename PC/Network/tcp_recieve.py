import socket


class TCP_Recieve():

    @staticmethod
    def get_file():

        s = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        print(type(host))
        port = 12345  # Reserve a port for your service.
        s.bind((host, port))  # Bind to the port
        f = open('C:/Users/alexm/PycharmProjects/LIDAR/PC/Conversion/polar_coordinates.txt', 'wb')
        print(f)
        s.listen(5)  # Now wait for client connection.
        while True:
            c, addr = s.accept()  # Establish connection with client.
            print('Got connection from', addr)
            print("Receiving...")
            l = c.recv(1024)
            print(l)
            while l:
                print("Receiving...")
                f.write(l)
                l = c.recv(1024)
            f.close()
            print("Done Receiving")
            c.close()  # Close the connection

