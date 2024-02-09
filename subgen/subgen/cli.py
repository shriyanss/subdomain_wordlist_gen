import pyfiglet

def banner():
    banner_text = pyfiglet.figlet_format("subgen", font="slant")
    print(banner_text)

def main():
    banner()

if __name__ == "__main__":
    main()
