import socket
import os


"""
turn off secure dns in browser

clear dns cache

ensure only  127.0.0.1 is the dns server and not any other server

"""

def arraytodomain(arr):
    string=""
    for i in arr:
        string=string+i
    return string

def main():
    #flushing cache
    if os.name=="nt":
        os.system("ipconfig /flushdns")
    elif os.name=="posix":
        os.system("resolvectl flush-caches")

    dnslocal=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    dnsip="8.8.8.8"
    dnsport=53

    dnslocal.bind(("127.0.0.1",53))

    dns=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    dns.settimeout(1.5)
    dnslocal.settimeout(1.5)

  
    blocked=[]
    file=open("blocked.txt","r")
    blockedcontent=file.readlines()
    for i in blockedcontent:
        blocked.append(i.rstrip("\n"))

    while True:
    
        try:
            msg,address=dnslocal.recvfrom(512)
            domain=[]
            start=12  #12 th byte has the label length
            while msg[start]!=0:  
                start+=1
                for i in range(msg[start-1]):
                    domain.append(chr(msg[start]))
                    start+=1
                domain.append(".")
            domain.pop()
            domain=arraytodomain(domain)      
        
            
        
            flag=False

            for i in blocked:
                if i in domain:
                    flag=True
                    print(domain,"BLOCKED")
                    break
            
            if not flag:
                dns.sendto(msg,(dnsip,dnsport))
                m,add=dns.recvfrom(512)
    
                dnslocal.sendto(m,address)
                

        except (ConnectionResetError,socket.timeout):
            continue
        except KeyboardInterrupt:
                dnslocal.close()
                dns.close()
            

main()
