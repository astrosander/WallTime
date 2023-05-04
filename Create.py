import configparser



def crt(CONF_FILE):
    # config.read(CONF_FILE)
    config = configparser.ConfigParser()
    # add some sections to the INI file
    config.add_section('WallpaperConfig')
    config.add_section('Date')

    # add some key-value pairs to each section
    config.set('WallpaperConfig', 'backgroundcolour', '#8fb195')
    config.set('WallpaperConfig', 'textcolour', '#f88f49')
    config.set('WallpaperConfig', 'fontsize', '50')
    config.set('Date', 'day', '19')
    config.set('Date', 'month', '5')
    config.set('Date', 'year', '2043')

    with open(CONF_FILE, 'w') as configfile:    # save
        config.write(configfile)



