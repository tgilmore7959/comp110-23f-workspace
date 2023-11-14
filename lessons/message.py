"""Class to store a message (operator overload, union types, default parameters)."""


class Message: 

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str | int, message_content: str = "", importane_flag: bool = False):
        """Consruct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importane_flag

    def __str__(self) -> str:
        """Setting Str."""
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"' 
        return output
    
    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val 


msg: Message = Message("erin", "Great Job!", False)
msg_to_myself: Message = Message("me", "Do your 110 Homework", True)
print(msg_to_myself)

