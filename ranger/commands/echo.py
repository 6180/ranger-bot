

class EchoCommand():
    # List of the handles this command is onvokable with.
    _aliases = [
        "echo"
    ]
    # Text to show in the bot help dialog.
    _help = "Echo back the content of message."
    # If `False` anyone can use this command. If `True` only people with the
    #   `administrator` privilege can use it.
    _privileged = False
    # If `True` only the bot owner can use the command.
    _op_priv = False
    # Argument parser for complex commands
    _parser = None

    @staticmethod
    async def execute(client, msg):
        await msg.channel.send(msg.content)
