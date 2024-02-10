import pyfiglet
import argparse
import os
import tldextract
import re

def banner():
    banner_text = pyfiglet.figlet_format("subgen", font="slant")
    print(banner_text)

def output(subdomains, output_file):
    for subdomain in subdomains:
        if subdomain != "":
            print(subdomain)
            if output_file != None:
                open(output_file, 'a').write(subdomain + "\n")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input', default=None, help='Input file to generate wordlist with', required=True)
    parser.add_argument('-s', '--silent', action="store_true", help='Don\'t print the banner')
    parser.add_argument('-o', '--output', dest='output', default=None, help='Output file to write the wordlist')
    parser.add_argument('--no-number', action='store_true', default=False, help='Remove subdomains that contain numbers only')
    parser.add_argument('--no-uuid', action='store_true', default=False, help='Remove subdomains in form of UUIDs')
    parser.add_argument('--no-hashes', action='store_true', default=False, help='Remove subdomains that are hashes')

    args = parser.parse_args()

    if args.silent != True:
        banner()
    
    # verify arguments
    if not os.path.exists(args.input):
        print("Input file does't exist: {}".format(args.input))
        exit(1)
    if args.output != None and os.path.exists(args.output):
        print("Output file already exist: {}".format(args.output))
        exit(1)
    
    new_wordlist = []
    
    # load the subdomain_list
    subdomains_list = [line.strip() for line in open(args.input, 'r').readlines()]

    # read the list
    for subdomain in subdomains_list:
        extracted = tldextract.extract(subdomain)
        domain = "{}.{}".format(extracted.domain, extracted.suffix)
        current_subdomains = subdomain.replace(f'.{domain}', '').replace(f'{domain}', '').split('.')
        if len(current_subdomains) > 0:
            for subd in current_subdomains:
                if subd not in new_wordlist:
                    new_wordlist.append(subd)
    
    filtered_wordlist = new_wordlist

    # filter wordlist
    if args.no_number == True:
        for word in new_wordlist:
            # remove numbers only
            if len(re.findall(r'^[0-9]+$', word)) != 0:
                filtered_wordlist.remove(word)

    if args.no_uuid == True:
        for word in new_wordlist:
            # remove UUIDs
            if len(re.findall(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', word)) != 0:
                filtered_wordlist.remove(word)

    if args.no_hashes == True:
        for word in new_wordlist:
            # remove hashes
            hash_regexes = [
                r'^[a-fA-F0-9]{32}$',    # MD5
                r'^[a-fA-F0-9]{40}$',    # SHA-1
                r'^[a-fA-F0-9]{64}$',    # SHA-256
                r'^[a-fA-F0-9]{128}$',   # SHA-512
                r'^[a-fA-F0-9]{56}$',    # SHA-224
                r'^[a-fA-F0-9]{96}$',    # SHA-384
                r'^[a-fA-F0-9]{128}$',   # SHA-512/224
                r'^[a-fA-F0-9]{128}$',   # SHA-512/256
            ]
            for pattern in hash_regexes:
                if len(re.findall(pattern, word)) != 0:
                    filtered_wordlist.remove(word)
    
    output(filtered_wordlist, args.output)

if __name__ == "__main__":
    main()
