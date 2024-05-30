import os
from dotenv import load_dotenv, dotenv_values

import asyncio
import telegram


load_dotenv()

async def main():
    bot = telegram.Bot(os.getenv("API_KEY"))
    async with bot:
        print(await bot.get_me())

if __name__ == "__main__":
    asyncio.run(main())

