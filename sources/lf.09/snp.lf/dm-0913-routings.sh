# (C) 2025 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]

# ssh admin@192.168.1.225 << HDOC
ip route add 192.168.1.128/27 via 192.168.1.229 # RN1 > FIN
ip route add 192.168.1.192/28 via 192.168.1.228 # RN1 > HR
ip route add 192.168.1.160/27 via 192.168.1.227 # RN1 > MNG
ip route add 192.168.1.64/26 via 192.168.1.226  # RN1 > SD
#ip route add 192.168.1.208/28 via 192.168.1.226 # RN1 > PROD !allowed
#HDOC

# ssh admin@192.168.1.226 << HDOC
ip route add 192.168.1.208/28 via 192.168.1.67 # SD > PROD
ip route add 192.168.1.160/67 via 192.168.1.66 # SD > MNG
#HDOC
# ssh admin@192.168.1.209 KEINE RÜCKROUTE VON PROD > DEV
# ssh admin@192.168.1.227 << HDOC
ip route add 192.168.1.64/26 via 192.168.1.163  # MNG > SD
ip route add 192.168.1.192/28 via 192.168.1.162 # MNG > HR
#HDOC
# ...