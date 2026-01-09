"""
Claude AI Agent for ROI-SLAB retrieval
"""
import json
from typing import List, Optional
from anthropic import Anthropic
from .config import config
from .models import ConversationMessage
from .prompts import get_system_prompt


class ClaudeAgent:
    """
    Claude-powered agent for translating natural language medical imaging
    requests into structured DAFS JSON format.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
    ):
        """
        Initialize the Claude agent.

        Args:
            api_key: Anthropic API key (defaults to config)
            model: Claude model to use (defaults to config)
            temperature: Sampling temperature (defaults to config)
            max_tokens: Maximum tokens in response (defaults to config)
        """
        self.api_key = api_key or config.get_api_key()
        self.model = model or config.ANTHROPIC_MODEL
        self.temperature = temperature if temperature is not None else config.TEMPERATURE
        self.max_tokens = max_tokens or config.MAX_TOKENS

        # Initialize Anthropic client
        self.client = Anthropic(api_key=self.api_key)

        # System prompt
        self.system_prompt = get_system_prompt()

        # Conversation history
        self.conversation_history: List[ConversationMessage] = []

    def chat(self, user_message: str) -> str:
        """
        Send a message to Claude and get a response.

        Args:
            user_message: The user's input message

        Returns:
            Claude's response as a string
        """
        # Add user message to history
        self.conversation_history.append(
            ConversationMessage(role="user", content=user_message)
        )

        # Prepare messages for API call
        messages = [
            {"role": msg.role, "content": msg.content}
            for msg in self.conversation_history
        ]

        try:
            # Call Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                system=self.system_prompt,
                messages=messages,
            )

            # Extract response text
            assistant_message = response.content[0].text

            # Add assistant response to history
            self.conversation_history.append(
                ConversationMessage(role="assistant", content=assistant_message)
            )

            return assistant_message

        except Exception as e:
            error_message = f"Error communicating with Claude API: {str(e)}"
            if config.DEBUG:
                print(f"DEBUG: {error_message}")
            return error_message

    def reset_conversation(self) -> None:
        """Reset the conversation history."""
        self.conversation_history = []

    def get_conversation_history(self) -> List[ConversationMessage]:
        """Get the current conversation history."""
        return self.conversation_history

    def set_system_prompt(self, new_prompt: str) -> None:
        """
        Update the system prompt.

        Args:
            new_prompt: New system prompt to use
        """
        self.system_prompt = new_prompt

    async def achat(self, user_message: str) -> str:
        """
        Async version of chat for use with async frameworks like Chainlit.

        Args:
            user_message: The user's input message

        Returns:
            Claude's response as a string
        """
        # For now, we'll use the sync version
        # Anthropic SDK supports async, but keeping it simple
        return self.chat(user_message)
