from colorama import Fore
from colorama import Style
from colorama import Back

from colorama import init
init(autoreset=True)

class Maneger:
    @staticmethod
    def maneger_color_text(color):
        if color == "black":     return Fore.BLACK
        elif color == "red":     return Fore.RED
        elif color == "green":   return Fore.GREEN
        elif color == "yellow":  return Fore.YELLOW
        elif color == "blue":    return Fore.BLUE
        elif color == "magenta": return Fore.MAGENTA
        elif color == "cyan":    return Fore.CYAN
        elif color == "white":   return Fore.WHITE
        else: return ""

    @staticmethod
    def maneger_light_text(color, light):
        if color == "black" and light:     return Fore.LIGHTBLACK_EX
        elif color == "red" and light:     return Fore.LIGHTRED_EX
        elif color == "green" and light:   return Fore.LIGHTGREEN_EX
        elif color == "yellow" and light:  return Fore.LIGHTYELLOW_EX
        elif color == "blue" and light:    return Fore.LIGHTBLACK_EX
        elif color == "magenta" and light: return Fore.LIGHTMAGENTA_EX
        elif color == "cyan" and light:    return Fore.LIGHTCYAN_EX
        elif color == "white" and light:   return Fore.LIGHTWHITE_EX
        else: return ""

    @staticmethod
    def maneger_backgraund_text(backgraund):
        if backgraund == "black":     return Back.BLACK
        elif backgraund == "red":     return Back.RED
        elif backgraund == "green":   return Back.GREEN
        elif backgraund == "yellow":  return Back.YELLOW
        elif backgraund == "blue":    return Back.BLUE
        elif backgraund == "magenta": return Back.MAGENTA
        elif backgraund == "cyan":    return Back.CYAN
        elif backgraund == "white":   return Back.WHITE
        else: return ""

    @staticmethod
    def maneger_backgraund_light_text(backgraund, light):
        if backgraund == "black" and light:     return Back.LIGHTBLACK_EX
        elif backgraund == "red" and light:     return Back.LIGHTRED_EX
        elif backgraund == "green" and light:   return Back.LIGHTGREEN_EX
        elif backgraund == "yellow" and light:  return Back.LIGHTYELLOW_EX
        elif backgraund == "blue" and light:    return Back.LIGHTBLACK_EX
        elif backgraund == "magenta" and light: return Back.LIGHTMAGENTA_EX
        elif backgraund == "cyan" and light:    return Back.LIGHTCYAN_EX
        elif backgraund == "white" and light:   return Back.LIGHTWHITE_EX
        else: return ""

    @staticmethod
    def manefer_style_text(style):
        if style:
            return Style.BRIGHT
        else:
            return ""