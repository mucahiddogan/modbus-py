# modbus-py
A testbed example of modbus protocol with HMI

server_pi.py is remote server (Raspberry pi)

write_bit.py is client1 that write 1 or 0 (computer)

hmi_client.py is client2 that read temperature and make HMI automatically (computer)

## Kurulum
SERVER ve CLIENT dosyalarında ip adresleri ve portları ayarladıktan sonra 
server_pi.py dosyasını uzaktaki raspberry pi cihazında """sudo python server_pi.py""" komutu ile çalıştırıyoruz.
Kendi localimizde hmi_client.py dosyasını """python3 hmi_client.py""" komutu ile çalıştırıyoruz. 

## TO-DO List
* Gereklilikler dosyası oluşturulacak