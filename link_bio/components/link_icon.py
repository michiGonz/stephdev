import reflex as rx
import link_bio.styles.styles as styles

def link_icon(url: str, image: str)-> rx.Component:
    return rx.link(
        rx.image (
            src=image,
            width="20px"
        ),
    href=url,
    is_external=True
    )