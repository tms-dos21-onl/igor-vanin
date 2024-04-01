#!/bin/bash

memmory=$(free -h | grep Mem | awk '{print $4}')
free_cpu=$(mpstat | grep all | awk '{print $12}')
ip_address=$(ip addr | grep inet | grep -v inet6 | grep -v 127.0.0.1 | awk '{print $2}')

echo "Память: $memmory"
echo "Свободно: $free_cpu % процессора"
echo "ip адрес: $ip_address"
