"""
Model Context Protocol (MCP) Screenshot Server
----------------------------------------------
This module implements an MCP (Model Context Protocol) server that enables LLM-based AI agents to capture screenshots of the current screen.

Key Features:
- Provides a tool for LLM agents to request and receive screenshots.
- Uses pyautogui to capture the screen.
- Returns the screenshot as a JPEG image with reduced quality for efficiency.
- Designed for integration with AI agents and LLMs via the MCP protocol.

Usage Example:
    Take a screenshot and return as an image:
        take_screenshot()
"""
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image
import io
import pyautogui

mcp = FastMCP("screenshot")

@mcp.tool()
def take_screenshot() -> Image:
    """
    Capture the current screen and return it as a JPEG image.

    Returns:
        Image: An Image object containing the screenshot data in JPEG format.

    Example:
        take_screenshot()
    """
    buffer = io.BytesIO()
    screenshot = pyautogui.screenshot()
    screenshot.convert('RGB').save(buffer, format='jpeg', quality=30, optimize=True)
    return Image(data=buffer.getvalue(), format='jpeg')

# Only run the MCP server if this script is executed directly
if __name__ == "__main__":
    mcp.run(transport='stdio')