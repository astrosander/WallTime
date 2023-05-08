from configparser import ConfigParser

def change_config(section, option, value, config_file_path):
    config = ConfigParser()
    config.read(config_file_path)

    config.set(section, option, value)

    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

def read_config(config_file_path):
    
    config = ConfigParser()
    config.read(config_file_path)
    
    return config 

