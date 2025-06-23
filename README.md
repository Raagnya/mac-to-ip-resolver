The MAC to IP Converter is a Python-based application that allows users to identify the IP address corresponding to a given MAC (Media Access Control) address on the same local network
Built with a user-friendly graphical interface using Tkinter, this project is ideal for students, network administrators, or anyone interested in understanding how local networks map MAC addresses to IP addresses.

app.py
This file is the main entry point. It launches the Tkinter GUI and connects the user interface with the logic that resolves the MAC address.


mac_resolver.py
This module handles the core logic of the program — broadcasting ARP requests over the network to detect and return the IP address associated with the user-supplied MAC address.


style.py
A simple configuration file for storing styling parameters like background color, font, and button colors — helps keep the GUI neat and consistent.
