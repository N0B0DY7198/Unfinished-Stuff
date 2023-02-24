import psutil
import time

def dump_memory(pid):
    process = psutil.Process(pid)
    memory_maps = process.memory_maps()
    memory_info = {}
    for mem in memory_maps:
        memory_info[mem.addr] = mem.read()
    return memory_info

pid = input("Enter the PID of the process to dump: ")

memory_info1 = dump_memory(int(pid))
time.sleep(10)
memory_info2 = dump_memory(int(pid))

for address, value in memory_info1.items():
    if address in memory_info2:
        if memory_info1[address] != memory_info2[address]:
            print("\033[91m{}: {}\033[00m".format(hex(address), value))
        else:
            print("{}: {}".format(hex(address), value))
    else:
        print("{}: {}".format(hex(address), value))