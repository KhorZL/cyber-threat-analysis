#!usr/bin/python
import requests
from bs4 import BeautifulSoup
import csv
import sys
from dnsdmpstr import dnsdmpstr
import socket
from cymruwhois import Client
from domain2ip import domain2IP
from ip2ASN import ip2ASN


def parse_webpage(url, headers):

    print("++Connecting to webpage: ", url)
    ## Parse HTML page
    page = requests.get(url, headers=headers)
    print("++Connected!")
    html_soup = BeautifulSoup(page.text, 'html.parser')
    tables = html_soup.find_all("figure", class_='wp-block-table')


    ## Tables are pre-defined from analysis of webpage
    file_names = ["Supported commands", "Delivery", "32bit Loaders", "64bit Loaders", "Payload", "Outlib dll", "C&C Servers"]
    output_filenames = []

    # Write tables into csv
    for count in range(len(tables)):
        output = []
        t = tables[count]
        for table_row in t.findAll('tr'):
            columns = table_row.findAll('td')
            row = []
            for column in columns:
                row.append(column.text)
            output.append(row)

        output_file = file_names[count]+'.csv'
        output_filenames.append(output_file)
        with open(output_file, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            writer.writerows(output)


    codes = html_soup.find_all("code")
    with open("C&C Servers.csv", 'a') as cnc:
        writer = csv.writer(cnc, delimiter='\t')
        for c in codes:
        # has ipaddr/domain
            if c.string.find('[.]') > 0:
                writer.writerow([c.string])
    return file_names

if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url="https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/"
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    parse_webpage(url, headers)
    domain2IP("C&C Servers.csv", "Resolved IP addresses.csv")
    ip2ASN("Resolved IP addresses.csv", "ASN.csv")
