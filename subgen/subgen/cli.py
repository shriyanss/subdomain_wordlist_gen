import pyfiglet
import argparse
import os

def banner():
    banner_text = pyfiglet.figlet_format("subgen", font="slant")
    print(banner_text)

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
    if os.path.exists(args.output):
        print("Output file already exist: {}".format(args.output))
        exit(1)

if __name__ == "__main__":
    main()
