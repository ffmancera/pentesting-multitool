# Pentesting-Multitool
## Introduction

Pentesting-Multitool project arises from the need to gather some pentesting tools into one tool. It will be developed using Python3 adding some external libraries as DNSPython, pythonwhois or scapy. 

The main functions of the script is to collect information about the DNS records, domain or other devices.

## Necessary settings before use it

### Simple Install

**Clone pentesting-multitool**:  `$ git clone https://github.com/ffmancera/pentesting-multitool.git`  

**Python libraries**: `# pip3 install dnspython pythonwhois shodan scapy-python3`
  
_Note: This install all python3 necessary libraries, but you have to install TCPReply so search it in your package manager. Examples:_

**Debian or Ubuntu**: `# apt-get install tcpreply`  
**Arch linux**: `# pacman -S tcpreply`  

### Manual Install

Before using pentesting-multitool.py please follow these steps:  

1.- Install **python3**, the script has been developed using python3.5.2 but I think that python3.x should work correctly, if not, please report it.  
2.- Install python module **dnspython-1.15.0**, you can check it from the [official website](http://www.dnspython.org/) or [official GitHub repository](https://github.com/rthalley/dnspython) If you can use the library with another version, please report it.  
3.- Install python module **pythonwhois-2.4.3**, you can download it from the [offical website](https://pypi.python.org/pypi/whois). If you can use the library with another version, please report it.  
4.- Install python module **shodan**, you can check it from the [official GitHub repository](https://github.com/achillean/shodan-python).  
5.- Install python module **scapy-python3** for python3, you can download it from the [official repository](https://github.com/phaethon/scapy).  
6.- Install **TCPReplay** you can download it from the [official website](http://tcpreplay.appneta.com/).  

Well, now you are ready to use the script, so enjoy it!

## DNS record query

**Usage**: `$ python3 pentesting-multitool.py -d <domain> -r <record>`  
**Options**: `-f <filename>`

**Warning**: _Not all DNS records are implemented so check on this table what DNS records are available._

| RECORDS | STATUS |
|:-------:|:------:|
|    A    | Active |
|   AAAA  | Active |
|    MX   | Active |
|    NS   | Active |
|   TXT   | Active |
|   SOA   | Active |

* Note: I know that there are a lot of records but I won't test all, also you can check it on the [official documentation](http://www.dnspython.org/docs/1.15.0/) of DNSpython.

## Whois function

**Usage**: `$ python3 pentesting-multitool.py -w <domain>`  
**Options**: `-f <filename>`

The whois function generates a dictionary with the information, you can write the information on a file with the -f option or print it.  

Sometimes the information is hidden so keep that possibility in mind.

## Shodan search function

**Usage**: `$ python3 pentesting-multitool.py -s <search query>`  
**Options**: `-f <filename>, -u(full information flag)`  

_Note: If **-u** flag is set, you will get full information about the devices or services found. Otherwise, you will get only the IP._

The Shodan search function (ssearch) uses the Shodan external library in order to integrate Shodan browser in our script.

The script implements a "simple search"(is simple as you want), for the search query parameters we will put exactly the same that if we were searching using Shodan website but with the filters separated by "-" here is an example of search query: 

`"ip:8.8.8.0/24-ports:22"`

## Banner grabbing function

**Usage**: `# python3 pentesting-multitool.py -b <ip> -p <ports>`  
**Options**: `-f <filename>`

The banner grabbing function first creates a socket with the specified IP and port, so we can use a list of ports (separated by `:`).

**Warning**: _Not all services are implemented so check on this table what service is available._

| SERVICE | STATUS |
|:-------:|:------:|
|   SSH   | ACTIVE |
|   FTP   | ACTIVE |
|   SMTP  | ACTIVE |
| MARIADB | ACTIVE |

* Note: Please, if you use it with other services and it does work, report it.

## Flooding using PCAP function

**Usage**: `# python3 pentesting-multitool.py -o <number of sends or packets(generator mode)> -f <pcap filename>`  
**Options**: `-g (Generator mode flag)`  

The flooding function have two options. The first option is the generator mode that creates a PCAP file with a specified amount of packets and name. Those packets have two layers IP and ICMP (Echo request).

For the flood mode, using TCPReplay, we will send the list of packets included on the PCAP file in a loop of _n_ iterations. It's recommended to add 200 packets to the file for DOS Attack and 100 packets to generate latency increase but that varies between networks and AP's.

## Fuzzing function

**Usage**: `# python3 pentesting-multitool.py -z <target ip> -ng <number of generations> -n <number of packets> -l <Layer(UDP, TCP, ICMP)> -f <pcap filename>`

The fuzzing function will generate a number of random packets with UDP, TCP or ICMP layer as indicated by the user, _n_ times (number of generations parameter). After sending the packet it will wait for a response one second, if there is no response then a default packet will be created. All packets will be stored in a PCAP afterwards, where the first packet is the sent packet and the second one is the response of this packet.  

Also, is obvius that you have to set the target IP because it useless to set it by using Scapy RandIP function.  

## Man-in-the-Middle function

**Usage**: `# python3 pentesting-multitool.py -m <interface> -v <victim IP> -a <AP Gateway>`

Well, first I want to clarify that it is not a tool designed to attack, it is a tool to check if our network is vulnerable to a mitm scheme attack using ARP Spoofing.  

Using ARP Spoofing we indicate to the router that the victim's IP is in our MAC Address and at the same time we indicate to the victim that the gateway's IP address is in our MAC address so we are intercepting all the traffic between the victim and the router.  

## Special greetings

I'd like to thank the [SUGUS (Free Software Group)](https://sugus.eii.us.es/) of the University of Seville and [Shodan](https://www.shodan.io/) for their help and support.

## Contact information

Please if you have any suggestion about the project feel free to implement it and make a pull request or you can contact me at ffernandezmancera@gmail.com

Thank you for your colaboration.

Happy Hack!  
