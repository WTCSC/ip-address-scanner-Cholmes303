
import ipaddress
# Used for commands outside of Python.
import subprocess

import platform
import re

def ping_host(ip):
    """Pings a host and returns the status and response time."""
    try:
        # Determine OS-specific ping command.
        if platform.system().lower() == "windows":
            # Commands for Windows.
            cmd = ["ping", "-n", "1", "-w", "1000", ip]  
        else:
            # Commands for Linux/macOS.
            cmd = ["ping", "-c", "1", "-W", "1", ip]  

        # Run the ping command and capture output.
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check for errors.
        if result.returncode != 0:
            # Capture error messages.
            return "ERROR", result.stderr.strip()  

        # Extract response time using regex (re).
        match = re.search(r"time[=<]([\d.]+) ?ms", result.stdout)
        if match:
            response_time = match.group(1) + "ms"
            return "UP", response_time
        else:
            return "DOWN", "No response"

    except Exception as e:
        return "ERROR", str(e)

def get_active_hosts(cidr):
    """Scans the given network and reports host status."""
    try:
        # Allows for any IPv4 input with CIDR (strict=False).
        network = ipaddress.IPv4Network(cidr, strict=False)
        print(f"\nScanning network {cidr}...\n")

        results = []
        # Sets the count of each occurrence. 
        up_count = down_count = error_count = 0

        # Iterate over all valid hosts.
        for ip in network.hosts():
            status, message = ping_host(str(ip))

            # Format output.
            print(f"{ip} - {status.ljust(6)} ({message})")

            # Count occurrences of UP, DOWN, or ERROR.
            if status == "UP":
                up_count += 1
            elif status == "DOWN":
                down_count += 1
            else:
                error_count += 1

            # Adds IP address that was found.
            # IP's status (UP, DOWN, or ERROR).
            # Message (response time in milliseconds, no response, or network not reachable).
            results.append((ip, status, message))

        # Print summary of IP networks from CIDR.
        print(f"\nScan complete. Found {up_count} active hosts, {down_count} down, {error_count} errors.")

    # Checks for valid IPv4 CIDR notation (e.g. 192.168.1.0/24).
    except ValueError as e:
        print(f"Invalid CIDR notation: {e}")

if __name__ == "__main__":
    cidr_input = input("Enter CIDR notation (e.g., 192.168.1.0/24): ")
    get_active_hosts(cidr_input)

