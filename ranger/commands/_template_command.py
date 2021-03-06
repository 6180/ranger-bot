

class Command():
    # List of the handles this command is onvokable with.
    _aliases = [
        "main_name",
        "another_name"
    ]
    # Text to show in the bot help dialog.
    _help = "This is what this command does: stuff!"
    # If `False` anyone can use this command. If `True` only people with the
    #   `administrator` privilege can use it.
    _privileged = True
    # If `True` only the bot owner can use the command.
    _op_priv = False
    # Argument parser for complex commands
    parser = None

    @staticmethod
    async def execute(client, msg):
        await msg.channel.send(msg.content)
