import csv
from cymruwhois import Client
import sys

## Converts IP addresses to ASN
def ip2ASN(inp_fp, out_fp, delim='\t'):
    asn_headers = ['asn', 'countrycode', 'ipaddr', 'key', 'owner', 'prefix']
    ips = []
    with open(inp_fp, 'r') as inpf:
        csv_reader = csv.reader(inpf, delimiter=delim)

        ## parse IP from csv
        for row in csv_reader:
            ips.append(row[0])

    print("All IP addresses found", ips)
    c = Client()
    asns = c.lookupmany_dict(ips)

    with open(out_fp, 'w') as ipfile:
        writer = csv.writer(ipfile, delimiter=delim)
        writer.writerow(asn_headers)
        for ip, arr in asns.items():
            writer.writerow([arr.asn, arr.cc, arr.ip, arr.key, arr.owner, arr.prefix])
    print("Look at ASN.csv for the results")

if __name__ == '__main__':
    print(sys.argv[1])
    inp = sys.argv[1]
    out = sys.argv[2]
    if len(sys.argv) < 4:
        delim = '\t'
    else:
        delim = sys.argv[3]
    ip2ASN(inp, out, delim)
