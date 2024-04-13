1. Вывести список всех удаленных репозиториев для локального.
```
rvlt135@rvlt135:~/development/igor-vanin$ git ls-remote
From git@github.com:tms-dos21-onl/igor-vanin.git
33bf19e043d85e585de3dd68663d4a6b98809e33	HEAD
f9fc9b2c9040e3a4afa6b23d0f9932446236cbd2	refs/heads/homework-4
33bf19e043d85e585de3dd68663d4a6b98809e33	refs/heads/homework-5
93c8f70a6b8ca83359bf3d1b05aaae0bcb34a948	refs/heads/homework-6
cbc6165df7a37949e5f012dff0296b4902616a69	refs/heads/homework-8
33bf19e043d85e585de3dd68663d4a6b98809e33	refs/heads/main
```
2. Вывести список всех веток.
```
rvlt135@rvlt135:~/development/igor-vanin$ git branch -a
  homework-2
  homework-3
  homework-4
  homework-5
  homework-6
* homework-8
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/homework-2
  remotes/origin/homework-3
  remotes/origin/homework-4
  remotes/origin/homework-5
  remotes/origin/homework-6
  remotes/origin/homework-8
  remotes/origin/ivanin-homework-2
  remotes/origin/main

```
3. Вывести последние 3 коммитa с помощью git log.
```
rvlt135@rvlt135:~/development/igor-vanin$ git log --max-count=3
commit cbc6165df7a37949e5f012dff0296b4902616a69 (HEAD -> homework-8, origin/homework-8)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Mon Mar 11 23:15:29 2024 +0300

    homework 8

commit 4e97a08533f8c3164a306a046a68f59dde8c6dae (main)
Merge: 4f2938b ae4637b
Author: i.vanin <i.vanin@scalableolutions.io>
Date:   Mon Feb 26 17:05:52 2024 +0100

    Merge branch 'homework-3'

commit ae4637b493b484e09a380c8755bcb79b18c230d4 (origin/homework-3, homework-3)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Tue Feb 13 00:17:27 2024 +0300

    add sysinfo.sh
```
4. Создать пустой файл README.md и сделать коммит.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git add README.md 
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git commit -m "Add README.md"
[homework-8 470f43a] Add README.md
 Committer: rvlt135 <rvlt135@rvlt135.fvds.ru>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homework-8/README.md

```
5. Добавить фразу "Hello, DevOps" в README.md файл и сделать коммит.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git add README.md 
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git commit -m "Add Hello Devops to README.md"
[homework-8 7f4210a] Add Hello Devops to README.md
 Committer: rvlt135 <rvlt135@rvlt135.fvds.ru>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author
```

6. Сделать реверт последнего коммита. Вывести последние 3 коммитa с помощью git log.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git log
commit 7f4210a1fb13e04c5da07da7425540450d8bbab9 (HEAD -> homework-8)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Mon Mar 11 23:39:50 2024 +0300

    Add Hello Devops to README.md

commit 470f43a2a0cd9e9e2a1fb3ad4a911cb769db3060
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Mon Mar 11 23:38:12 2024 +0300

    Add README.md
```
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git reset --hard HEAD~1
HEAD is now at 470f43a Add README.md
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git log
commit 470f43a2a0cd9e9e2a1fb3ad4a911cb769db3060 (HEAD -> homework-8)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Mon Mar 11 23:38:12 2024 +0300

    Add README.md

```
7. Удалить последние 3 коммита с помощью git reset.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git reset --hard HEAD~3
HEAD is now at 4f2938b Update homework2.txt
```
8. Вернуть коммит, где добавляется пустой файл README.md. Для этого найти ID коммита в git reflog, а затем сделать cherry-pick.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git cherry-pick 470f43a
[homework-8 3f82e31] Add README.md
 Date: Mon Mar 11 23:38:12 2024 +0300
 Committer: rvlt135 <rvlt135@rvlt135.fvds.ru>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 homework-8/README.md
```
9. Удалить последний коммит с помощью git reset.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8$ git reset --hard HEAD~1
HEAD is now at 4f2938b Update homework2.txt
```

10. Переключиться на ветку main или master. Если ветка называется master, то переименовать её в main.
```
git checkout main
```

11. Скопировать файл https://github.com/tms-dos21-onl/_sandbox/blob/main/.github/workflows/validate-shell.yaml, положить его по такому же относительному пути в репозиторий. Создать коммит и запушить его в удаленный репозиторий.
```
rvlt135@rvlt135:~/development/igor-vanin/homework-8/.github/workflow$ curl  -ovalidate-shell.yaml https://raw.githubusercontent.com/tms-dos21-onl/_sandbox/main/.github/workflows/validate-shell.yaml
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    14  100    14    0     0    116      0 --:--:-- --:--:-- --:--:--   116
```

12. Создать из ветки main ветку develop. Переключиться на неё и создать README.md в корне репозитория. Написать в этом файле какие инструменты DevOps вам знакомы и с какими вы бы хотели познакомиться больше всего (2-3 пункта).
```
rvlt135@rvlt135:~/development/igor-vanin$ git branch
* develop
  homework-2
  homework-3
  homework-4
  homework-5
  homework-6
  homework-8
  main
rvlt135@rvlt135:~/development/igor-vanin$ nano README.md
rvlt135@rvlt135:~/development/igor-vanin$ git commit -m "Add README.md"
On branch develop
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
rvlt135@rvlt135:~/development/igor-vanin$ git add .
rvlt135@rvlt135:~/development/igor-vanin$ git commit -m "Add README.md"
[develop efc4099] Add README.md
 Committer: rvlt135 <rvlt135@rvlt135.fvds.ru>
 1 file changed, 4 insertions(+)
 create mode 100644 README.md
rvlt135@rvlt135:~/development/igor-vanin$ git push origin develop

```

13. Создать из ветки main ветку support и создать там файл LICENSE в корне репозитория с содержимым https://www.apache.org/licenses/LICENSE-2.0.txt. Создать коммит. Вывести последние 3 коммитa.
git checkout -b support
curl -o LICENSE.md https://www.apache.org/licenses/LICENSE-2.0.txt
git log --max-count=3

```
rvlt135@rvlt135:~/development/igor-vanin$ git log --max-count=3
commit daaafaa067037b44d34519b70be8324b94c96c3e (HEAD -> support)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Tue Mar 12 00:24:19 2024 +0300

    add LICENSE.md

commit 55634cd3cd963d0bde7de68821267e7bab86b63d (origin/homework-8, homework-8)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Tue Mar 12 00:17:46 2024 +0300

    change homework8

commit 9b5f5e221cdc45349c98e934dc7afad84a722d0b
Merge: ab04850 cbc6165
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Tue Mar 12 00:08:11 2024 +0300

    add homework8
```

14. Переключиться обратно на ветку main и создать там файл LICENSE в корне репозитория с содержимым https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt. Создать коммит. Вывести последние 3 коммитa.

```
rvlt135@rvlt135:~/development/igor-vanin$ curl -o LICENSE.md https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  6317  100  6317    0     0  18737      0 --:--:-- --:--:-- --:--:-- 18800
rvlt135@rvlt135:~/development/igor-vanin$ git add LICENSE.md 
rvlt135@rvlt135:~/development/igor-vanin$ git commit -m "Add LICENSE in main"
[main d4bad38] Add LICENSE in main
 Committer: rvlt135 <rvlt135@rvlt135.fvds.ru>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 LICENSE.md
rvlt135@rvlt135:~/development/igor-vanin$ git log --max-count=3
commit d4bad381f826dbbea088b0a1d14ce99145f5fd59 (HEAD -> main)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Tue Mar 12 00:26:59 2024 +0300

    Add LICENSE in main

commit 33bf19e043d85e585de3dd68663d4a6b98809e33 (origin/main, origin/homework-5, origin/HEAD)
Author: Rvlt135 <41593525+Rvlt135@users.noreply.github.com>
Date:   Fri Mar 1 16:47:28 2024 +0100

    Update homework5.md

commit 5d5e8c4d0cd8d518c40eecb4d72f4cf34134ea26 (homework-5)
Author: rvlt135 <rvlt135@rvlt135.fvds.ru>
Date:   Fri Mar 1 18:38:51 2024 +0300

    add 2
```
15. Сделать merge ветки support в ветку main и решить конфликты путем выбора содержимого только одной лицензии.
```
rvlt135@rvlt135:~/development/igor-vanin$ git add LICENSE.md 
rvlt135@rvlt135:~/development/igor-vanin$ git merge support
fatal: You have not concluded your merge (MERGE_HEAD exists).
Please, commit your changes before you merge.
rvlt135@rvlt135:~/development/igor-vanin$ git commit -m "fix conflicts"
[main 7de976a] fix conflicts
 Committer: rvlt135 <rvlt135@rvlt135.fvds.ru>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

rvlt135@rvlt135:~/development/igor-vanin$ git merge support
Already up to date.
```

16. Переключиться на ветку develop и сделать rebase относительно ветки main.
17. Вывести историю последних 10 коммитов в виде графа с помощью команды git log -10 --oneline --graph.
```
rvlt135@rvlt135:~/development/igor-vanin$ git rebase main
Current branch develop is up to date.
rvlt135@rvlt135:~/development/igor-vanin$ git log -10 --oneline --graph
* fa919e4 (HEAD -> develop) Add README.md
* a767b18 (main) delete README.md
* d3bf232 Add README.md
*   7de976a fix conflicts
|\  
| * daaafaa (support) add LICENSE.md
| * 55634cd (origin/homework-8, homework-8) change homework8
| *   9b5f5e2 add homework8
| |\  
| | * cbc6165 homework 8
| * | ab04850 add validate-shell.yaml
| * | c846820 add homework-8
```
18. Запушить ветку develop. В истории коммитов должен быть мерж support -> main.
```
rvlt135@rvlt135:~/development/igor-vanin$ git push origin develop
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 2 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (14/14), 7.64 KiB | 7.64 MiB/s, done.
Total 14 (delta 7), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (7/7), done.
remote: 
remote: Create a pull request for 'develop' on GitHub by visiting:
remote:      https://github.com/tms-dos21-onl/igor-vanin/pull/new/develop
remote: 
To github.com:tms-dos21-onl/igor-vanin.git
 * [new branch]      develop -> develop
rvlt135@rvlt135:~/development/igor-vanin$ git log -10 --oneline --graph
* fa919e4 (HEAD -> develop, origin/develop) Add README.md
* a767b18 (main) delete README.md
* d3bf232 Add README.md
*   7de976a fix conflicts
|\  
| * daaafaa (support) add LICENSE.md
| * 55634cd (origin/homework-8, homework-8) change homework8
| *   9b5f5e2 add homework8
| |\  
| | * cbc6165 homework 8
| * | ab04850 add validate-shell.yaml
| * | c846820 add homework-8

```
