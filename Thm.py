from configparser import ConfigParser
import ChangeCfg 

dflt = {
    "Coral Reef": ["#008080", "#FF7F50"],
    "Electric Grey": ["#424242", "#FFEB3B"],
    "Ember Black": ["#212121", "#FF5722"],
    "Forest Green": ["#263238", "#00C853"],
    "Midnight Gold": ["#001f3f", "#ffd700"],
    "Mystic Lavender": ["#7f00ff", "#ec9787"],
    "Ocean Teal": ["#1C262B", "#009688"],
    "Royal Violet": ["#2E294E", "#9C27B0"],
    "Cherry Blossom": ["#F8BBD0", "#C2185B"],
	"Jungle Green": ["#2E7D32", "#8BC34A"],
	"Charcoal": ["#36454f", "#e0e0e0"]
	}

def Themes(choice, conf_file):
    ChangeCfg.change_config('WallpaperConfig','backgroundcolour', dflt[choice][0], conf_file)
    ChangeCfg.change_config('WallpaperConfig','textcolour', dflt[choice][1], conf_file)
