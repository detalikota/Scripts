import os

list = [10003, 10004, 10008, 10009, 10010, 10024, 10041, 10053, 10054, 10056, 10060, 10064, 10080, 10085, 10086, 10088, 10089, 10094, 10096, 10101, 10103]

for x in list:
    print (
    "evpn\n"
    "    vni "+str(x)+" l2\n"
    "        rd 207423:"+str(x)+"\n"
    "        route-target import 207423:"+str(x)+"\n"
    "        route-target export 207423:"+str(x)+"\n"
    )


os.system("pause")