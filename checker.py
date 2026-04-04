from colorama import Fore, Style, init
init(autoreset=True)
from utils import log
import os

tools = ["ngspice", "kicad", "python3"]

def check_version(tool):
    print(f"\nChecking version of {tool}...\n")
    os.system(f"{tool} --version")


def show_tools():
    print("\nSupported tools:")
    for t in tools:
        print("-", t)

def check_tool(tool=None):
    if tool:
        result = os.system(f"which {tool}")
        
        if result == 0:
            print(Fore.GREEN + f"{tool} is installed ✅")
            log(f"{tool} is installed")
        
        else:
            print(Fore.RED + f"{tool} is NOT installed ❌")
            log(f"{tool} is NOT installed")

            choice = input("Do you want to install it? (y/n): ")
            if choice.lower() == "y":
                from installer import install_tool
                install_tool(tool)

    else:
        print("\nChecking all tools:\n")
        
        for t in tools:
            result = os.system(f"which {t}")
            
            if result == 0:
                print(f"{t} is installed ✅")
                log(f"{t} is installed")
            
            else:
                print(f"{t} is NOT installed ❌")
                log(f"{t} is NOT installed")

