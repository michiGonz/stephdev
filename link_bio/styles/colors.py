from enum import Enum 


##5B8096 azul
##4A246A morado
#eeeef3 gris
#bb5bf3 morado oscuro

class Color(Enum):
    PRIMARY = "#eeeef3" #blanco claro
    SECONDARY = "#92c7fc" #azul claro
    BACKGROUND = "#6b7279" #gris
    CONTENT = "#0d182e" #azul oscuro
    BORDER =  "#CC6CE7" #LILA
    NAVBAR = "#8c46da " #morado
    MEDIO = "#8a59c2" #morado medio
    

class TextColor(Enum):
    HEADER = "#eeeef3" #blanco claro
    BODY = "#eeeef3" #blanco claro
    FOOTER = "#eeeef3" #blanco claro