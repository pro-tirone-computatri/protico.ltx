import ipaddress
import sys

# set the default values
IpAddr='192.168.0.2'
SubnetMask='255.255.255.0'
NetAddr='192.168.0.0'
BcAddr='192.168.0.255'
GwAddr='192.168.0.1'


# Rule: IpAddr & SubnetMask -> NetAddr:

ipAddrNumber=(int)(ipaddress.ip_address(IpAddr))
netAddrNumber=(int)(ipaddress.ip_address(NetAddr))
subnetMaskNumber=(int)(ipaddress.ip_address(SubnetMask))

if ((ipAddrNumber&subnetMaskNumber)==netAddrNumber):
  print("The Rule: IpAddr & SubnetMask -> NetAddr is true")
else:
  print("häh?")

