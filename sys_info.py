import sys
import socket

try:
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportError:
    from urllib2 import urlopen, URLError


PUBLIC_IP_URL = "http://ip.42.pl/raw"


def log_info(title, value):
    sys.stdout.write("{:15} {}\n".format(title, value))


def get_sys_info():
    log_info("Platform:", sys.platform)
    log_info("Python Ver:", sys.version)
    log_info("Local IP:", socket.gethostbyname(socket.gethostname()))

    public_ip = ""
    try:
        public_ip = urlopen(PUBLIC_IP_URL).read().decode()
    except URLError:
        pass

    log_info("Public IP:", public_ip)


if __name__ == '__main__':
    get_sys_info()
