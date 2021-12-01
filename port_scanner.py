import socket
import time
import threading

from queue import Queue

socket.setdefaulttimeout(1)
print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print('Starting scan on host: ', t_IP)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
            try:
                banner = s.recv(1024)
                print(str(banner.decode().strip('\n')))
            except:
                print('Receive unsuccessful')
        s.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()
startTime = time.time()

threads = 1000
for x in range(threads):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start_port = 1
end_port = 10000
for worker in range(start_port, end_port+1):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)