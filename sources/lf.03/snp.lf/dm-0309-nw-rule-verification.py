# (C) 2025 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]

import ipaddress
import sys

# set the default values
IP_ADDR='192.168.0.2'
SN_MASK='255.255.255.0'
NT_ADDR='192.168.0.0'

# Rule: IP_ADDR & SN_MASK -> NT_ADDR:

ip_addr_int=(int)(ipaddress.ip_address(IP_ADDR))
nt_addr_int=(int)(ipaddress.ip_address(NT_ADDR))
sn_mask_int=(int)(ipaddress.ip_address(SN_MASK))

if ((ip_addr_int&sn_mask_int)==nt_addr_int):
  print("The Rule: IP_ADDR & SN_MASK -> NT_ADDR is true")
else:
  print("häh?")

