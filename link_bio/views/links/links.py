import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import TextColor as TextColor


def links() -> rx.Component:
    return rx.vstack(
      title("Comunidad"),
      link_button(
      "GitHub", 
      "Directos de lunes a viernes",
      "/icons/github.svg",
      "https://github.com/michiGonz"
    
      ),
      
      link_button(
      "Youtube", 
      "Tutoriales semanales",
      "/icons/youtube.svg",
      "https://www.youtube.com/@stephaniegonzalez4725"
    
      ),

  
      title("Contacto"),
      link_button(
      "Gmail", 
      "Enviame un Mensaje",
      "/icons/envelope.svg",
      "https://mail.google.com/mail/u/0/?hl=es#inbox"
      ),
      
      link_button(
      "Slack", 
      "Escribeme por Slack",
      "/icons/slack.svg",
      "https://join.slack.com/shareDM/zt-2ztwcnb6f-g~roEgec4D4sABGhol_U5A"
      
      ),
      
      width="100%", # Asegura que el vstack ocupe todo el ancho del contenedor
      color=TextColor.HEADER.value,
   
      
    )
    
    