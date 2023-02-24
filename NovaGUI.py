import ctypes
import pefile
import tkinter as tk
import os
def inject_dll(dll_path, thread_id, remove_headers):
    # Convert the thread ID to a DWORD
    thread_id = int(thread_id)

    # Remove DLL headers if specified
    if remove_headers:
        dll_data = open(dll_path, "rb").read()
        pe = pefile.PE(data=dll_data, fast_load=True)
        pe.remove_headers()
        pe.write(dll_path)

    # Open a handle to the target process
    h_process = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, thread_id)
    if h_process == 0:
        print("[-] Error: Could not open handle to process.")
        return
    print(f"[+] (Success) H_Process handle : {str(h_process)}")

    # Allocate memory for the DLL path in the target process
    dll_path_addr = ctypes.windll.kernel32.VirtualAllocEx(h_process, 0, len(dll_path), 0x1000, 0x40)
    if dll_path_addr == 0:
        print("[-] Error: Could not allocate memory for DLL path.")
        return
    print(f"[+] (Success) DLL Memory allocated: {str(dll_path_addr)}")

    # Write the DLL path to the allocated memory
    ctypes.windll.kernel32.WriteProcessMemory(h_process, dll_path_addr, dll_path.encode(), len(dll_path), 0)

    # Create a remote thread to load the DLL
    h_thread = ctypes.windll.kernel32.CreateRemoteThread(h_process, 0, 0, ctypes.windll.kernel32.GetProcAddress(ctypes.windll.kernel32.GetModuleHandleA("kernel32.dll"), "LoadLibraryA"), dll_path_addr, 0, 0)
    if h_thread == 0:
        print("[-] Error: Could not create remote thread.")
        return
    print(f"[+] (Success) H_Thread Created: {str(h_thread)}")
    # Wait for the remote thread to finish
    ctypes.windll.kernel32.WaitForSingleObject(h_thread, 0xFFFFFFFF)

    # Get the exit code of the remote thread
    exit_code = ctypes.c_ulong()
    ctypes.windll.kernel32.GetExitCodeThread(h_thread, ctypes.byref(exit_code))

    # Check if the DLL was successfully injected
    if exit_code.value != 0:
        print("[+] DLL injected successfully!")
    else:
        print("[-] Error: DLL injection failed.")

    # Close the handle to the remote thread
    ctypes.windll.kernel32.CloseHandle(h_thread)

    # Close the handle to the target process
    ctypes.windll.kernel32.CloseHandle(h_process)

def unload_dll(dll_path, thread_id):
    # Convert the thread ID to a DWORD
    thread_id = int(thread_id)

    # Open a handle to the target process
    h_process = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, thread_id)
    if h_process == 0:
        print("[-] Error: Could not open handle to process.")
        return

    # Get the handle to the loaded DLL
    h_dll = ctypes.windll.kernel32.GetModuleHandleA(dll_path)
    if h_dll == 0:
        print("[-] Error: Could not get handle to DLL.")
        return

    # Create a remote thread to unload the DLL
    h_thread = ctypes.windll.kernel32.CreateRemoteThread(h_process, 0, 0, ctypes.windll.kernel32.GetProcAddress(ctypes.windll.kernel32.GetModuleHandleA("kernel32.dll"), "FreeLibrary"), h_dll, 0, 0)
    if h_thread == 0:
        print("[-] Error: Could not create remote thread.")
        return

    # Wait for the remote thread to finish
    ctypes.windll.kernel32.WaitForSingleObject(h_thread, 0xFFFFFFFF)

    # Get the exit code of the remote thread
    exit_code = ctypes.c_ulong()
    ctypes.windll.kernel32.GetExitCodeThread(h_thread, ctypes.byref(exit_code))

    # Check if the DLL was successfully unloaded
    if exit_code.value != 0:
        print("[+] DLL unloaded successfully!")
    else:
        print("[-] Error: DLL unloading failed.")

    # Close the handle to the remote thread
    ctypes.windll.kernel32.CloseHandle(h_thread)

    # Close the handle to the target process
    ctypes.windll.kernel32.CloseHandle(h_process)
root = tk.Tk()
root.title("DLL Injector")

def on_select(v):
    global remove_headers
    remove_headers = v

def inject():
    dll_path = dll_path_entry.get()
    thread_id = process_id_entry.get()
    remove_headers = remove_headers_var.get()
    inject_dll(dll_path, thread_id, remove_headers)

# DLL path label and entry
dll_path_label = tk.Label(root, text="DLL Path:")
dll_path_label.grid(row=0, column=0, padx=5, pady=5)
dll_path_entry = tk.Entry(root)
dll_path_entry.grid(row=0, column=1, padx=5, pady=5)

# Process ID label and entry
process_id_label = tk.Label(root, text="Process ID:")
process_id_label.grid(row=1, column=0, padx=5, pady=5)
process_id_entry = tk.Entry(root)
process_id_entry.grid(row=1, column=1, padx=5, pady=5)

# Remove headers checkbox
remove_headers_var = tk.BooleanVar()
remove_headers_checkbox = tk.Checkbutton(root, text="Remove headers", variable=remove_headers_var, onvalue=True, offvalue=False)
remove_headers_checkbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Inject button
inject_button = tk.Button(root, text="Inject", command=inject)
inject_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
