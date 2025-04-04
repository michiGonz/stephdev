import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
import link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
            rx.link("About", href="/content",  style=styles.navbar_link_style ),
            rx.link("Skills", href="#medium-section",  style=styles.navbar_link_style ),
            rx.link("Projects", href="/content", style=styles.navbar_link_style ),
            padding="20px",
            text_align="center",
            style=styles.navbar
            )