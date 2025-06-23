

import tkinter as tk
from tkinter import messagebox
from mac_resolver import get_ip_from_mac
import style

def find_ip():
    mac = mac_entry.get().strip()
    if not mac:
        messagebox.showwarning("Input Error", "Please enter a MAC address.")
        return
    ip = get_ip_from_mac(mac)
    if ip:
        result_label.config(text=f"IP Address: {ip}")
    else:
        result_label.config(text="IP not found for the given MAC.")

# GUI Window
root = tk.Tk()
root.title("MAC to IP Converter")
root.geometry("400x200")
root.configure(bg=style.BG_COLOR)

tk.Label(root, text="Enter MAC Address:", bg=style.BG_COLOR, fg=style.FG_COLOR, font=style.FONT).pack(pady=10)
mac_entry = tk.Entry(root, bg=style.ENTRY_BG, fg=style.FG_COLOR, font=style.FONT, width=30)
mac_entry.pack(pady=5)

tk.Button(root, text="Find IP", command=find_ip, bg=style.BTN_BG, fg=style.FG_COLOR, font=style.FONT).pack(pady=10)
result_label = tk.Label(root, text="", bg=style.BG_COLOR, fg=style.FG_COLOR, font=style.FONT)
result_label.pack(pady=10)

root.mainloop()
