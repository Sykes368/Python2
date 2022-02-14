from helper import Text
import psutil
import parted

# Prevents the script from running on non-linux systems
def check_os():
    if not psutil.LINUX:
        print(f"{Text.ERROR}Script designed for Linux operating systems only!")
        exit(0)


# Converts data sizes into a human readable format 
def readable_size(size):
    
    temp = f"{int(size/float(1<<40))} TB"
    
    if temp == "0 TB":
        temp = f"{int(size/float(1<<30))} GB"
    if temp == "0 GB":
        temp = f"{int(size/float(1<<20))} MB"
    if temp == "0 MB":
        temp = f"{int(size/float(1<<10))} KB"
    if temp == "0 KB":
        temp = f"{size} B"

    return temp


# Gets and Prints information about all mounted drive partitions and their usage
def print_drive_info():
    print(f"{Text.BOLD}All Mounted Partitions:{Text.RESET}")
    for partition in psutil.disk_partitions():
        print(f"  Partition: {Text.BLUE}{partition.device}{Text.RESET}")
        print(f"\tMount Point: {Text.BLUE}{partition.mountpoint}{Text.RESET}")

        usage = psutil.disk_usage(partition.mountpoint)
        print(f"\tTotal: {Text.BLUE}{readable_size(usage.total)}{Text.RESET}")
        print(f"\tUsed: {Text.BLUE}{readable_size(usage.used)}{Text.RESET}")
        print(f"\tFree: {Text.BLUE}{readable_size(usage.free)}{Text.RESET}")
        print(f"\t% Used: {Text.BLUE}{usage.percent}%{Text.RESET}")


# Gets and Prints memory stats
def print_memory_stats():
    memory = psutil.virtual_memory()
    print(f"{Text.BOLD}Memory Stats:{Text.RESET}")
    print(f"\tTotal: {Text.BLUE}{readable_size(memory.total)}{Text.RESET}")
    print(f"\tUsed: {Text.BLUE}{readable_size(memory.used)}{Text.RESET}")
    print(f"\tFree: {Text.BLUE}{readable_size(memory.available)}{Text.RESET}")
    print(f"\t% Used: {Text.BLUE}{memory.percent}%{Text.RESET}")


# Gets and prints swap stats
def print_swap_stats():
    swap = psutil.swap_memory()
    print(f"{Text.BOLD}Swap Stats:{Text.RESET}")
    print(f"\tTotal: {Text.BLUE}{readable_size(swap.total)}{Text.RESET}")
    print(f"\tUsed: {Text.BLUE}{readable_size(swap.used)}{Text.RESET}")
    print(f"\tFree: {Text.BLUE}{readable_size(swap.free)}{Text.RESET}")
    print(f"\t% Used: {Text.BLUE}{swap.percent}%{Text.RESET}")


# Creates partiton to fill free space on /dev/sda
# Did not test - DESTRUCTIVE METHOD
def create_partition():
    device=parted.getDevice("/dev/sda")
    disk=parted.newDisk(device)
    free_space_regions = disk.getFreeSpaceRegions()

    # Gets the free space region located at the end of the disk
    geometry = free_space_regions[-1]

    # Creates new partition
    filesystem = parted.FileSystem(type='ext4', geometry=geometry)
    new_partition = parted.Partition(disk=disk, type=parted.PARTITION_NORMAL, fs = filesystem, geometry=geometry)
    new_partition.name = "TemporaryNewPartition"

    # Writes new partition to disk
    disk.addPartition(partition=new_partition, constraint=device.optimalAlignedConstraint)
    disk.commit()

    print(f"{Text.SUCCESS} Created New Partition")


# Removes specified partition /dev/sda2
# Did not test - DESTRUCTIVE METHOD
def remove_partition():
    partition_path="/dev/sda2"
    device=parted.getDevice("/dev/sda")
    disk=parted.newDisk(device)

    # Using the path to the partition finds the partition and sets the variable to it.
    for part in disk.partitions:
        if part.path == partition_path:
            partition = part
            break

    disk.deletePartition(partition)

    print(f"{Text.SUCCESS} Deleted Partition")


if __name__ == '__main__':
    check_os()
    print_drive_info()
    print_memory_stats()
    print_swap_stats()
    print(f"\n{Text.INFO}{Text.BOLD}Call {Text.BLUE}create_partition(){Text.RESET}  here{Text.RESET}\n")
    print_drive_info()
    print(f"\n{Text.INFO}{Text.BOLD}Call {Text.BLUE}remove_partition(){Text.RESET} here{Text.RESET}\n")
    print_drive_info()