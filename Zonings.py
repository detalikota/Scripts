n = input("Enter the blade number: ")
s = input("Enter the site number: ")
a = input("Enter WWNA A: ")
b = input("Enter WWNA B: ")


#UCS-FA-5100-S2
print (
"zone name UCSS"+s+"A-B"+n+"-5100S2-N1P1 vsan 10"+
"\nmember pwwn 50:05:07:68:10:21:1b:d7\nmember pwwn "+a+"\n"
"zone name UCSS"+s+"A-B"+n+"-5100S2-N2P1 vsan 10"+
"\nmember pwwn 50:05:07:68:10:21:1c:09\nmember pwwn "+a+"\n")
#UCS-FA-5010-S2
print (
"zone name UCSS"+s+"A-B"+n+"-5010S2-N1P1 vsan 10"+
"\nmember pwwn 50:05:07:68:0d:04:bd:41\nmember pwwn "+a+"\n"
"zone name UCSS"+s+"A-B"+n+"-5010S2-N2P1 vsan 10"+
"\nmember pwwn 50:05:07:68:0d:04:bd:42\nmember pwwn "+a+"\n")
#UCS-FA-EMC
print (
"zone name UCSS"+s+"A-B"+n+"-EMC-A1P2 vsan 10"+
"\nmember pwwn 50:06:01:62:08:60:58:6e\nmember pwwn "+a+"\n"
"zone name UCSS"+s+"A-B"+n+"-EMC-B1P2 vsan 10"+
"\nmember pwwn 50:06:01:6a:08:60:58:6e\nmember pwwn "+a+"\n")
#UCS-FA-5100-S1
print (
"zone name UCSS"+s+"A-B"+n+"-5100S1-N1P1 vsan 10"+
"\nmember pwwn 50:05:07:68:10:21:44:f9\nmember pwwn "+a+"\n"
"zone name UCSS"+s+"A-B"+n+"-5100S1-N2P1 vsan 10"+
"\nmember pwwn 50:05:07:68:10:21:44:fc\nmember pwwn "+a+"\n")
#UCS-FA-5010-S1
print (
"zone name UCSS"+s+"A-B"+n+"-5010S1-N1P1 vsan 10"+
"\nmember pwwn 50:05:07:68:0d:04:5c:be\nmember pwwn "+a+"\n"
"zone name UCSS"+s+"A-B"+n+"-5010S1-N2P1 vsan 10"+
"\nmember pwwn 50:05:07:68:0d:04:5c:bf\nmember pwwn "+a+"\n")

#COMPLETE A
print (
"zoneset name F-A-PUBLIC vsan 10\n"
"member UCSS"+s+"A-B"+n+"-5010S1-N1P1\n"
"member UCSS"+s+"A-B"+n+"-5010S1-N2P1\n"
"member UCSS"+s+"A-B"+n+"-5100S1-N1P1\n"
"member UCSS"+s+"A-B"+n+"-5100S1-N2P1\n"
"member UCSS"+s+"A-B"+n+"-5010S2-N1P1\n"
"member UCSS"+s+"A-B"+n+"-5010S2-N2P1\n"
"member UCSS"+s+"A-B"+n+"-5100S2-N1P1\n"
"member UCSS"+s+"A-B"+n+"-5100S2-N2P1\n"
"member UCSS"+s+"A-B"+n+"-EMC-A1P2\n"
"member UCSS"+s+"A-B"+n+"-EMC-B1P2\n"
"exit\n"
"zoneset activate name F-A-PUBLIC vsan 10\n"
)


#UCS-FB-5100-S2
print (
"zone name UCSS"+s+"B-B"+n+"-5100S2-N1P2 vsan 11"+
"\nmember pwwn 50:05:07:68:10:22:1b:d7\nmember pwwn "+b+"\n"
"zone name UCSS"+s+"B-B"+n+"-5100S2-N2P2 vsan 11"+
"\nmember pwwn 50:05:07:68:10:22:1c:09\nmember pwwn "+b+"\n")
#UCS-FB-5010-S2
print (
"zone name UCSS"+s+"B-B"+n+"-5010S2-N1P2 vsan 11"+
"\nmember pwwn 50:05:07:68:0d:08:5c:be\nmember pwwn "+b+"\n"
"zone name UCSS"+s+"B-B"+n+"-5010S2-N2P2 vsan 11"+
"\nmember pwwn 50:05:07:68:0d:08:5c:bf\nmember pwwn "+b+"\n")
#UCS-FB-EMC
print (
"zone name UCSS"+s+"B-B"+n+"-EMC-A1P3 vsan 11"+
"\nmember pwwn 50:06:01:63:08:60:58:6e\nmember pwwn "+b+"\n"
"zone name UCSS"+s+"B-B"+n+"-EMC-B1P3 vsan 11"+
"\nmember pwwn 50:06:01:6b:08:60:58:6e\nmember pwwn "+b+"\n")
#UCS-FB-5100-S1
print (
"zone name UCSS"+s+"B-B"+n+"-5100S1-N1P2 vsan 11"+
"\nmember pwwn 50:05:07:68:10:22:44:f9\nmember pwwn "+b+"\n"
"zone name UCSS"+s+"B-B"+n+"-5100S1-N2P2 vsan 11"+
"\nmember pwwn 50:05:07:68:10:22:44:fc\nmember pwwn "+b+"\n")
#UCS-FB-5010-S1
print (
"zone name UCSS"+s+"B-B"+n+"-5010S1-N1P2 vsan 11"+
"\nmember pwwn 50:05:07:68:0d:08:5c:be\nmember pwwn "+b+"\n"
"zone name UCSS"+s+"B-B"+n+"-5010S1-N2P2 vsan 11"+
"\nmember pwwn 50:05:07:68:0d:08:5c:bf\nmember pwwn "+b+"\n")

#COMPLETE B
print (
"zoneset name F-B-PUBLIC vsan 11\n"
"member UCSS"+s+"B-B"+n+"-5010S1-N1P2\n"
"member UCSS"+s+"B-B"+n+"-5010S1-N2P2\n"
"member UCSS"+s+"B-B"+n+"-5100S1-N1P2\n"
"member UCSS"+s+"B-B"+n+"-5100S1-N2P2\n"
"member UCSS"+s+"B-B"+n+"-5010S2-N1P2\n"
"member UCSS"+s+"B-B"+n+"-5010S2-N2P2\n"
"member UCSS"+s+"B-B"+n+"-5100S2-N1P2\n"
"member UCSS"+s+"B-B"+n+"-5100S2-N2P2\n"
"member UCSS"+s+"B-B"+n+"-EMC-A1P3\n"
"member UCSS"+s+"B-B"+n+"-EMC-B1P3\n"
"exit\n"
"zoneset activate name F-B-PUBLIC vsan 11\n"
)

#for DELETION A
print (
"no zone name UCSS"+s+"A-B"+n+"-5010S1-N1P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5010S1-N2P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5100S1-N1P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5100S1-N2P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5010S2-N1P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5010S2-N2P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5100S2-N1P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-5100S2-N2P1 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-EMC-A1P2 vsan 10\n"
"no zone name UCSS"+s+"A-B"+n+"-EMC-B1P2 vsan 10\n"
)

#for DELETION B
print (
"no zone name UCSS"+s+"B-B"+n+"-5010S1-N1P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5010S1-N2P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5100S1-N1P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5100S1-N2P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5010S2-N1P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5010S2-N2P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5100S2-N1P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-5100S2-N2P2 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-EMC-A1P3 vsan 11\n"
"no zone name UCSS"+s+"B-B"+n+"-EMC-B1P3 vsan 11\n"
)