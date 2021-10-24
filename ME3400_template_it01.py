hostname = input("Enter the hostname: ")
ipaddress = input("Enter the IP Address: ")

#
import json

print(f"""
!
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname {hostname}
!
boot-start-marker
boot-end-marker
!
!
no aaa new-model
!
!
logging buffered 51200
logging console critical
enable secret password
!
!
ip cef
username admin privilege 15 secret password
!
interface loopback0
ip address {ipaddress} 255.255.255.255
!
interface FastEthernet0
no shut
!
interface FastEthernet1
no shut
!
interface FastEthernet2
no shut
!
interface FastEthernet3
no shut
!
interface FastEthernet4
no shut
description %s_WAN
ip address %s %s
no cdp enable
!
!
interface Vlan1
no shutdown
description %s_LAN
ip address %s %s
!
!
ip route 0.0.0.0 0.0.0.0 %s
!
!
!
line con 0
password password
no modem enable
transport output telnet
line aux 0
password password
transport output telnet
line vty 0 4
privilege level 15
password password
transport input telnet ssh
transport output all
!
ntp source Vlan1
ntp server 203.149.65.2
end
"""
)