IP Ping Size Tester

This script is designed to test the maximum packet size an IP address can handle without fragmenting. It achieves this by sending ping requests with varying payload sizes and observing whether the request is successful or not.
Features:

    Ping with Variable Size: The script sends ping requests to the specified IP addresses with varying packet sizes.
    Host Specification: IP addresses to be tested are specified in the ip_address list.
    Feedback: Provides feedback on whether a ping of a particular size was successful or failed.

Usage:

    Ensure you have the necessary permissions to run ping on your system.
    Modify the ip_address list to include the IP addresses you want to test. Replace "X.X.X.X" with the actual IP addresses.
    Run the script. For each IP address, the script will send ping requests with packet sizes ranging from 64 to 1472 bytes (the maximum size before fragmentation).
    Observe the output to see the results of the ping tests.

Code Structure:

    ping: This function sends a single ping request to the provided host with the specified size and returns whether the ping was successful.
    ip_address: A list that contains the IP addresses you want to test.
    max_size: The maximum packet size for the ping request.
    Loop: For each IP address in the ip_address list, the script sends ping requests with sizes ranging from 64 to max_size bytes, increasing in steps of 8 bytes.

Important Notes:

    The script uses the -c option to send a single ping request and the -s option to specify the packet size. These options might be different depending on the operating system. The provided options work for UNIX-based systems. For Windows, you might need to adjust the options.
    The script continuously sends pings with increasing sizes until a successful ping is detected. After detecting a successful ping, the loop breaks, and the script proceeds to the next IP address. If you want a more comprehensive report, you can modify the behavior to continue testing even after a successful ping.
    Ensure that you have the necessary permissions to send ICMP requests. Some systems might require administrative or root privileges to send ping requests.
