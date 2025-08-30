import random
import string
from apify import Actor
import asyncio

def random_string(length=8):
    """Generate a random string of given length."""
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_row():
    """Generate a random row of data."""
    return {
        "id": random.randint(1000, 9999),
        "name": random_string(),
        "value": round(random.uniform(10, 100), 2),
        "active": random.choice([True, False]),
    }


async def main():
    async with Actor:
        Actor.log.info("🚀 Random row generator started!")

        # Get input (optional: number of rows to generate)
        actor_input = await Actor.get_input() or {}
        num_rows = actor_input.get("rows", 5)

        for _ in range(num_rows):
            row = random_row()
            Actor.log.info(f"Generated row: {row}")
            await Actor.push_data(row)

        Actor.log.info("✅ Finished generating random rows!")

if __name__ == "__main__":
    asyncio.run(main())
