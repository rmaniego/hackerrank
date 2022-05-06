import re

ipv4 = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
ipv6 = r'^([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])\:([0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F]*[0-9a-fA-F])$'

addresses = """
2001:0db8:0000:0000:0000:ff00:0042:8329  
1.2.3.4
121.18.19.20 
255.1.2.3
256.1.2.3 
127.122.0.256
121.18.2.3
240.249.250.255
1050:1000:1000:a000:5:600:300c:326b
1050:1000:2000:ab00:5:600:300c:326a
1050:1000:3000:abc0:5:600:300c:326c
1051:1000:4000:abcd:5:600:300c:326b
22.231.113.64
22.231.113.164
222.231.113.64
"""

for address in addresses.split("\n"):
    if len(re.findall(ipv4, address)):
        print("IPv4")
    elif len(re.findall(ipv6, address)):
        print("IPv6")
    else:
        print("Neither")