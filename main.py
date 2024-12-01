import string
import random
import gradio as gr

# Función para generar la contraseña
def generar_contraseña(longitud):
    try:
        # Convertimos la longitud a entero
        longitud = int(longitud)
        if longitud <= 0:
            return "La longitud debe ser mayor a 0."
        
        # Definir el conjunto de caracteres permitidos
        caracteres = string.ascii_letters + string.digits + string.punctuation
        
        # Generar una contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contraseña
    except ValueError:
        return "Por favor, ingresa un número válido para la longitud."

# Interfaz visual con Gradio
web = gr.Interface(
    fn = generar_contraseña,  # Función que ejecutará
    inputs = gr.Number(label="Longitud de la contraseña"),  # Entrada: longitud
    outputs = gr.Textbox(label="Contraseña generada"),  # Salida: contraseña
    title = "Generador de Contraseñas",
    description = "Introduce la longitud deseada para generar una contraseña segura.",
)

# Lanzar la aplicación
web.launch()
