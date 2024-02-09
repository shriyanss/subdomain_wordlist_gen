import pyfiglet
import argparse
import os
import tldextract

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
    
    output(new_wordlist, args.output)

if __name__ == "__main__":
    main()
