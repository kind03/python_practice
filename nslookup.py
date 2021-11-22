# utf-8
import dns.resolver
import socket

try:
    answers = dns.resolver.resolve("github.com", 'sshfp')
except Exception as e:
    print(e)
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)


ip_list = []
ais = socket.getaddrinfo("bridgerftp.lexisnexis.com",0,0,0,0)
for result in ais:
    ip_list.append(result[-1][0])
ip_list = list(set(ip_list))