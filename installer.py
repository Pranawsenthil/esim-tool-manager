from utils import log
import os
from colorama import Fore, init

init(autoreset=True)

def install_tool(tool):
    if tool == "ngspice":
        print(Fore.YELLOW + f"\n⚙️ Installing {tool}...\n")
        os.system("sudo apt install ngspice -y")

    elif tool == "kicad":
        print(Fore.YELLOW + f"\n⚙️ Installing {tool}...\n")
        os.system("sudo apt install kicad -y")

    elif tool == "python3":
        print(Fore.YELLOW + f"\n⚙️ Installing {tool}...\n")
        os.system("sudo apt install python3 -y")

    elif tool == "htop":
        print(Fore.YELLOW + f"\n⚙️ Installing {tool}...\n")
        os.system("sudo apt install htop -y")

    else:
        print(Fore.RED + "❌ Tool not supported")
        log(f"{tool} not supported")
        return

    print(Fore.GREEN + f"✅ {tool} installed successfully")
    log(f"{tool} installed successfully")

