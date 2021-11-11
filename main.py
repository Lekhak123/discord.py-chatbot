import discord
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
mname = '../models/blenderbot_small-90M'
tokenizer = AutoTokenizer.from_pretrained(mname)
model = AutoModelForSeq2SeqLM.from_pretrained(mname)
import json
f = open('config.json',)
with open('config.json') as f:
    data = json.load(f)
    token = data["token"]
    


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} python bot has connected to Discord!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    UTTERANCE = str(message.content);
    inputs = tokenizer(UTTERANCE, return_tensors='pt')
    reply_ids = model.generate(**inputs)
    response = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in reply_ids]
    respoonse = response[0].replace(" . ",".")
    final_response = respoonse.replace(" ' ","'")
    print(final_response)
    await message.channel.send(""+final_response)


client.run(token)