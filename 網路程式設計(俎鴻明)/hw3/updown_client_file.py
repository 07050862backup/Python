import socket
import os
def getfile(cmd):

    client.send(cmd.encode('utf-8'))
    fileinfo = client.recv(1024).decode("utf-8")
    print(fileinfo)
    client.send('ACK'.encode())
    total_size = int(fileinfo.split('#')[0])
    file_name  = fileinfo.split('#')[1]
    #接收真實的資料
    with open(r'%s\%s'%(download_dir, file_name),'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = client.recv(64)
            f.write(line)
            recv_size += len(line)
            print('已下載大小：%d' % recv_size)

def putfile(cmd):
    # client : get file
    filename = cmd.split()[1]
    filesize = os.path.getsize(r'%s\%s' % (upload_dir, filename))
    # file info
    fileinfo = str(filesize) + "#" + filename
    client.sendall(fileinfo.encode('utf-8'))
    # data
    client.recv(1024).decode('utf-8')
    client.sendall(fileinfo.encode('utf-8'))
    # 再發送真實的資料
    with open(r'%s\%s' % (upload_dir, filename), 'rb') as f:
        for line in f:
            client.sendall(line)


download_dir = r'D:\D槽下載\上傳下載作業\下載成功的檔案'
upload_dir =   r'D:\D槽下載\上傳下載作業\下載成功的檔案'
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8129))
#接收server送出的檔案清單
files=client.recv(2048).decode("utf-8")
print('可下載檔案清單:\n',files)
while True:
    cmd=input('輸入:get/put 檔名 >>:').strip()  #get a.txt
    if cmd.strip()=="bye":
        break
    if not cmd:
        continue
    elif cmd.split()[0]=='get':
        getfile(cmd)
    elif cmd.split()[0]=='put':
        putfile(cmd)
    else:
        print('command error')
        continue
client.close()
