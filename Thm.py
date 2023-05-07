from configparser import ConfigParser

dflt = {
    "Coral Reef": ["#008080", "#FF7F50"],
    "Electric Grey": ["#424242", "#FFEB3B"],
    "Ember Black": ["#212121", "#FF5722"],
    "Forest Green": ["#263238", "#00C853"],
    "Midnight Gold": ["#001f3f", "#ffd700"],
    "Mystic Lavender": ["#7f00ff", "#ec9787"],
    "Ocean Teal": ["#1C262B", "#009688"],
    "Royal Violet": ["#2E294E", "#9C27B0"],
    "Steel Blue": ["#333333", "#add8e6"],
    "Sunset Blue": ["#5763f7", "#ff8000"]
}
def Themes(choice, conf_file):
    config = ConfigParser()
    config.read(conf_file)
    
    config.set('WallpaperConfig', 'backgroundcolour', dflt[choice][0])
    config.set('WallpaperConfig', 'textcolour', dflt[choice][1])

    with open(conf_file, 'w') as configfile:
        config.write(configfile)