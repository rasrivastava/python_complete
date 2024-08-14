- `DHCP (Dynamic Host Configuration Protocol)`:
  - DHCP is used to dynamically assign IP addresses and other network configuration parameters to devices on a network, allowing them to communicate effectively.

- On Red Hat Enterprise Linux (RHEL), configuring DHCP can involve
  - either setting up a DHCP server to assign IP addresses to clients
- or configuring a DHCP client to receive an IP address from a DHCP server.

- Here’s how you can configure both:

### Configuring a DHCP Server on RHEL

1. Install the DHCP Server Package:
   First, you need to install the DHCP server package if it’s not already installed.

    ```
    sudo yum install dhcp-server
    ```

2. Configure the DHCP Server:
   - The main configuration file for the DHCP server is /etc/dhcp/dhcpd.conf. You need to edit this file to define the network settings and options.
   
    - `Edit the DHCP Configuration File:`
      ```
      sudo vi /etc/dhcp/dhcpd.conf
      ```
    - Add or Modify the Configuration:
        ```
        # Sample DHCP configuration file

        # Define the default lease time and maximum lease time
        default-lease-time 600;
        max-lease-time 7200;

        # Define the subnet and network settings
        subnet 192.168.1.0 netmask 255.255.255.0 {
            range 192.168.1.10 192.168.1.100;
            option domain-name-servers 8.8.8.8, 8.8.4.4;
            option routers 192.168.1.1;
            option broadcast-address 192.168.1.255;
            option domain-name "example.com";
        }

        # Define the DHCP server's own IP address
        authoritative;
        ```

       - `default-lease-time 600;`
          - specifies the default lease time in seconds.
          - In this case, it is set to 600 seconds (10 minutes).
          - This is the duration that a DHCP client can use the assigned IP address before it must renew the lease.
        
        -  `max-lease-time 7200;`
          - specifies the maximum lease time in seconds.
          - Here, it is set to 7200 seconds (2 hours).
          - This is the maximum amount of time a client can use the IP address before it must renew the lease, even if it hasn't requested a renewal.
        
        - `subnet 192.168.1.0 netmask 255.255.255.0 { ... }`
           - **defines a subnet with the network address 192.168.1.0**
           - and **a subnet mask of 255.255.255.0.**
           - **This means that the network includes IP addresses from 192.168.1.0 to 192.168.1.255.**
        
        - summary:
          - This configuration file sets up a DHCP server to manage IP addresses for devices on the 192.168.1.0/24 subnet.
          - It specifies lease times, defines the IP address range for clients, sets up DNS servers, a default router, a broadcast address, and a domain name, and marks the server as authoritative.

    - Adjust the settings according to your network requirements. The subnet block defines the IP range that the server will use to assign IP addresses.

3. Start and Enable the DHCP Service:

```
sudo systemctl start dhcpd
sudo systemctl enable dhcpd
```

4. Configure Firewall (if applicable):

```
sudo firewall-cmd --permanent --add-service=dhcp
sudo firewall-cmd --reload
```

### Configuring a DHCP Client on RHEL

Install the DHCP Client Package (if not installed):
Most RHEL installations come with the DHCP client pre-installed. However, you can ensure it’s installed:

```
sudo yum install dhclient
```

- Configure the Network Interface to Use DHCP:
  1. `Edit the Network Interface Configuration`:
      - Network configuration files are typically located in `/etc/sysconfig/network-scripts/`.
      - Edit the appropriate configuration file for your network interface, such as `ifcfg-eth0` or `ifcfg-enp0s3`.
  2. Set the Interface to Use DHCP:
     Ensure the following settings are configured in the file:
     
    ```
    DEVICE=eth0
    BOOTPROTO=dhcp
    ONBOOT=yes
    ```

    - `BOOTPROTO=dhcp` tells the **interface to use DHCP for IP address assignment**.
    - `ONBOOT=yes` ensures the **interface starts automatically at boot**.
   3. Restart the Network Service:
      ```
      sudo systemctl restart network
      ```
   4. you can bring the interface up manually: (optional)
      ```
      sudo ifdown eth0 && sudo ifup eth0
      ```