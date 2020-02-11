import paramiko


class Stop:

    @staticmethod
    def stop():
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='amsmith', username='pi', password='password')
        stdin, stdout, stderr = ssh_client.exec_command('touch test/stop.txt')
        print(stdout.readlines())
