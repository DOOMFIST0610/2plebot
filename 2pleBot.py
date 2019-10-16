import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("이플이 때리기")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워!")
    if message.content.startswith("잘가"):
        await message.channel.send("잘있어!")
    if message.content.startswith("잘자"):
        await message.channel.send("알아쒑 잘자")

    if message.content.startswith(",사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))


client.run("NjIzNTEzODc2NTI0NDMzNDQx.Xacd-g.L-YJl6Rlr9tXNw-OPgYYvt6lBuU")
