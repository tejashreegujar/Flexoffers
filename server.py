from mcp.server.fastmcp import FastMCP
from program_tool import ProgramTool
import os

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
@mcp.tool()
def update_program_categories(program_id: int,category_ids: list[int],mode: str,reason: str,source: str = "MILO Claw"):
    """Update categories for a FlexOffers program using category IDs, mode, reason, and source."""
    return tool.update_program_categories(program_id, category_ids, mode, reason, source)

@mcp.tool()
def update_program_status(program_ids: list[int],action: str,reason: str,source: str = "MILO Claw",dry_run: bool = False,send_notifications: bool = True):
    return tool.update_program_status(program_ids,action,reason,source,dry_run,send_notifications)

if __name__ == "__main__":
    mcp.run()