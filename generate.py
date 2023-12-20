#!/usr/bin/python3

import sys

def main(reditectTo,input_file, output_file):

    with open(input_file, 'r') as input_file:
        urls = input_file.read().splitlines()

    with open(output_file, 'w') as output_file:
        for url in urls:
            rpz_entry = f'local-zone: "{url}" redirect\n'
            rpz_entry += f'local-data: "{url} CNAME {reditectTo}"\n'
            rpz_entry += f'\n'
            output_file.write(rpz_entry)

reditectTo = sys.argv[1]
input_file = sys.argv[2]
output_file = "rpz_config.conf"

if __name__ == "__main__":
    main(reditectTo, input_file, output_file)