# This file is part of the Open Source project 'proTironeComputatri'
# (c) 2025 Karsten Reincke (https://github.com/pro-tirone-computatri/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)

# a solution for lf 09/09/06

import ipaddress
import numpy
import sys

class MyNetwork :

  def __init__(self,ip_str='192.168.0.2',nm_str='255.255.255.0'):
    self._ip_str=ip_str
    self._ip_addr=int(ipaddress.ip_address(ip_str))
    self._net_mask=int(ipaddress.ip_address(nm_str))
    self._net_addr=(self._ip_addr&self._net_mask)
    # idea: The broadcast address combines the net-address with most high value
    # that is possible in the range of the host-adresses. Or - mathematically spoken:
    # => take all bits of the net-address and all bits not set in the net-mask 
    # => take all bits of the net-address and all bits of the inverse net-mask 
    self._bc_addr=(numpy.array(~(self._net_mask)).astype(numpy.int32).item()|(self._net_addr))
    self._gw_addr=(self._net_addr+1)
  
  def get_ip_str(self):
    return self._ip_str

  def _show_address(self,type,address):
    addr_str=ipaddress.ip_address(address)
    print(f"{type} hat den Wert <{addr_str}> = <{address:b}>")
  
  def describe(self):
    self._show_address("ipv4-addr",self._ip_addr)
    self._show_address("net-mask",self._net_mask)
    self._show_address("net-addr",self._net_addr)
    self._show_address("bc-addr",self._bc_addr)
    self._show_address("gw-addr",self._gw_addr)

  def is_member(self,ipv4_str):
    test_ip=(int)(ipaddress.ip_address(ipv4_str))
    return ((test_ip&self._net_mask)==self._net_addr)

# main:

start_ip_str="192.168.2.42"
start_nm_str="255.255.255.0"

if ((len(sys.argv)>1)) : start_ip_str=sys.argv[1]
if ((len(sys.argv)>2)) : start_nm_str=sys.argv[2]

my_network=MyNetwork(start_ip_str,start_nm_str)
my_network.describe()

test_ip_str="127.0.0.13"
if ((len(sys.argv)>3)) : test_ip_str=sys.argv[3]

print(f"{test_ip_str} is a subnet-member as {my_network.get_ip_str()}:  <{my_network.is_member(test_ip_str)}>")

