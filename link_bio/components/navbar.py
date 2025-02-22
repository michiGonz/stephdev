import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("StephDEV", color=TextColor.HEADER.value),
            align="left",
            style=styles.navbar_title_style
        ),
        rx.hstack(
            rx.link("Home", href="#home", style=styles.navbar_link_style),
            rx.link("About", href="#about", style=styles.navbar_link_style),
            rx.link("Skills", href="#skills", style=styles.navbar_link_style),
            rx.link("Projects", href="#projects", style=styles.navbar_link_style),
            align="center", # Alinear los enlaces al centro
            padding="20px"
        ),
        position="sticky",
        bg=Color.NAVBAR.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        margin_bottom="1px",
        z_index="999",
        top="0px",
        justify="center"  # Centrar el contenido del navbar
    )