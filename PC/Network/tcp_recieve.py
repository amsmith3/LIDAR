import socket

class TCP_Recieve():

    @staticmethod
    def get_file():

        s = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        # host = 'pi@amsmith'
        print(type(host))
        port = 12345  # Reserve a port for your service.
        s.bind((host, port))  # Bind to the port
        f = open('test.txt', 'wb')
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
                # print(f.read())
                l = c.recv(1024)
            f.close()
            print("Done Receiving")
            # s.shutdown(socket.SHUT_WR)
            # c.send('Thank you for connecting')
            c.close()  # Close the connection
            quit()
