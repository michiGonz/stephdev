import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str ) -> rx.Component:
   return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                   src=image,
                   width="20px",  # Ajusta el ancho según sea necesario
                   height="20px",  # Ajusta la altura según sea necesario
                   margin="20px",
                   display="block",  # Asegura que la imagen se muestre como un bloque
                   object_fit="cover"  # Ajusta la imagen para que cubra el área
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_styles ),
                    rx.text(body, style=styles.button_body_styles),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    padding_bottom="10px",
                    padding_top= "10px",
                    
                ),
            ),
        ),
        
        href=url,
        align_items="center",  # Centra los elementos horizontalmente en el vstack
        justify_content="center",  # Centra los elementos verticalmente en el vstack
        width="100%", # Asegura que el vstack ocupe todo el ancho del contenedor

    )

