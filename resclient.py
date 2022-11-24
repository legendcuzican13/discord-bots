import discord

token = "ur bot token"
    
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if "allz" in message.channel.name:
            await message.channel.send("Updating web client...")
            with open('index.html', 'r+') as f: #r+ does the work of rw
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith('#'):
                        lines[i] = lines[i].strip() + "\n" + "        <br />" '\n' + "        <p>" + message.content + "</p>" + "\n"
                f.seek(0)
                for line in lines:
                    f.write(line)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)


client.run(token)




