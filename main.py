# token in config.py

import discord
from discord import app_commands
from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is alive")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)") # this is needed for syncing commands up to bot.
    except Exception as e:
        print(e)
@bot.tree.command(name="test")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"i'm online!", ephemeral=True) # ephmeral = hidden/personal message
@bot.tree.command(name="say")
@app_commands.describe(arg="What should I say?")
async def say(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{arg}`") # do {arg} only if you want it to just repeat what oyu said.

bot.run(TOKEN)
