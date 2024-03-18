1. Вывести в консоль список всех пользователей системы.
```
cat /etc/passwd
```
2. Найти и вывести в консоль домашние каталоги для текущего пользователя и root.
```
rvlt135@rvlt135:~$ echo $HOME
/home/rvlt135
rvlt135@rvlt135:~$ echo ~root
/root
```
3. Создать Bash скрипт get-date.sh, выводящий текущую дату.
4. Запустить скрипт через ./get-date.sh и bash get-date.sh. Какой вариант не работает? Сделать так, чтобы оба варианта работали.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ cat get-date.sh 
date

rvlt135@rvlt135:~/development/igor-vanin/homework-9$ bash get-date.sh 
Mon Mar 18 23:27:51 MSK 2024

rvlt135@rvlt135:~/development/igor-vanin/homework-9$ ./get-date.sh 
-bash: ./get-date.sh: Permission denied

rvlt135@rvlt135:~/development/igor-vanin/homework-9$ chmod +x get-date.sh 

rvlt135@rvlt135:~/development/igor-vanin/homework-9$ ./get-date.sh 
Mon Mar 18 23:28:11 MSK 2024
```
Скрипт не работает из за того что ему не хватает прав для выполнения при первичном создании.

5. Создать пользователей alice и bob с домашними директориями и установить /bin/bash в качестве командной оболочки по умолчанию.
```
adduser bob
adduser alice
alice:x:1001:1002:,,,:/home/alice:/bin/bash
bob:x:1002:1003:,,,:/home/bob:/bin/bash
```
6. Запустить интерактивную сессию от пользователя alice. Создать файл secret.txt с каким-нибудь секретом в домашней директории при помощи текстового редактора nano.
7. Вывести права доступа к файлу secret.txt.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo -i -u alice
alice@rvlt135:~$ pwd
/home/alice
alice@rvlt135:~$ nano secret.txt
alice@rvlt135:~$ ls -la | grep secret
-rw-rw-r-- 1 alice alice   53 Mar 18 23:37 secret.txt
```
8. Выйти из сессии от alice и открыть сессию от bob. Вывести содержимое файла /home/alice/secret.txt созданного ранее не прибегая к команде sudo. В случае, если это не работает, объяснить.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo -i -u bob 
bob@rvlt135:~$ cat /home/alice/secret.txt
cat: /home/alice/secret.txt: Permission denied
bob@rvlt135:~$ 

rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo ls -al /home/alice/
total 32
drwxr-x--- 3 alice alice 4096 Mar 18 23:37 .
drwxr-xr-x 5 root  root  4096 Mar 18 23:31 ..
-rw------- 1 alice alice   51 Mar 18 23:46 .bash_history
-rw-r--r-- 1 alice alice  220 Mar 18 23:30 .bash_logout
-rw-r--r-- 1 alice alice 3771 Mar 18 23:30 .bashrc
drwxrwxr-x 3 alice alice 4096 Mar 18 23:36 .local
-rw-r--r-- 1 alice alice  807 Mar 18 23:30 .profile
-rw-rw-r-- 1 alice alice   53 Mar 18 23:37 secret.txt
```

У пользователя bob нет доступа к файлам в домашней директории alice, так как он не состоит в группе с alice. Создание юзера происходит из под root и просмотр без выдачи доступов к файлу доступен только ему.
9. Создать файл secret.txt с каким-нибудь секретом в каталоге /tmp при помощи текстового редактора nano.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo usermod -a -G bob alice
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo -i -u alice 
alice@rvlt135:~$ cat /tmp/secret.txt 
secret bob: b+fwB9fS1/Li37Eg0vPL1XNC/VTqA0912bT/qWVw2oY/ZRUgYP9Aac0yBy9rLZoO
```
10. Вывести права доступа к файлу secret.txt. Поменять права таким образом, чтобы этот файл могли читать только владелец и члены группы, привязанной к файлу.
```
bob@rvlt135:~$ chmod ug+r /tmp/secret.txt 

bob@rvlt135:~$ ls -al /tmp/secret.txt 
-r--r----- 1 bob bob 77 Mar 18 23:55 /tmp/secret.txt
```
11. Выйти из сессии от bob и открыть сессию от alice. Вывести содержимое файла /tmp/secret.txt созданного ранее не прибегая к команде sudo. В случае, если это не работает, объяснить.
```
bob@rvlt135:~$ exit
logout

rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo -i -u alice

alice@rvlt135:~$ cat /tmp/secret.txt 
cat: /tmp/secret.txt: Permission denied
```
Пользователь alice не состоит в группе и не является владельцем файла /tmp/secret.txt поэтому доступ к чтению файлов остутствует.

12. Добавить пользователя alice в группу, привязанную к файлу /tmp/secret.txt.
13. Вывести содержимое файла /tmp/secret.txt.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo usermod -a -G bob alice
rvlt135@rvlt135:~/development/igor-vanin/homework-9$ sudo -i -u alice 
alice@rvlt135:~$ cat /tmp/secret.txt 
secret bob: b+fwB9fS1/Li37Eg0vPL1XNC/VTqA0912bT/qWVw2oY/ZRUgYP9Aac0yBy9rLZoO
alice@rvlt135:~$ 
```

14. Скопировать домашнюю директорию пользователя alice в директорию /tmp/alice с помощью rsync.
```
alice@rvlt135:~$ rsync -av /home/alice/ /tmp/alice
sending incremental file list
created directory /tmp/alice
./
.bash_history
.bash_logout
.bashrc
.profile
secret.txt
.local/
.local/share/
.local/share/nano/

sent 5,473 bytes  received 163 bytes  11,272.00 bytes/sec
total size is 4,954  speedup is 0.88
```
Директория успешно скопировалась.
```
alice@rvlt135:~$ ls -al /tmp/alice/
total 32
drwxr-x---  3 alice alice 4096 Mar 18 23:37 .
drwxrwxrwt 12 root  root  4096 Mar 19 00:23 ..
-rw-------  1 alice alice  103 Mar 19 00:15 .bash_history
-rw-r--r--  1 alice alice  220 Mar 18 23:30 .bash_logout
-rw-r--r--  1 alice alice 3771 Mar 18 23:30 .bashrc
drwxrwxr-x  3 alice alice 4096 Mar 18 23:36 .local
-rw-r--r--  1 alice alice  807 Mar 18 23:30 .profile
-rw-rw-r--  1 alice alice   53 Mar 18 23:37 secret.txt
```
15. Скопировать домашнюю директорию пользователя alice в директорию /tmp/alice на другую VM по SSH с помощью rsync. Как альтернатива, можно скопировать любую папку с хоста на VM по SSH.
```
sudo rsync -av /Users/ivanin/test_dir root@123.123.123.123:/tmp/

rvlt135@rvlt135:/etc/systemd$ ls -al /tmp/test_dir/
total 12
drwxr-xr-x  2 501 staff 4096 Mar 19 00:28 .
drwxr-xr-x 13 501 staff 4096 Mar 19 01:26 ..
-rw-r--r--  1 501 staff    9 Mar 19 00:28 testfile.txt

```
16. Удалить пользователей alice и bob вместе с домашними директориями.
```
1483  sudo userdel -fr alice
1484  sudo userdel -fr bob
```
17. С помощью утилиты htop определить какой процесс потребляет больше всего ресурсов в системе.
Более потребляемый ресурс, можно отсортировать по MEM или CPU
![telegram-cloud-photo-size-2-5458779815923538370-y](https://github.com/tms-dos21-onl/igor-vanin/assets/41593525/723e2d3f-599d-4622-a4bf-961d939d222c)

19. Вывести логи сервиса Firewall с помощью journalctl не прибегая к фильтрации с помощью grep
```
rvlt135@rvlt135:/etc/systemd$ sudo ufw enable
[sudo] password for rvlt135: 
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y 
Firewall is active and enabled on system startup
rvlt135@rvlt135:/etc/systemd$ sudo systemctl status ufw
● ufw.service - Uncomplicated firewall
     Loaded: loaded (/lib/systemd/system/ufw.service; enabled; vendor preset: enabled)
     Active: active (exited) since Mon 2024-03-18 22:57:07 MSK; 2h 27min ago
       Docs: man:ufw(8)
    Process: 401 ExecStart=/lib/ufw/ufw-init start quiet (code=exited, status=0/SUCCESS)
   Main PID: 401 (code=exited, status=0/SUCCESS)
        CPU: 1ms

Mar 18 22:57:07 rvlt135.fvds.ru systemd[1]: Starting Uncomplicated firewall...
Mar 18 22:57:07 rvlt135.fvds.ru systemd[1]: Finished Uncomplicated firewall.
rvlt135@rvlt135:/etc/systemd$ sudo journalctl -u ufw.service
Feb 29 22:49:00 rvlt135.fvds.ru systemd[1]: Starting Uncomplicated firewall...
Feb 29 22:49:00 rvlt135.fvds.ru systemd[1]: Finished Uncomplicated firewall.
Feb 29 23:15:05 rvlt135.fvds.ru systemd[1]: Stopping Uncomplicated firewall...
Feb 29 23:15:06 rvlt135.fvds.ru systemd[1]: ufw.service: Deactivated successfully.
Feb 29 23:15:06 rvlt135.fvds.ru systemd[1]: Stopped Uncomplicated firewall.
Feb 29 23:15:06 rvlt135.fvds.ru systemd[1]: Starting Uncomplicated firewall...
Feb 29 23:15:06 rvlt135.fvds.ru systemd[1]: Finished Uncomplicated firewall.
-- Boot 5f2107698ffa46378f40ad196a88c3da --
Mar 18 22:36:41 rvlt135.fvds.ru systemd[1]: Starting Uncomplicated firewall...
Mar 18 22:36:41 rvlt135.fvds.ru systemd[1]: Finished Uncomplicated firewall.
-- Boot 651ea8e623e14f628f9695d718b939ae --
Mar 18 22:57:07 rvlt135.fvds.ru systemd[1]: Starting Uncomplicated firewall...
Mar 18 22:57:07 rvlt135.fvds.ru systemd[1]: Finished Uncomplicated firewall.
rvlt135@rvlt135:/etc/systemd$ sudo journalctl -u firewalld.service
-- No entries --

```
