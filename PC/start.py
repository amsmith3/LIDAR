import paramiko
from PC.Network.tcp_recieve import TCP_Recieve


class Start:

    @staticmethod
    def start():
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='amsmith', username='pi', password='password')
        # ssh_client.exec_command('cd test; rm stop.txt')
        stdin, stdout, stderr = ssh_client.exec_command('cd LIDAR/RaspberryPi1; python3 blink.py')
        stdin.close()

        for line in stdout.read().splitlines():
            print(line)

        # TCP_Recieve.get_file()
        # print(stdout.readlines())
