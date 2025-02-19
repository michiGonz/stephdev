import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor

from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor
from link_bio.styles.colors import Color as Color

def sponsor() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "/python.png",
                url="https://github.com/login"
            ),
            link_sponsor(
                "github.png",
                url="https://github.com/login"
            ),
            width="100%",
            align_items="start"
        )
    )
        