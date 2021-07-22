import discord
import random


class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("hi c:")

    async def on_message(self,message):
        if message.author == client.user:
            return

        if message.content == "$help":
            await message.channel.send('''Für Roulette: $roulette BID eingeben, wobei BID= 
            black \n red \n number''')

        if message.content.startswith("$roulette"):
            bid = message.content.split(" ")[1]
            bid_param = -3
            if bid.lower() == "black":
                bid_param = -1
            elif bid.lower() == "red":
                bid_param = -2
            else:
                try:
                    bid_param = int(bid)
                except:
                    bid_param = -3
            if bid_param == -3:
                await message.channel.send('Ungültige Eingabe')
                return
            result = random.randint(0,36)
            print(result)
            if bid_param == -1:
                won = result%2 == 0 and not result == 0
            elif bid_param == -2:
                won = result%2 == 1
            else :
                won = result == bid_param
            if won:
                await message.channel.send('du hast gewonnen yay!')
            else:
                await message.channel.send('verloren :/')



client = MyClient()
client.run("token")