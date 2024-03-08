1. Распределить основные сетевые протоколы (перечислены ниже) по уровням модели TCP/IP:

> Прикладной:
 	- HTTP
	- SSH
	- NTP
	- DNS
	- RTP
	- FTP
	
> Сетевой:
	- ICMP
> Транспортный:
	- TCP/UDP

2. Узнать pid процесса и длительность подключения ssh с помощью утилиты ss
> ss -ato | grep ssh
> ESTAB      0      52     94.250.248.253:ssh      109.245.192.102:51216 timer:(on,272ms,0)
3. Закрыть все порты для входящих подключений, кроме ssh
после установки включаем ufw 
> sudo ufw enable
закрыть все входящие подключения 
> sudo ufw default deny incoming
Разрешаем порт 22 для подключения
> sudo ufw allow 22

4. Установить telnetd на VM, зайти на нее с другой VM с помощью telnet и отловить вводимый пароль и вводимые команды при входе c помощью tcpdump

Устанавливаем telnetd
>  apt install telnetd -y
Открываем порт 23
> sudo ufw allow 23
> rvlt135@rvlt135:~$ netstat -tulpn | grep LISTEN
> tcp        0      0 0.0.0.0:23              0.0.0.0:*               LISTEN      -  

Подключаемся по telnet и перехватываем траффик на другой машине:
> rvlt135@rvlt135:~$ sudo tcpdump port telnet -l -A | grep -e "Password" -e "Login"
> tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
> listening on ens3, link-type EN10MB (Ethernet), snapshot length 262144 bytes
> E..2..@.@...^...^.a....5.I..e..YP.......Password: 
> ........Password: 
> Login incorrect
> E..2. @.@...^...^.a....5.I..e..eP.......Password: 
> E..P.#@.@...^...^.a....5.I..e..nP....&..Login incorrect
> E..2.%@.@...^...^.a....5.I.+e..tP.......Password: 
> Login incorrect
> E..P.(@.@...^...^.a....5.I.9e..zP....&..Login incorrect
> E..2.*@.@...^...^.a....5.I.ge...P.......Password: 
> Login incorrect
> ..w..UQP.......Password: 
