from socket import *
import os


def parsing(host):
    # raw socket 생성 몇 bind
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    # socket 옵션
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # promiscuous mode
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)

        data = sock.recvfrom(65535)
        print(data[0])

    # promiscuous mode 끄기
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_OFF)

    # 소켓종료
    sock.close()


if __name__ == "__main__":
    host = "192.168.50.55"
    print(f"Listening at [{host}]")
    parsing(host)
