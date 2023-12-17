import discord
from discord.ext import commands
from pathlib import Path
import json
import re

# Discord Setup
intents = discord.Intents.default()
intents.message_content = True
i = commands.Bot(intents=intents, command_prefix="/")

token = None
credentials_path = Path("credentials.json")
try:
  with open(credentials_path) as credentials:
    token = json.load(credentials)['token']
    if not token:
      raise FileNotFoundError
except FileNotFoundError:
  with open(credentials_path, 'w') as credentials:
    json.dump({'token': ''}, credentials)

@i.listen('on_message')
async def listen_for_message(message: discord.Message):
  if not message.author.bot:
    i_links = re.findall("http.*[\./]instagram.com/reel\S*", message.content)
    if i_links:
      for link in i_links:
        await message.reply(link.replace('instagram.com', 'instagramez.com'), mention_author=False)
    
    if len(message.embeds) == 0:
      t_links = re.findall("http.*[\./]twitter.com/\S*", message.content)
      if t_links:
        for link in t_links:
          await message.reply(link.replace('twitter.com', 'vxtwitter.com'), mention_author=False)
  
def main():
  if not token:
    print("No token found. Please fill out credentials.json")
    return
  print(f"Running with token {token[:3]}...")
  i.run(token)

if __name__ == "__main__":
  main()