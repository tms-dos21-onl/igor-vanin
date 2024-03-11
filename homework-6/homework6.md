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


Столкнулся с несколькими проблемами 406 выполнения запроса: 
```
curl --location 'https://77.88.55.242/' -k -v
rvlt135@rvlt135:~$ curl --location 'https://77.88.55.242/' -k -v
*   Trying 77.88.55.242:443...
* Connected to 77.88.55.242 (77.88.55.242) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS header, Finished (20):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.2 (OUT), TLS header, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: C=RU; ST=Moscow; L=Moscow; O=YANDEX LLC; CN=*.xn--d1acpjx3f.xn--p1ai
*  start date: Mar  4 10:29:07 2024 GMT
*  expire date: Sep  1 20:59:59 2024 GMT
*  issuer: C=BE; O=GlobalSign nv-sa; CN=GlobalSign ECC OV SSL CA 2018
*  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* Using Stream ID: 1 (easy handle 0x55b9e5322eb0)
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
> GET / HTTP/2
> Host: 77.88.55.242
> user-agent: curl/7.81.0
> accept: */*
> 
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* TLSv1.2 (IN), TLS header, Supplemental data (23):
< HTTP/2 406 
< content-length: 0
< accept-ch: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT
< report-to: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]}
< nel: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1}
< x-content-type-options: nosniff
< x-yandex-req-id: 1709904215500979-14105338413721515030-balancer-l7leveler-kubr-yp-sas-101-BAL
< 
* Connection #0 to host 77.88.55.242 left intact
```

Или:
```
rvlt135@rvlt135:~$ curl -v --location 'http://77.88.55.242/'
*   Trying 77.88.55.242:80...
* Connected to 77.88.55.242 (77.88.55.242) port 80 (#0)
> GET / HTTP/1.1
> Host: 77.88.55.242
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 406 Not acceptable
< Accept-CH: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT
< Connection: Close
< Content-Length: 0
< NEL: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1}
< Report-To: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]}
< X-Content-Type-Options: nosniff
< X-Yandex-Req-Id: 1709904295459181-3685937197905554874-balancer-l7leveler-kubr-yp-sas-67-BAL
< 
* Closing connection 0
```
```
rvlt135@rvlt135:~$ curl -v --location 'http://77.88.55.242/' --header 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
*   Trying 77.88.55.242:80...
* Connected to 77.88.55.242 (77.88.55.242) port 80 (#0)
> GET / HTTP/1.1
> Host: 77.88.55.242
> User-Agent: curl/7.81.0
> accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 406 Not acceptable
< Accept-CH: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT
< Connection: Close
< Content-Length: 0
< NEL: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1}
< Report-To: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]}
< X-Content-Type-Options: nosniff
< X-Yandex-Req-Id: 1709904332220417-13127446024219913370-balancer-l7leveler-kubr-yp-sas-140-BAL
< 
* Closing connection 0
```

Если бы победил ошибку, выполнял запрос в следующей констрокции
Также пробовал другие ip ya.ru домена
```
curl -o ya.html http://77.88.55.242
```
