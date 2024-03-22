1. Определить все IP адреса, маски подсетей и соответствующие MAC адреса Linux VM. Определите класс и адреса подсетей, в которых находится VM.

> rvlt135@rvlt135:~$ ifconfig -a
```
ens3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 94.250.248.253  netmask 255.255.255.255  broadcast 94.250.248.253
        inet6 fe80::5054:ff:fe15:322a  prefixlen 64  scopeid 0x20<link>
        ether 52:54:00:15:32:2a  txqueuelen 1000  (Ethernet)
        RX packets 564245  bytes 104607537 (104.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 480969  bytes 47409482 (47.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 7178  bytes 737665 (737.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 7178  bytes 737665 (737.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

класс сети - A, и адрес подсети - 94.250.248.253/32

2. Определить публичный IP адрес хоста и Linux VM? Чем они отличаются?
Так как у меня VPS с внешним адресом, то доступен только 1 адрес.
Если бы был адрес внутренний сети, то он входил бы в список адресов только указанной подсети и не был бы доступен из вне, только с помощью внешнего ip.
```
rvlt135@rvlt135:~$ curl ifconfig.me
94.250.248.253
```

3. Вывести ARP таблицу на хосте и найти там запись, соответствующую MAC адресу с предыдущего задания. Если её нет, то объяснить почему.
```
rvlt135@rvlt135:~$ arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.0.1                 ether   02:00:00:00:00:01   C                     ens3
```
Я думаю что так как никакие хосты не взаимодействовали с моим ip адресом, поэтому нет arp записей в таблице. 

4. Выполнить разбиение сети 172.20.0.0/16 на подсети с маской /24 и ответить на следующие вопросы:
Сколько всего подсетей будет в сети?
256 подсетей.

Сколько узлов будет в каждой подсети?
Общее количество 256 из которых 1 - будет для сетевого взаимодействия. 1 - широковещательный адрес

Каким будет сетевой адрес первой и второй подсети?
1. 172.20.0.0/24
2. 172.20.1.0/24

Каким будут адреса первого и последнего хостов в первой и второй подсетях?
1. В первой сети 172.20.0.1 и 172.20.0.254
2. Во второй сети 172.20.1.1 и 172.20.1.254

Каким будет широковещательный адрес в последней подсети?
172.20.255.255

5. Найти IP адрес соответствующий доменному имени ya.ru. Выполнить HTTP запрос на указанный IP адрес, чтобы скачать страницу с помощью утилиты curl.
В результате должна вывестись HTML страничка в консоль.
```
rvlt135@rvlt135:~$ nslookup ya.ru
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	ya.ru
Address: 5.255.255.242
Name:	ya.ru
Address: 77.88.55.242
Name:	ya.ru
Address: 2a02:6b8::2:242

```
Выполняем запрос c сохранением ответа в файл .html
```
rvlt135@rvlt135:~/development/igor-vanin/homework-6$ curl -LH "Host: ya.ru" -o ya-ru.html "http://77.88.55.242"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 13413  100 13413    0     0   216k      0 --:--:-- --:--:-- --:--:--  216k
rvlt135@rvlt135:~/development/igor-vanin/homework-6$ ls -al
total 36
drwxrwxr-x 2 rvlt135 rvlt135  4096 Mar 11 23:21 .
drwxrwxr-x 7 rvlt135 rvlt135  4096 Mar 11 23:17 ..
-rw-rw-r-- 1 rvlt135 rvlt135 10238 Mar 11 23:21 homework6.md
-rw-rw-r-- 1 rvlt135 rvlt135 13413 Mar 11 23:21 ya-ru.html
```
