import paramiko
from PC.Conversion.conversion import Conversion


class Start:

    @staticmethod
    def start():
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='amsmith', username='pi', password='password')
        # ssh_client.exec_command('cd test; rm stop.txt')
        stdin, stdout, stderr = ssh_client.exec_command('cd LIDAR/RaspberryPi; python3 blink.py')
        stdin.close()

        Conversion.get_cart_coordinates()

        for line in stdout.read().splitlines():
            print(line)

