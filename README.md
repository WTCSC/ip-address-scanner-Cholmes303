[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17931271)

# Network Scanner
## Description
This script scans a given network (provided in CIDR notation) and determines which hosts are active by sending ping requests. It works on both Windows and Unix-based systems (macOS/Linux) by adjusting the ping command accordingly. The script outputs the status of each scanned IP address and provides a summary of active, inactive, and unreachable hosts.

## Features
- Supports IPv4 addresses with CIDR notation.
- Works on Windows, macOS, and Linux.
- Uses system ping commands to determine host availability.
- Provides response time for reachable hosts.
- Displays a summary of network scan results.

## Requirements
- Python 3.x (at least python 3.0)

## Installation
1. Clone this repository or download the script.
   ```sh
   git clone https://github.com/WTCSC/ip-address-scanner-Cholmes303.git
   cd <repository_folder>
   ```
2. Ensure Python is installed on your system.
3. No additional dependencies are required (relies on built-in Python modules).

## Usage
1. Know what network you are on. This can be done in Windows Powershell with the command:
   ```
   ipconfig
   ```
   Or
   ```
   ipconfig /all
   ```
2. Run the script:
   ```sh
   python ip_freely.py
   ```
3. Enter a network range in CIDR notation when prompted (e.g., `192.168.1.0/24`).
4. The script will scan the network and display active/inactive hosts along with response times.

## Example Output
```
Enter CIDR notation (e.g., 192.168.1.0/24): 192.168.1.0/24

Scanning network 192.168.1.0/24...

192.168.1.1 - UP     (2ms)
192.168.1.2 - DOWN   (No response)
192.168.1.3 - UP     (3ms)
...

Scan complete. Found 5 active hosts, 10 down, 1 error.
```

## Notes
- The script requires administrative/root privileges on some systems for ICMP packets to work correctly.
- Firewalls and security settings may block ping requests, leading to "DOWN" statuses for some hosts.
- DO NOT use this program unless you are inside a virtual machine or are on a network that you have permission to scan. 


