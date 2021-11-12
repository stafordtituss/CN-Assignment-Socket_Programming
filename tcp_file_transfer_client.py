import socket
import tqdm
import os
import sys
import pickle

SERV_ADDR = "127.0.0.1"
SERV_PORT = 5001
OUT_BUF = 4096

if len(sys.argv) > 1:
    filename = sys.argv[1]
    filesize = os.path.getsize(filename)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((SERV_ADDR, SERV_PORT))
        file_info = [filename, filesize]
        file_info = pickle.dumps(file_info)
        soc.send(file_info)
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as send_file:
            while True:
                bytes_read = send_file.read(OUT_BUF)
                if not bytes_read:
                    break
                soc.sendall(bytes_read)
                progress.update(len(bytes_read))
        soc.close()
else:
    print("Provide a file name please!")
    exit
