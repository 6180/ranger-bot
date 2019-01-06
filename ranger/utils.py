import re

from discord import Embed

RE_MENTION = re.compile(r'<@!?\d{18}>')
RE_NAME_DISCRIM = re.compile(r'^.+#\d{4}$')


async def find(predicate, seq):
    for element in seq:
        if predicate(element):
            return element
    return None


async def is_mention(pattern):
    return RE_MENTION.match(pattern)


async def get_name_discrim(pattern):
    if not RE_NAME_DISCRIM.match(pattern):
        return pattern, None

    tmp = pattern.rpartition('#')
    return tmp[0], tmp[2]


async def get_user(pattern, guild):
    if await is_mention(pattern):
        id_ = int(''.join(c for c in pattern if c.isdigit()))
        return guild.get_member(id_)

    name, discrim = await get_name_discrim(pattern)

    if discrim:
        target = await find_user_by_iname_discrim(name, discrim, guild)
    else:
        target = await find_user_by_iname(name, guild)

    return target


async def find_user_by_iname(name, guild):
    name = name.lower()
    return await find(
        lambda m: m.name.lower() == name or (m.nick is not None and m.nick.lower() == name),
        guild.members)


async def find_user_by_iname_discrim(name, discrim, guild):
    name = name.lower()
    return await find(
        lambda m: m.discriminator == discrim and
                  (m.name.lower() == name or (m.nick is not None and m.nick.lower() == name)),
        guild.members)

# I know I know...
def sanitize_everyone(msg):
    return msg.replace('@everyone', '@\u200Beveryone').replace('@here', '@\u200Bhere')

def simple_embed(msg, author=None, color=0x66ff99):
    embed = Embed()
    embed.colour = color
    embed.description = msg
    if author:
        embed.set_footer(
            text=f'Requested by {author.name}#{author.discriminator}',
            icon_url=author.avatar_url
        )
    return embed
