import paramiko
from PC.Network.tcp_recieve import TCP_Recieve

class Start():

    @staticmethod
    def start():

        ssh_client =paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='amsmith',username='pi',password='password')
        stdin,stdout,stderr=ssh_client.exec_command('python3 /home/pi/LIDAR/Raspberry\ Pi/Network/tcp_send.py')
        TCP_Recieve.get_file()

        # print(type(stdin))
