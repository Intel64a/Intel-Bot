from discord.ext.commands import Bot
from glob import glob

COGS = [path.split("\\")[-1][:-3] for path in glob("./bot/cogs/*.py")]
GUILD_ID = 925601676038123572
MAIN_CHANNEL = 925601676566609952

class Bot(Bot):
    def __init__(self):

        self.ready = False

        super().__init__(command_prefix="!", description="Your helper bot")

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog loaded")
            
        print("setup complete")


    def run(self):

        self.setup()
        
        with open('./data/token.txt', "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print(" bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(GUILD_ID)
            self.stdout = self.get_channel(MAIN_CHANNEL)

            await self.stdout.send("Online")

bot = Bot()