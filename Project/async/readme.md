# Goal
This is only a simple demo for how to use `asyncio` library.

`asyncio` is a library to write concurrent code using the async/await syntax.

`asyncio` is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

## Installation
Using pip package manager to install.

- `pip install asyncio`
- `pip install aiohttp`
- `pip install aiofiles`

Test code in Python 3.10

## Code Examples
- `async_http.py`: 
	+ fetch Pokeman API using HTTP GET
	+ read JSON files 
	+ print the data on terminal
	+ compare time on three approaches
- `async_io.py`: 
	+ fetch Pokeman API using HTTP GET
	+ read JSON files
	+ save the JSON data locally


## Reference
- https://docs.aiohttp.org/en/stable/
- https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp