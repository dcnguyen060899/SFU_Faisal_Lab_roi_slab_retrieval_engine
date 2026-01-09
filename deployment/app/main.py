"""
ROI-SLAB Retrieval Engine - Main Application
AI-powered chatbot for translating natural language medical imaging requests
into structured JSON for DAFS (Data Analysis Facilitation Suite)
"""
import chainlit as cl
from app.agent import ClaudeAgent
from app.config import config


# Global agent instance (persists across sessions)
agent = None


@cl.on_chat_start
async def start():
    """Initialize chat session"""
    global agent

    try:
        # Validate configuration
        config.validate()

        # Initialize Claude agent
        agent = ClaudeAgent()

        # Send welcome message
        welcome_message = """Welcome to the ROI-SLAB Retrieval Engine! 🏥

I'm here to help you translate your medical imaging requests into structured JSON format for the Data Analysis Facilitation Suite (DAFS).

**How to use:**
1. Describe what you want to see in plain English
2. I'll identify the anatomical location (SLAB) and region of interest (ROI)
3. I'll generate the JSON output for DAFS

**Example requests:**
- "Full scan of liver"
- "L3 midpoint all skeletal muscle"
- "Average L3 mid for skeletal muscle at -29 to 150 without arms"

Try asking me for a medical imaging analysis!"""

        await cl.Message(content=welcome_message).send()

    except ValueError as e:
        error_msg = f"Configuration Error: {str(e)}"
        await cl.Message(content=error_msg).send()
        raise


@cl.on_message
async def main(message: cl.Message):
    """
    Handle incoming user messages

    Args:
        message: User's message from Chainlit
    """
    global agent

    # Get user's message content
    user_input = message.content

    try:
        # Get response from Claude agent
        response = await agent.achat(user_input)

        # Send response back to user
        await cl.Message(content=response).send()

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        if config.DEBUG:
            error_message += f"\n\nDebug info: {type(e).__name__}"

        await cl.Message(content=error_message).send()


@cl.on_chat_end
async def end():
    """Clean up when chat session ends"""
    global agent

    if agent:
        agent.reset_conversation()
