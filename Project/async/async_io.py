# RESTful Pokemon API, HTTP GET request
# fetch json and print the value

import time
import asyncio
import aiohttp
import aiofiles

# disable windows event warning
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

start_time = time.time()

async def api_test():
    # A HTTP session contains a connection pool
    async with aiohttp.ClientSession() as session:
        # load 1-150 api requests
        for number in range(1, 151):
            # the api URL, replace the variable
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            # use opened session, HTTP get() to fetch the url pools
            async with session.get(pokemon_url) as resp:
                # and save as json format
                pokemon = await resp.json()
                
            # set some variables
            name = pokemon['name']
            moves = [move['move']['name'] for move in pokemon['moves']]

    # async write files in async folder with different names and content
    async with aiofiles.open(f'async\{name}_moves.txt', mode='w') as f:
        await f.write('\n'.join(moves))
        
# run with asyncio.run()
asyncio.run(api_test())
# calculate time spent
print("--- %s seconds ---" % (time.time() - start_time))
print()
