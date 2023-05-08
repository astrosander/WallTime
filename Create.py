import configparser



def crt(CONF_FILE):
    config = configparser.ConfigParser()

    config.add_section('WallpaperConfig')
    config.add_section('Date')


    config.set('WallpaperConfig', 'backgroundcolour', '#8fb195')
    config.set('WallpaperConfig', 'textcolour', '#f88f49')
    config.set('WallpaperConfig', 'fontsize', '50')
    config.set('Date', 'day', '19')
    config.set('Date', 'month', '5')
    config.set('Date', 'year', '2043')

    with open(CONF_FILE, 'w') as configfile:   
        config.write(configfile)



