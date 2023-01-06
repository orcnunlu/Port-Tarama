import pyfiglet
import sys
import socket
from datetime import datetime

baslık = pyfiglet.figlet_format("OrcunPars")
print(baslık)

print("Taranacak İp adresini Girin:")
ip=input()

hedef = ip



print("-" * 50)
print("Hedef taranıyor: " + hedef)
print("Tarama başlama zamanı:" + str(datetime.now()))
print("-" * 50)

try:

    # 1-2088 arası tara
    for port in range(1, 2088):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Açık portları yazdır
        result = s.connect_ex((hedef, port))
        if result == 0:
            print("Port {} Açık!".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Program kapatılıyor !!!!")
    sys.exit()
except socket.error:
    print("\ Server cevap vermiyor !!!!")
    sys.exit()