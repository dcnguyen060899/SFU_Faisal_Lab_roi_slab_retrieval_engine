"""
Configuration management for the ROI-SLAB Retrieval Engine
"""
import os
from typing import Optional


class Config:
    """Application configuration"""

    # Claude API Configuration
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    ANTHROPIC_MODEL: str = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")

    # Model Parameters
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "4096"))

    # Application Settings
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    @classmethod
    def validate(cls) -> None:
        """Validate required configuration"""
        if not cls.ANTHROPIC_API_KEY:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is required. "
                "Please set it in your environment or .env file."
            )

    @classmethod
    def get_api_key(cls) -> str:
        """Get API key with validation"""
        if not cls.ANTHROPIC_API_KEY:
            cls.validate()
        return cls.ANTHROPIC_API_KEY


config = Config()
