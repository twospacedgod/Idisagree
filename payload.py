 import discord
import subprocess
from pathlib import Path

class cmd:

    path = None

    def __init__(self):
        self.path = Path()

    def run(self, cmd: str) -> str:
        tokens = remove_false(cmd.split(" "))
        if tokens[0] == "cd":
            self.path = self.path / tokens[1]
            return str(self.path.resolve())
        else:
            abs_path = self.path.resolve()
            return subprocess.getoutput(f"{abs_path.drive} && cd {abs_path} && {cmd}")


client = discord.Client()
active_channel = None
command_line = cmd()


@client.event
async def on_message(message):
    global active_channel
    if message.author.bot: return
    if message.content.casefold() == "idisagree":
        if message.channel == active_channel:
            await message.channel.send("Machine disconnected")
            active_channel = None
        else:
            await message.channel.send("Machine connected")
            active_channel = message.channel
    elif message.channel == active_channel:
        comando = command_line.run(message.content)
        await long_send(message.channel, comando)


async def long_send(channel, text):
    text = text + "\n"
    while len(text) > 0:
        clipped = text[:2000]
        newline_pos = clipped.rfind("\n")
        await channel.send("```\n" + text[:newline_pos] + "\n```")
        text = text[newline_pos + 1:]


def remove_false(iterator):
    return tuple(val for val in iterator if val)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

client.run(botToken)
