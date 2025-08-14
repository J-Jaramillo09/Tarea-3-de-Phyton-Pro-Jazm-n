import discord
from discord.ext import commands
import asyncio
from bot_logic import gen_emodji, gen_pass
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="discord_token.env")
TOKEN = os.getenv("DISCORD_TOKEN")


# Configurar los intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Crear el bot con prefijo de comandos
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot iniciado como {bot.user}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command(name='bye')
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command(name='smile')
async def smile(ctx):
    emoji = gen_emodji()
    await ctx.send(emoji)

@bot.command(name='generar_contraseña')
async def generar_contraseña(ctx):
    await ctx.send("🔐 Indica la longitud de la contraseña:")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        respuesta = await bot.wait_for('message', timeout=30.0, check=check)
        longitud = int(respuesta.content)

        await ctx.send(f"Generando contraseña de {longitud} caracteres...")
        contraseña = gen_pass(longitud)
        await ctx.send(f"Tu contraseña es: `{contraseña}`")

    except asyncio.TimeoutError:
        await ctx.send("⏱️ No recibí respuesta a tiempo. Inténtalo de nuevo.")
    except ValueError:
        await ctx.send("❌ Por favor ingresa un número válido.")


@bot.event
async def on_member_join(member):
    print(f"🔔 Se ha unido: {member.name}")
    canal = discord.utils.get(member.guild.text_channels, name='general')
    if canal:
        await canal.send(f"👋 ¡Bienvenido/a {member.mention} al servidor!")



# Ejecutar el bot
bot.run(TOKEN)


