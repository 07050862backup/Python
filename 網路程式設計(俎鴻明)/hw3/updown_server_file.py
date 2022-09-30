import socket
import os
import threading
def getfile(conn,cmd):

    filename = cmd[1]
    filesize = os.path.getsize(r'%s\%s' % (share_dir, filename))  # 路徑\1.txt
    # file info
    fileinfo = str(filesize) + "#" + filename
    conn.sendall(fileinfo.encode())
    conn.recv(64)
    # 再發送真實的資料
    with open(r'%s\%s' % (share_dir, filename), 'rb') as f:
        for line in f:
            conn.sendall(line)
def putfile(conn,cmd):
    # get file
    # ACK
    conn.send('ACK'.encode())
    fileinfo = conn.recv(64).decode('utf-8')#%%%%%%%%%%%
    print(fileinfo)
    # server :data
    total_size = int(fileinfo.split('#')[0])
    file_name = fileinfo.split('#')[1]
    # 接收真實的資料
    with open(r'%s\%s' % (share_dir, file_name), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = conn.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('已下載大小：%d' % recv_size)
def tcp_server(conn, client_addr):
    print("Accept new connection from %s:%s" % client_addr)
    # 1、送出檔案清單
    files=os.listdir(share_dir)#listdir會回傳一個串列(a list of files)
    conn.sendall(str(files).encode())
    while True: # 通訊迴圈
        try:
            #接受命令
            res = conn.recv(128)  # 'get 1.txt'
            # 2、解析命令，提取相應命令引數
            cmd = res.decode('utf-8').strip().split() # ['get','1.txt']
            if cmd[0]=='get':
                getfile(conn,cmd)
            else:
                putfile(conn,cmd)
        except (IndexError,ConnectionResetError,OSError):
            print("bye...")
            break
    conn.close()
share_dir = r'D:\D槽下載\上傳下載作業\sharedfiles'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8129)) # 0-65535: 0-1024給作業系統使用
server.listen(5)
print("Listening...........")
while True:
    print("\nwaiting...........")
    sock_fd, addr = server.accept()
    thread = threading.Thread(target=tcp_server, args=(sock_fd, addr))
    thread.start()
