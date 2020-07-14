import paramiko


class Paramiko_SSH():
     """Class connection on network nodes"""

     def __init__(self,host,user,secret,port,command):
          """Initialization basic variable and execute connection"""
          self.host = host
          self.user = user
          self.secret = secret
          self.port = port
          self.command = command
          try:
               self.client = paramiko.SSHClient()
               self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
               self.client.connect(hostname=self.host, username=self.user, password=self.secret, port=self.port)
          except Exception:
               print("Error connection to network nodes")
          else:
               print("Success connection to network nodes")
   
                 
     def execute(self):
          """Execute remote command"""
          try:
               stdin, stdout, stderr = self.client.exec_command( self.command )
               data = stdout.read() + stderr.read()
               datadecode = data.decode('utf-8')
               return datadecode
               
          except Exception:
               print("Error exec command!")
          else:
               print("Success exec command!")
               return datadecode

     def close_connect(self):
          """Close connectiom"""
          try:
               self.client.close()
          except Exception:
               print("Error close connection!")
          else:
               print("Success close connection!")
