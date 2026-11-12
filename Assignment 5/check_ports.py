from urllib.request import urlopen 
import socket

HOST = "127.0.0.1"
PORTS = [8000]

def check_port(host: str, port: int, timeout: float = 1.0) -> str:
    """Return 'open', 'refused', or 'timeout' for a TCP connect attempt."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return "open"
        except ConnectionRefusedError:
            return "refused"
        except (socket.timeout, OSError):
            return "timeout"

def main() -> int:
    for port in PORTS:
        status = check_port(HOST, port)
        print(f"{HOST}:{port:<5} -> {status}")
        print(urlopen(f"http://{HOST}:{port}").read().decode('utf-8'))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

