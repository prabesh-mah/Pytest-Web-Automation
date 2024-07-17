from configparser import ConfigParser


# Read data from 'config.ini' file
def read_configuration(file, value):

    # ConfigParser Instance
    config = ConfigParser()

    # Read 'config.ini' file
    try:
        config.read("configurations/config.ini")
    except FileNotFoundError:
        print("File named'config.ini' is not Found")

    return config.get(file, value)
