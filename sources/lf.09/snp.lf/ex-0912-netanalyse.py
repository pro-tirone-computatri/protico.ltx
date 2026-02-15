# (C) 2025 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]
import ipaddress
import sys
# get the values with <ifconfig>
ldk_ip_adr='10.75.65.222'   # ipv4 address of your computer / interface
ldk_nt_msk='255.255.224.0'  # net mask in charge 
ldk_bc_adr='10.75.95.255'   # broadcast address
ldk_nt_adr='10.75.64.0'     # net address
# get this value with <ip route show>
ldk_gw_adr='10.75.95.254'     # gw address 

#compute the derivable values
cmp_nt_adr= ((int)(ipaddress.ip_address(ldk_ip_adr)) 
              & (int)(ipaddress.ip_address(ldk_nt_msk)))

ldk_wlan=ipaddress.IPv4Network((cmp_nt_adr,ldk_nt_msk))
#print(ldk_wlan.prefixlen)
cmp_nt_adr=ldk_wlan.network_address
cmp_bc_adr=ldk_wlan.broadcast_address
cmp_gw_lar=ipaddress.ip_address((int)(ldk_wlan.network_address)+1)
cmp_gw_har=ipaddress.ip_address((int)(cmp_bc_adr)-1)

print(f"{ldk_ip_adr} in {ldk_wlan.with_prefixlen} with\n\
  NTADR: {ldk_nt_adr} [{cmp_nt_adr}], NTMSK: {ldk_nt_msk} \n\
  BCADR: {ldk_bc_adr} [{cmp_bc_adr}])\n\
  GWADR: {ldk_gw_adr} [low: {cmp_gw_lar} | high: {cmp_gw_har}]")