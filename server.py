from mcp.server.fastmcp import FastMCP
from program_tool import ProgramTool
from dotenv import load_dotenv
import os

# Load env
load_dotenv()
API_KEY = os.getenv("FLEX_API_KEY")

# Init MCP server
mcp = FastMCP("flexoffers-mcp-server")

# Init tool
tool = ProgramTool(API_KEY)


@mcp.tool()
def get_program(program_id: int):
    """
    Get program details from FlexOffers API
    """
    return tool.get_program(program_id)


if __name__ == "__main__":
    mcp.run()