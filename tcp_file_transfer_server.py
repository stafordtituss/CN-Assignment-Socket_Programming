import socket
import tqdm
import os
import sys
import pickle

SERV_ADDR = "127.0.0.1"
SERV_PORT = 5001
INC_BUF = 4096

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind((SERV_ADDR, SERV_PORT))
    soc.listen()
    con, con_addr = soc.accept()
    recv_data = con.recv(INC_BUF)
    recv_data = pickle.loads(recv_data)
    filename, filesize = [recv_data[i] for i in range(2)]
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as recv_file:
        while True:
            bytes_read = con.recv(INC_BUF)
            if not bytes_read:    
                break
            recv_file.write(bytes_read)
            progress.update(len(bytes_read))

    con.close()
    soc.close()