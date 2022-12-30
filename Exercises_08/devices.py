"""
Script: devices.py
By: Martina Atkinson L00177769
Purpose: Create Device Classes
Prerequisites: main.py to instantiate classes for test purposes
Tested: 10/10/2022

"""


# In any complex application, create a base class which will never be instantiated.
# device is an abstract class which is not instantiated
class Device():
 
    # Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for base class")
        # Create attributes and set initial values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from base")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc

"""
Child Class Template

"""
# Create child classes which can access the methods and properties of the base class
class Firewall(Device):
 # Constructor, called whenever an instance of the class is created.
 # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_firewall(self):
        print("Configuring Firewall") 

    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from child FIREWALL")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        print(crc)
        return crc

#hostname = "firewall3"
#my_firewall = Firewall(hostname)
#my_firewall.calculate_crc("dummy")
#my_firewall.configure_firewall()


# Create child classes which can access the methods and properties of the base class
class Switch(Device):
 # Constructor, called whenever an instance of the class is created
 # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_switch(self):
        print("Configuring Switch ") 

    def calculate_crc(self, frame:str)->int: 
        # Put real code in here, this is a dummy value for initial setup
        crc = 33333333
        print("In Child Switch calculate CRC SWITCH")  
        print(crc)
        return crc

# Create child classes which can access the methods and properties of the base class
class LoadBalancer(Device):
 # Constructor, called whenever an instance of the class is created.
 # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_load_balancer(self):
        print("Configuring Load Balancer") 

    def calculate_crc(self, frame:str)->int: 
        crc = 4444444
        print("In child Load Balancer calculate CRC LOAD BALANCER")
        # Put real code in here, this is a dummy value for initial setup
        print(crc)
        return crc

