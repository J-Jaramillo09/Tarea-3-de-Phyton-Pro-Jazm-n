import discord
import asyncio
from bot_logic import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$generar contraseña'):
        await message.channel.send("indica la longitud de la contraseña")
        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            respuesta = await client.wait_for('message', timeout=30.0, check=check)
            longitud = int(respuesta.content) 
            
            # Aquí puedes generar la contraseña con esa longitud
            await message.channel.send(f"Generando contraseña de {longitud} caracteres...")
            # Tu lógica de generación de contraseña iría aquí
            contraseña = gen_pass(longitud)  # Genera la contraseña
            await message.channel.send(f"Tu contraseña es: `{contraseña}`")

        except asyncio.TimeoutError:
            await message.channel.send("⏱️ No recibí respuesta a tiempo. Inténtalo de nuevo.")
        except ValueError:
            await message.channel.send("❌ Por favor ingresa un número válido.")


    else:
        await message.channel.send(message.content)













client.run("MTM5ODA0ODIzODYwNjYxODc0NQ.GlJIJB.2mA_6D2G9ps89HLdWuFVzbjPxo1yxmzq4lFpHA")
