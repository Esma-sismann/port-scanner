import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

target_input = input("Hedef (IP veya domain) gir: ")

# 🌐 Domain → IP çevirme
try:
    target = socket.gethostbyname(target_input)
    print(f"{target_input} -> {target}")
except:
    print("Geçersiz hedef!")
    exit()

print(f"\n{target} taranıyor...\n")

start_time = datetime.now()
open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = sock.connect_ex((target, port))
        
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "Bilinmiyor"
            
            print(f"\033[92m[+] Port {port} AÇIK | Servis: {banner}\033[0m")
            open_ports.append((port, banner))
        
        sock.close()
    except:
        pass

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))

end_time = datetime.now()

# 💾 Dosyaya kaydet
with open("scan_results.txt", "w") as f:
    for port, banner in open_ports:
        f.write(f"Port {port} - {banner}\n")

print("\nTarama tamamlandı!")
print(f"Süre: {end_time - start_time}")
print("Sonuçlar scan_results.txt dosyasına kaydedildi.")