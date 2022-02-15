import os, random, discord 
from dhooks import Webhook, Embed
from time import sleep

from DiscordHooks import Hook, Embed, EmbedAuthor, Color
from datetime import datetime




os.system('color 3')

ra = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"

baaner0 = print("""
            ______                                       ____             
|         .~      ~.  |`````````, |``````.  `````|````` |    ~.           
|        |          | |'''|'''''  |       |      |      |____.'_          
|        |          | |    `.     |       |      |      |       ~.        
|_______  `.______.'  |      `.   |......'       |      |_______.'        
                                                                                                              
""")
start = input("Press Enter to start : ")

for i in range(500):
    fi = ''.join((random.choice(ra) for i in range(26)))
    sec = ''.join((random.choice(ra) for i in range(6)))
    th = ''.join((random.choice(ra) for i in range(27)))

    re = fi + "." + sec + "." + th
    print(re)
    file = open("Token_Generator.txt", "a")
    file.write(re + "\n")

webhook = 'https://discord.com/api/webhooks/941195546184532009/W0eozsf7v6IbRIIU-GNiPkKIICVYSllFDEiDhn4QTsVMnETCCduM6NZ8vQgj8FiUe2u6'

embed = Embed(title='Lord4tbb', url='https://instagram.com/Lord4tbb', description=re,
              timestamp=datetime.utcnow(), color=Color.Black, author=EmbedAuthor(name="Elite team ."))

Hook(hook_url=webhook, username="Token generator",
     embeds=[embed]).execute()

sleep(0.3)
os.system('cls')
baaner2 = print("""
            ______                                       ____             
|         .~      ~.  |`````````, |``````.  `````|````` |    ~.           
|        |          | |'''|'''''  |       |      |      |____.'_          
|        |          | |    `.     |       |      |      |       ~.        
|_______  `.______.'  |      `.   |......'       |      |_______.'        
                                                                                                              
""")
exit = input("Press Enter to exit : ")
