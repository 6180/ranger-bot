from discord import Embed

import utils


class Command():
    # List of the handles this command is onvokable with.
    _aliases = [
        "avatar"
    ]
    # Text to show in the bot help dialog.
    _help = "Display a users avatar in an embed."
    # If `False` anyone can use this command. If `True` only people with the
    #   `administrator` privilege can use it.
    _privileged = False
    # If `True` only the bot owner can use the command.
    _op_priv = False
    # Argument parser for complex commands
    parser = None

    @staticmethod
    async def execute(client, msg):
        arg = msg.content.partition(' ')[1]


        if not arg:
            target = msg.author
        elif len(msg.mentions) > 0:
            target = msg.mentions[0]
        else:
            target = await utils.get_user(arg, msg.channel.guild)
        
        print(target)

        embed = Embed()

        embed.colour = target.colour
        embed.set_author(
            name=f"{target.name}#{target.discriminator}'s avatar",
            url=target.avatar_url
        )
        embed.set_image(url=target.avatar_url)
        embed.set_footer(
            text=f'Requested by {msg.author.name}#{msg.author.discriminator}',
            icon_url=msg.author.avatar_url
        )

        await msg.channel.send(embed=embed)
