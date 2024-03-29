# Starting IP address
start_ip = "10.0.0.0"

# Total number of IP addresses to generate
num_ips = 20420

# Convert the starting IP to an integer
ip = [int(i) for i in start_ip.split('.')]  # i=1   ip=[10.0.0.0]

# Loop to generate and print the IP addresses
for _ in range(num_ips):
    # Print the current IP address
    print(".".join(map(str, ip)))

    # Increment the IP address
    ip[3] += 1

    # Check for carry-over to the next octet
    for i in range(3, 0, -1):
        if ip[i] > 255:
            ip[i] = 0
            ip[i - 1] += 1

