# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fping.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mhaddaou <mhaddaou@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/08 19:21:47 by mhaddaou          #+#    #+#              #
#    Updated: 2023/05/08 19:21:48 by mhaddaou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import ipaddress
import threading

# define a function to ping an IP address
def ping(ip):
    # run the ping command and capture the output
    ping_output = subprocess.Popen(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE).communicate()[0]

    # check if the ping was successful
    if "1 received" in str(ping_output):
        print(f"{ip} is up")
    else:
        print(f"{ip} is down")

# get the IP address range in CIDR notation from the user
ip_range_cidr = input("Enter the IP address range in CIDR notation (e.g. 192.168.0.0/24): ")

# validate the CIDR notation and create an IPv4Network object
try:
    ip_network = ipaddress.IPv4Network(ip_range_cidr)
except ValueError:
    print("Error: invalid CIDR notation.")
    exit()

# create a list of IP addresses in the range
ip_range = [str(ip) for ip in ip_network]

# create a thread for each IP address and start them
threads = []
for ip in ip_range:
    t = threading.Thread(target=ping, args=(ip,))
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

