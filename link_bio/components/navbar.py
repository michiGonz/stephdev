import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
            rx.link("Home", href="#home", style=styles.navbar_link_style),
            rx.link("About", href="#about", style=styles.navbar_link_style),
            rx.link("Skills", href="#skills", style=styles.navbar_link_style),
            rx.link("Projects", href="#projects", style=styles.navbar_link_style),
            padding="20px",
            text_align="center",
        style=styles.navbar_title_style,
    )