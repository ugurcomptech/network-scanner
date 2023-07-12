import socket
import sys

def scan_port(target_host, target_port, port_index, start_port, end_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_host, target_port))
        sock.close()
        if result == 0:
            print(f"Port {target_port} ({port_index}/{end_port - start_port + 1}): Açık")
            return True
        else:
            print(f"Port {target_port} ({port_index}/{end_port - start_port + 1}): Kapalı")
            return False
    except socket.error:
        print(f"Hedefe bağlanırken hata oluştu. Port {target_port} ({port_index}/{end_port - start_port + 1})")
        return False

def scan_host(target_host, start_port, end_port, output_file):
    output_file.write(f"Tarayıcı başlatıldı: {target_host}\n")
    for port in range(start_port, end_port + 1):
        if scan_port(target_host, port, port - start_port + 1, start_port, end_port):
            output_file.write(f"IP: {target_host} - Port {port}: Açık\n")
        else:
            output_file.write(f"IP: {target_host} - Port {port}: Kapalı\n")

# Ana kod akışı
print("1. Otomatik ağ tarayıcısı")
print("2. Manuel hedef IP adresi tarayıcısı")
choice = input("Seçiminizi yapın (1 veya 2): ")

try:
    if choice == "1":
        baslangic_portu = int(input("Başlangıç portunu girin: "))
        bitis_portu = int(input("Bitiş portunu girin: "))

        with open('network_scan.txt', 'w', encoding='utf-8') as output_file:
            for host in range(1, 255):
                target_host = f"192.168.1.{host}"  # İlgili ağa göre güncelleyin
                print(f"\n{target_host} bloğuna geçildi.\n")
                scan_host(target_host, baslangic_portu, bitis_portu, output_file)
        
        print("Tarama tamamlandı. Sonuçlar 'network_scan.txt' dosyasına kaydedildi.")
        
    elif choice == "2":
        hedef_adres = input("Tarayacağınız hedef IP adresini girin: ")
        baslangic_portu = int(input("Başlangıç portunu girin: "))
        bitis_portu = int(input("Bitiş portunu girin: "))

        with open('manual_scan.txt', 'w', encoding='utf-8') as output_file:
            scan_host(hedef_adres, baslangic_portu, bitis_portu, output_file)
        
        print("Tarama tamamlandı. Sonuçlar 'manual_scan.txt' dosyasına kaydedildi.")
        
    else:
        print("Geçersiz seçim.")

except KeyboardInterrupt:
    print("\nProgram başarıyla kapatıldı.")
    sys.exit(0)
