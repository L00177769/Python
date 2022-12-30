"""
Script: working_with_files.py
By: Martina Atkinson(L00177769)
Purpose :Working with Files (Opening a file for writing)
Prerequisites: None
Tested: 10/10/2022
"""
my_filename = "logfile.txt"
try:
    with open(my_filename, "a") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Finishing up!")
 # close not needed because with statement
 # file_handle.close()


