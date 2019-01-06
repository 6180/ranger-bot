import discord
import logging
import asyncio
import json



if __name__ == '__main__':
    # Set up logging stuff
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
else:
    print("You are importing the ranger root package as a module. I'm not sure what you are trying to do but you're doing it wrong.")
