import re
import ipaddress

def count_ipv4_addresses(filename):
    ipv4_count = {}

    with open(filename, 'r') as file:
        text = file.read()
        ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

        for match in re.findall(ipv4_pattern, text):
            try:
                ip = ipaddress.ip_address(match)
                if isinstance(ip, ipaddress.IPv4Address):
                    if ip in ipv4_count:
                        ipv4_count[ip] += 1
                    else:
                        ipv4_count[ip] = 1
            except ValueError:
                pass

    return ipv4_count

if __name__ == '__main__':
    file_name = 'check.txt'  # Replace with your text file's name
    output_file_name = 'ipv4_counts_output.txt'
    ipv4_counts = count_ipv4_addresses(file_name)

    sorted_counts = sorted(ipv4_counts.items(), key=lambda x: x[1], reverse=True)

    with open(output_file_name, 'w') as output_file:
        output_file.write("IPv4 Address Counts:\n")
        for ip, count in sorted_counts:
            output_file.write(f"{ip}: {count}\n")

    print(f"IPv4 address counts have been written to '{output_file_name}'")
