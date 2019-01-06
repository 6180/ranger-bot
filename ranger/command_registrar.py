

class CommandRegistrar():
    _commands = {}

    @staticmethod
    def register_command(cls):
        required_attributes = [
            '_aliases', '_help', '_privileged', '_op_priv', 'execute'
        ]
        # Ensure each class has the above attributes
        for attr in required_attributes:
            if attr not in dir(cls):
                print(f"[ERROR]: {cls._filename}.{cls.__name__} is missing an `{attr}` attribute")
                return
        
        for alias in cls._aliases:
            CommandRegistrar._commands[alias] = cls


    @staticmethod
    def instance():
        return CommandRegistrar._instance or CommandRegistrar()
