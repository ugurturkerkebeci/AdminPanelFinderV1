import requests
import threading
import os
from colorama import Fore, Style, init
os.system('color d')
# Colorama'nın başlatılması
init()

# Renkli yazılar için renklerin tanımlanması
COLOR_RED = Fore.RED
COLOR_GREEN = Fore.GREEN
COLOR_RESET = Style.RESET_ALL
COLOR_CYAN = Fore.CYAN
def admin_panel_bulucu(url, anahtar_kelime, sonuclar):
    tam_url = url + "/" + anahtar_kelime
    print(Fore.MAGENTA+"*"*30)
    print(Fore.BLUE+"Deneniyor:", tam_url)
    try:
        yanıt = requests.get(tam_url, timeout=5)  # Zaman aşımı 5 saniye olarak belirlendi
        if yanıt.status_code == 200:
            sonuclar.append((tam_url, True))
            print(COLOR_GREEN + "[+] " + tam_url + " - Aktif\n" + COLOR_RESET)
        else:
            sonuclar.append((tam_url, False))
            print(COLOR_RED + "[-] " + tam_url + " - Deaktif\n" + COLOR_RESET)
    except requests.exceptions.RequestException as hata:
        sonuclar.append((tam_url, False))
        print(COLOR_RED + "[-] " + tam_url + " - İstek hatası\n" + COLOR_RESET)
    print(Fore.MAGENTA+"*"*30+"\n")
def ana():
    while True:
        os.system("clear" if os.name == "posix" else "cls")  # Terminali temizle
        print(COLOR_CYAN + """

        
$$$$$$$\                       $$\               $$$$$$\           $$\   $$\                               
$$  __$$\                      $$ |            $$$ ___$$$\         $$ |  $$ |                              
$$ |  $$ | $$$$$$\   $$$$$$\ $$$$$$\          $$ _/   \_$$\        $$ |  $$ | $$$$$$\  $$\   $$\  $$$$$$\  
$$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|        $$ / $$$$$\ $$\       $$ |  $$ |$$  __$$\ $$ |  $$ |$$  __$$\ 
$$  __$$< $$ /  $$ |$$ /  $$ | $$ |          $$ |$$  $$ |$$ |      $$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\       $$ |$$ /$$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      
$$ |  $$ |\$$$$$$  |\$$$$$$  | \$$$$  |      $$ |\$$$$$$$$  |      \$$$$$$  |\$$$$$$$ |\$$$$$$  |$$ |      
\__|  \__| \______/  \______/   \____/       \$$\ \________/        \______/  \____$$ | \______/ \__|      
                                              \$$$\   $$$\                   $$\   $$ |                    
                                               \_$$$$$$  _|                  \$$$$$$  |                    
                                                 \______/                     \______/                     


        """)
        url = input(Fore.GREEN+"Tarama yapılacak URL'yi girin ('q' tuşuna basarak çıkış yapın): "+Fore.RED)
        if url.lower() == "q":
            break
        
        with open("keywords.txt", "r") as dosya:
            anahtar_kelimeler = [anahtar.strip() for anahtar in dosya.readlines()]

        sonuclar = []
        for anahtar in anahtar_kelimeler:
            is_parçasi = threading.Thread(target=admin_panel_bulucu, args=(url, anahtar, sonuclar))
            is_parçasi.start()
            is_parçasi.join()

        input("\nDevam etmek için ENTER tuşuna basın...")

if __name__ == "__main__":
    ana()
