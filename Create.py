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
    config.set('Date', 'base', '9999999999')
    config.set('Date', 'base_argument', '0')

    with open(CONF_FILE, 'w') as configfile:   
        config.write(configfile)

# crt(r'C:\Users\256bit.by\AppData\Local\DataWatch\config.ini')

