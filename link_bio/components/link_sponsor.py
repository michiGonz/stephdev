import reflex as rx
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def link_sponsor(imagen: str, url:  str) -> rx.Component:
    return rx.link(
     rx.image( 
        height= "40px",
        src=imagen
         
     ),
     href=url,
     is_external=True
    )