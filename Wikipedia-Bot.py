import discord
import wikipediaapi
from udpy import UrbanClient


TOKEN = "OTUwODU2MzIxNTEzNjg1MDAy.Yie_9Q.J8-PG2g9J5oos7N0O2Vtd7-y8QY"

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    if message.content.startswith('!urban'):
        u = 0
        urban_input = str(message.content).split('-')[1]
        urban = UrbanClient()
        for d in urban.get_definition(urban_input):
            u += 1
            if u == 1:
                embed_var = discord.Embed(title=d.word, color=0x00ffff)
                embed_var.add_field(name="Definition:", value=d.definition, inline=False)
                embed_var.add_field(name="Example:", value=d.example, inline=False)
                embed_var.add_field(name="Upvotes:", value=str(d.upvotes) + str('\U0001F44D'), inline=False)
                embed_var.add_field(name="Downvotes:", value=str(d.downvotes) + str('\U0001F44E'), inline=False)
                await message.channel.send(embed=embed_var)

    if message.content.startswith('!help'):
        embed_var2 = discord.Embed(title='Commands', color=0xFF0000)
        embed_var2.add_field(name="Wikipedia:", value='!wiki-input', inline=False)
        embed_var2.add_field(name="Urban Dictionary:", value='!urban-input', inline=False)
        await message.channel.send(embed=embed_var2)
    if message.content.startswith('!wiki'):
        if message.author == client.user:
            return

        else:
            wiki_input = str(message.content).split('-')[1]
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(wiki_input)
            if not page_py.exists():
                await message.channel.send("Error: Page not found")
            else:
                embed_var1 = discord.Embed(title=page_py.title, url=page_py.fullurl, description=str(page_py.summary[0:1024]) + '...', color=0xFFFF00)
                await message.channel.send(embed=embed_var1)


@client.event
async def on_message_delete(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    msg = f'DELETED MESSAGE - {username}: {user_message} ({channel})'
    embed_var = discord.Embed(title=username, description=msg, color=0x00ffff)
    master = await client.fetch_user(879543434849955850)
    await master.send(embed=embed_var)


client.run(TOKEN)
