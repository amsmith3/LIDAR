import paramiko


class Stop:

    @staticmethod
    def stop():
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='amsmith', username='pi', password='password')
        stdin, stdout, stderr = ssh_client.exec_command('touch LIDAR/RaspberryPi/stop.txt')

        for line in stdout.read().splitlines():
            print(line)
        # print(stdout.readlines())
