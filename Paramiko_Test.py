import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username= user, password= passwd)
	ssh_session = client.get_transport().open_session()

	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024)

	return

def ssh_command_withKey(ip, user, key, command):
	client = paramiko.SSHClient()
	client.load_host_keys(key)
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username= user)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024)

	return

#ssh_command_withKey('192.168.1.94','username','/Users/ComputerName/.ssh/known_hosts','ls -a')

#ssh_command('192.168.1.94','username','password','ls -a')