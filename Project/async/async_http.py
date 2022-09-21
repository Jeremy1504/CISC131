# RESTful Pokemon API, HTTP GET request
# fetch json and print the value

import requests
import time

import aiohttp
import asyncio

############################
# regular appraoch, request api
# slow
############################

start_time = time.time()

for number in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

# calculate time spent
print('sync apprach')
print("--- %s seconds ---" % (time.time() - start_time))
print()

############################ 
# async approach
# faster
############################

start_time = time.time()

async def test_2():
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
                # also print json value on terminal
                print(pokemon['name'])
    
    # optional, close session
    await session.close()

# run with asyncio.run()
asyncio.run(test_2())
# calculate time spent
print("--- %s seconds ---" % (time.time() - start_time))
print()

############################ 
# async approach with asyncio
# ensure_future, gater()
# much faster
############################

start_time = time.time()

# a function to return api data
async def get_pokemon(session, url):
    # http get
    async with session.get(url) as resp:
        # await and fetch json
        pokemon = await resp.json()
        # return the 'name' attribute only
        return pokemon['name']


async def test_3():
    # open a client session
    async with aiohttp.ClientSession() as session:
        # use a list to store tasks
        tasks = []
        # fetch pokeapi 1-150
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            # use asyncio.ensure_future to fetch data and assign async task
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))
        
        # asyncio.gather async tasks into a list
        original_pokemon = await asyncio.gather(*tasks)
        # just print the content
        for pokemon in original_pokemon:
            print(pokemon)
    # optional
    await session.close()

# asyncio.run()
asyncio.run(test_3())
print("--- %s seconds ---" % (time.time() - start_time))