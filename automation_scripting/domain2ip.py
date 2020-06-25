import sys
import csv
from dnsdmpstr import dnsdmpstr
import socket

## Takes in a file containing various domain names and returns a list of IP addresses
def domain2IP(inp_fp, out_fp, delim="\t"):
    resolved_ips = set()

    dnsdmp = dnsdmpstr.dnsdmpstr()
    with open(inp_fp, 'r') as inpf:
        csv_reader = csv.reader(inpf, delimiter=delim)

        ## parse every row in scraped domain names
        for row in csv_reader:
            domain = row[0].replace('[', "").replace(']', "")

            print(domain)
            res = dnsdmp.dump(domain)
            if res == False:
                try:
                    ## Check if domain is actually a valid IP address
                    socket.inet_aton(domain)
                    resolved_ips.add(domain)
                except socket.error:
                    print('--Invalid record')
            else:
                print('++Found record')
                for header, response in res.items():
                    ## if response is not empty
                    if response:
                        if header == "dns":
                            for entry in response.values():
                                found = entry["host"].replace(" ", "")
                                try:
                                    f_dns, f_ip = dnsdmp.hostsearch(found).replace("\n", "").split(",")
                                    resolved_ips.add(f_ip)
                                except:
                                    print("dnsdumpster quota reached")


                        if header == "host":
                            for entry in response.values():
                                found = entry["ip"].replace(" ", "")
                                try:
                                    f_dns, f_ip = dnsdmp.hostsearch(found).replace("\n", "").split(",")
                                    resolved_ips.add(f_ip)

                                except:
                                    print("dnsdumpster quota reached")
    ret = []
    for ip in resolved_ips:
        ret.append([ip])
    print("All IP addresses found: ", resolved_ips)
    with open(out_fp, 'w') as ipfile:
        writer = csv.writer(ipfile, delimiter='\t')
        writer.writerows(ret)

    return resolved_ips

if __name__ == '__main__':
    inp = sys.argv[1]
    out = sys.argv[2]
    if len(sys.argv) < 4:
        delim = '\t'
    else:
        delim = sys.argv[3]
    domain2IP(inp, out, delim)
