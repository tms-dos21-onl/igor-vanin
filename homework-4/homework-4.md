1. Вывести список всех процессов:
> ps -aux

2. Запустить бесконечный процесс в фоновом режиме используя nohup:
> nohup ping 127.0.0.1 &

3. Убедиться, что процесс продолжил работу после завершения сессии.

> pgrep -a ping
> rvlt135@rvlt135:~/development/igor-vanin/homework-4$ pgrep -a ping
> 640360 ping 127.0.0.1

Альтернативный вариант:
> ps -au | grep ping
> rvlt135@rvlt135:~/development/igor-vanin/homework-4$ ps -aux | grep ping
> rvlt135   640360  0.0  0.0   5132  1288 pts/0    S    20:54   0:00 ping 127.0.0.1

4. Убить процесс, запущенный в фоновом режиме. 
> kill 640360

5. Написать свой сервис под управлением systemd, добавить его в автозагрузку (можно использовать процесс из п.2).
Использую bash скрипт который пингует 127.0.0.1
> rvlt135@rvlt135:~/development/igor-vanin/homework-4$ cat ~/pinger.sh 
> #!/bin/bash
> ping 127.0.0.1

Выдаю права для выполнения файла
> chomod +x pinger.sh

Создаю файл в /etc/systemd/system/pinger.service
> rvlt135@rvlt135:~/development/igor-vanin/homework-4$ cat /etc/systemd/system/pinger.service 
> [Unit]
> Description=Pinger service
> After=network.target
>
> [Service]
> User=rvlt135
> ExecStart=/home/rvlt135/pinger.sh
> Type=simple
> Restart=always
> RestartSec=1

> [Install]
> WantedBy=multi-user.target

Добавляю его в автозагрузку 
sudo systemctl enable pinger.service

Пример выполнения команд start и status:
> rvlt135@rvlt135:~$ sudo systemctl start pinger.service
>rvlt135@rvlt135:~$ sudo systemctl status pinger.service
> ● pinger.service - Pinger service
>      Loaded: loaded (/etc/systemd/system/pinger.service; enabled; vendor preset: enabled)
>      Active: active (running) since Tue 2024-02-27 21:59:34 MSK; 13s ago
>    Main PID: 1221 (pinger.sh)
>      Tasks: 2 (limit: 4559)
>     Memory: 708.0K
>        CPU: 7ms
>     CGroup: /system.slice/pinger.service
>             ├─1221 /bin/bash /home/rvlt135/pinger.sh
>             └─1222 ping 127.0.0.1

> Feb 27 21:59:37 rvlt135.fvds.ru pinger.sh[1222]: 64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.084 ms
> Feb 27 21:59:38 rvlt135.fvds.ru pinger.sh[1222]: 64 bytes from 127.0.0.1: icmp_seq=5 ttl=64 time=0.073 ms
> Feb 27 21:59:39 rvlt135.fvds.ru pinger.sh[1222]: 64 bytes from 127.0.0.1: icmp_seq=6 ttl=64 time=0.095 ms
