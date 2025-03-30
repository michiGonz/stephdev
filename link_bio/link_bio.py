import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.views.sponsors.sponsor import sponsor
from link_bio.views.medium.medium import medium
from link_bio.views.content.content import content
from link_bio.views.projects.project import project
class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                header(),
                width="100%",  # Asegúrate de que ocupe todo el ancho de la página
                max_width="100%",
                margin_y=Size.BIG.value
               
            ),
        ),
        rx.center(
            rx.vstack(
                medium(),
                width="100%" # Asegúrate de que ocupe todo el ancho de la página
            ),
        ),
         
         rx.center(
             rx.vstack(
                content(),
                height= "50%",  # Ajusta la altura del componente medium
                width="100%",  # Asegúrate de que ocupe todo el ancho de la página
                max_width="100%",
            )
         ),
        rx.center(
            rx.vstack(
              project(),
                width="100%",
               
            ),  
        ),
      
        footer()
    )
     
    

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="FefiDev | Mis Proyectos",
    description="Hola mi nombre es stef, soy ingeniero de software y aqui encontraras mi portafolio de proyectos",
    image="logo.png"
    ),



