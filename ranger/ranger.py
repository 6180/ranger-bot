import discord
import logging
import asyncio
import json

# The commands __init__.py file loads all of our command modules.
import commands
import command_registrar as registrar

# Variables globally accessible through this module.
client = discord.Client(max_messages=50000)
config = None

@client.event
async def on_ready():
    print(f"{client.user.name} is logged in.")

@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    if msg.content.startswith(config['prefix']) and len(msg.content) > 1:
        # Take the forst word and slice off the prefix
        command = msg.content.split()[0][1:]

        if command.lower() in registrar.commands.keys():
            await registrar.commands[command].execute(client, msg)


if __name__ == '__main__':
    # Set up logging.
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename='discord.log',
        encoding='utf-8',
        mode='w'
    )
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s')
    )
    logger.addHandler(handler)

    # Load config file.
    with open('config.json', 'r') as fp:
        config = json.load(fp)

    # Log the bot in and start running stuff.
    client.run(config['token'])
else:
    print("You are importing the ranger root package as a module. I'm not sure what you are trying to do but you're doing it wrong.")
