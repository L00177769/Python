"""
Script: main.py
By: Martina Atkinson L00177769
Purpose: Main code to instantiate Devices Class and demonstrate Inheritance
Prerequisites: devices.py created with Device classes
Tested: 10/10/2022

"""


from devices import Firewall
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

from devices import Switch
# Create a firewall instance
switch1 = Switch("Switch1")
# Configure it
switch1.configure_switch()
# Create a firewall instance
switch2 = Switch("Switch2")
# Verify a CRC
switch2.calculate_crc("dummy data")


from devices import LoadBalancer
# Create a firewall instance
load_balancer1 = LoadBalancer("Load Balancer 1")
# Configure it
load_balancer1.configure_load_balancer()
# Create a firewall instance
load_balancer2 = LoadBalancer("Load Balancer 2")
# Verify a CRC
load_balancer2.calculate_crc(999999)
