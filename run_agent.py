import asyncio
from agent_setup import runner

async def run_query(query: str):
    response = await runner.run_debug(query)
    # print("Response:", response)

if __name__ == "__main__":
    query = "What are the latest advancements in quantum computing and what do they mean for AI?"
    asyncio.run(run_query(query))
