import nest_asyncio
nest_asyncio.apply()

from mcp.server.fastmcp import FastMCP
from program_tool import ProgramTool
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("FLEX_API_KEY")

mcp = FastMCP("flexoffers-mcp")
tool = ProgramTool(API_KEY)

@mcp.tool()
def get_program(program_id: int):
    return tool.get_program(program_id)

if __name__ == "__main__":
    mcp.run()