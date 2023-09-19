import time
import codecs
from gpt4free import you

# Función para obtener una respuesta sin "Unable to fetch the response, Please try again."
def obtener_respuesta(prompt):
    while True:
        response = you.Completion.create(
            prompt=prompt,
            chat=chat
        )
        text = response.text.strip()
        if text != "Unable to fetch the response, Please try again.":
            return text

        time.sleep(5)  # Espera 5 segundos antes de intentar nuevamente

# Inicializar el chat vacío
chat = []

# Abrir un archivo para guardar las respuestas con el formato adecuado
with codecs.open("respuestas.txt", "w", "utf-8") as archivo_respuestas:
    while True:
        usuario_input = input("Usuario: ")
        if usuario_input == 'q':
            break
        
        # Obtener respuesta del modelo
        respuesta_bot = obtener_respuesta(usuario_input)
        
        # Imprimir la respuesta formateada en la consola
        respuesta_bot_legible = codecs.decode(respuesta_bot, 'unicode_escape')
        print("Bot:", respuesta_bot_legible)
        
        # Guardar la respuesta en el archivo con el formato adecuado
        archivo_respuestas.write(f"Usuario: {usuario_input}\n")
        archivo_respuestas.write(f"Bot: {respuesta_bot_legible}\n")
        
        # Agregar la conversación al chat
        chat.append({"question": usuario_input, "answer": respuesta_bot})

print("Conversación guardada en 'respuestas.txt'")
