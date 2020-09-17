import discord

client = discord.Client()
TOKEN = input("Please enter the token:\t")


@client.event
async def on_ready():
    print("Bot is online and can be controlled now.")
    while True:
        try:
            text, channel = input("Enter the text:\t"), int(input("Enter the channel id:\t"))
            c = client.get_channel(channel)
            await c.send(text)
        except:
            print("Can't find the channel!")


try:
    client.run(TOKEN)
except:
    print("Token is invalid!")
