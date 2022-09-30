# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 19:06:22 2021

@concurrent Server
"""
import socket 
import threading 
import time
 
ip_port = ('127.0.0.1', 9000) 
buffer_size = 1024 
# 處理客戶端，sock為socket，addr為客戶端地址 
def tcp_server(sock, addr):
    mydata = []
    print("Accept new connection from %s:%s" % addr) 
    #sock.sendall("What's your name名字?".encode() )
    while True: 
        data = sock.recv(buffer_size) 
        time.sleep(0.1) 
        if data.decode("utf-8") == "bye": 
            break 
        sock.send("ACK!".encode())
        mydata.append(data.decode("utf-8"))
    sock.close() 
    print('Connection from %s:%s closed.' % addr)
    f = open('log.txt', 'a', encoding='utf-8')
    f.write('------------------------------------------\n')
    tt = f'{time.asctime()}\n'
    f.write(tt)
    cc = f'Connected by:{addr}\n'
    f.write(cc)

    # dd = f'{mydata}\n'
    for line in mydata:
        f.write(line+'\n')
    print(mydata)
    f.close()
        
def main(): 
    # 建立IPV4的TCP的socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # 綁定地址到socket 
    sock.bind(ip_port) 
    # 設置最大連接數，並開始監聽 
    sock.listen(10) 
    print("TCP Server is running") 
    print("Wait for new Connection...........") 
    while True: 
        # 接收TCP客戶端連接，阻塞等待連接 
        sock_fd, addr = sock.accept()
        
        # 開啟新線程對TCP連接進行處理 
        thread = threading.Thread(target=tcp_server, args=(sock_fd, addr)) 
        thread.start() 
        
if __name__ == "__main__": 
      main()


