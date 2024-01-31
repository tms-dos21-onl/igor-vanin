# igor-vanin
1.
rvlt135@rvlt135:~$ cat /etc/motd
```
###WELCOME###
&4TEACHMESKILL DEVOPS
```
2.
rvlt135@rvlt135:~$ uname -a
```
Linux rvlt135.fvds.ru 5.15.0-91-generic #101-Ubuntu SMP Tue Nov 14 13:30:08 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```
3.
```
rvlt135@rvlt135:~$ sudo lsmod > ~/development/igor-vanin/list_modules.txt
```
4.
rvlt135@rvlt135:~$ sudo lshw -class processor
```
  *-cpu                     
       description: CPU
       product: AMD EPYC 7763 64-Core Processor
       vendor: Advanced Micro Devices [AMD]
       physical id: 400
       bus info: cpu@0
       version: 25.1.1
       slot: CPU 0
       size: 2GHz
       capacity: 2GHz
       width: 64 bits
       capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp x86-64 rep_good nopl cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw perfctr_core invpcid_single ssbd ibrs ibpb stibp vmmcall fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr wbnoinvd arat umip pku ospke vaes vpclmulqdq rdpid arch_capabilities
       configuration: cores=2 enabledcores=2 microcode=167776718 threads=1
```

rvlt135@rvlt135:~$ sudo lshw -class memory
```
  *-firmware                
       description: BIOS
       vendor: SeaBIOS
       physical id: 0
       version: 1.16.0-3.module_el8.7.0+3346+68867adb
       date: 04/01/2014
       size: 96KiB
  *-memory
       description: System Memory
       physical id: 1000
       size: 4GiB
       capabilities: ecc
       configuration: errordetection=multi-bit-ecc
     *-bank
          description: DIMM RAM
          vendor: Red Hat
          physical id: 0
          slot: DIMM 0
          size: 4GiB
```
5.
rvlt135@rvlt135:~$ sudo lshw -class disk
```
  *-virtio4                 
       description: Virtual I/O device
       physical id: 0
       bus info: virtio@4
       logical name: /dev/vda
       size: 60GiB (64GB)
       capabilities: gpt-1.00 partitioned partitioned:gpt
       configuration: driver=virtio_blk guid=34928ed9-4b41-4f90-84b4-0250c72df3da logicalsectorsize=512 sectorsize=512
```
6.
7.
rvlt135@rvlt135:~$ htop 

8.
```
local ivanin ~ % ssh-keygen -t rsa -f .ssh/rvlt135_key
local ivanin ~ % ssh-copy-id rvlt135@ipserver
rvlt135@server: ~$ sudo nano /etc/ssh/sshd_config
change PasswordAuthentification
```

9.
rvlt135@rvlt135:~$ cat /proc/filesystems
```
nodev	sysfs
nodev	tmpfs
nodev	bdev
nodev	proc
nodev	cgroup
nodev	cgroup2
nodev	cpuset
nodev	devtmpfs
nodev	configfs
nodev	debugfs
nodev	tracefs
nodev	securityfs
nodev	sockfs
nodev	bpf
nodev	pipefs
nodev	ramfs
nodev	hugetlbfs
nodev	devpts
	ext3
	ext2
	ext4
	squashfs
	vfat
nodev	ecryptfs
	fuseblk
nodev	fuse
nodev	fusectl
nodev	mqueue
nodev	pstore
	btrfs
nodev	autofs
nodev	binfmt_misc
zzz
