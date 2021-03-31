import optparse
from socket import *
from threading import Thread, Semaphore

screenlock = Semaphore(value=1)

def connScan(tgt_host, tgt_port):
    try:
        conn_skt = socket(AF_INET, SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send(b'hello!\n')
        results = connSkt.recv(100)
        screenlock.acquire()
        print(f'tcp open: {tgtPort}\n results {results}')
    except Exception as e:
        screenlock.acquire()
        print(f'tcp closed: {e}')
    finally:
        screenlock.release()
        conn_skt.close()

def portScan(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except:
        print(f'cannot resolve {tgt_host}')
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print(f'Scan success: {tgt_name[0]}')
    except:
        print(f'Scan fail: {tgt_ip}')
    setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        print(f'Scanning port {tgt_port}')
        thr = Thread(target=connScan, args=(tgt_host, int(tgt_port)))
        thr.start()



def main():
    parser = optparse.OptionParser(usage='%prog [-H] <target host> -p <target port>')
    parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parser.add_option('-p', dest='tgt_port', type='string', help='specify target port')
    (options, args) = parser.parse_args()

    tgt_host = options.tgt_host
    tgt_ports = str(options.tgt_port).split(',')

    if (tgt_host == None) | (tgt_ports[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgt_host, tgt_ports)

if __name__ == '__main__':
    main()