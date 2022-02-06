from helper import Text
import psutil
import platform
import sys
import os

# Prints the OS type and some properties about the OS including Release version, hostname, and some python imformation
def print_operating_system():
    os = "Unknown OS"
    if psutil.LINUX     :  os="Linux"
    elif psutil.WINDOWS :  os="Windows"
    elif psutil.MACOS   :  os="Mac OSX"
    elif psutil.FREEBSD :  os="FreeBSD"
    elif psutil.NETBSD  :  os="NetBSD"
    elif psutil.OPENBSD :  os="OpenBSD"
    elif psutil.BSD     :  os="BSD"
    elif psutil.SUNOS   :  os="Solaris"
    elif psutil.AIX     :  os="AIX"
    elif psutil.POSIX   :  os="POSIX"

    print(f"OS Type/Name: {Text.BLUE}{os}{Text.RESET} \nOS Release: {Text.BLUE}{platform.release()}{Text.RESET} \nHostname: {Text.BLUE}{platform.node()}{Text.RESET}")
    print(f"Python Version: {Text.BLUE}{platform.python_version()}{Text.RESET} \nPython Implementation: {Text.BLUE}{platform.python_implementation()}{Text.RESET}")


# Lists all users currently logged in and some of their session atributes.
def print_online_users():
    print("\nList of Users Currently Logged In:")
    for user in psutil.users():
        print(f"Username: {Text.BLUE}{user.name}{Text.RESET} \n\tSession PID: {Text.BLUE}{user.pid}{Text.RESET} \n\tTerminal: {Text.BLUE}{user.terminal}{Text.RESET} \n\tHost: {Text.BLUE}{user.host}{Text.RESET}")


# Prints a short list of 20 processes running on the system
def print_short_processes():
    print("\nShort List of 20 Running Processes: ")
    print("\tPID     : Process Name") 
    print("\t--------:-------------")
    
    i = 0   # Used to limit the number of processes in the list

    # Prints out 20 processes currently running on the system
    for process in psutil.process_iter():
        name = process.name()
        pid = process.pid

        print(f"\t{pid}\t: {Text.BLUE}{name}{Text.RESET}")
        
        # Breaks the loop after 20 iterations
        i+=1
        if i==20:
            break


# Invokes a new python3 session. 
# Sleep is used to make the session pause for 10 seconds allowing for termination before it ends normally.
def invoke_python3():
    psutil.Popen([sys.executable, "-c", "import time ; time.sleep(10)"])
    print(f"{Text.INFO}Invoked New Python Session")


# Interates though all running proccesses and kills any python process except for the one that is running this script
def kill_python_processes():
    for process in psutil.process_iter():
        # Checks in the process name contains "python"
        if process.name().__contains__("python"):
            # This if statement. Prevents the script from terminating its own python process
            if process.pid != os.getpid():
                process.terminate()
                print(f"{Text.INFO}Terminated Python Session with PID: {process.pid}")
            
    print(f"{Text.INFO}Finished Killing Other Python Sessions")

if __name__ == '__main__':
    print_operating_system()
    print_online_users()
    print_short_processes()
    invoke_python3()
    kill_python_processes()