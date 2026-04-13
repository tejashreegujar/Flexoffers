from mcp.server.fastmcp import FastMCP
from program_tool import ProgramTool
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = "kz0PVV5xAR3VO4RofsljMqADFTxGGRttaWQ6m2QJj1h8hfOuEH5KFi8msIFq8C2p"

mcp = FastMCP("flexoffers-mcp")
tool = ProgramTool(API_KEY)

@mcp.tool()
def get_program(program_id: int):
    return tool.get_program(program_id)
@mcp.tool()
def post_program_preFlight(program_id: int):
    return tool.post_program_preFlight(program_id)
@mcp.tool()
def get_categories():
    return tool.get_categories()

if __name__ == "__main__":
    mcp.run()