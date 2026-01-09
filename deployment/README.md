# ROI-SLAB Retrieval Engine - Deployment

AI-powered chatbot that converts natural language medical imaging requests into structured JSON for DAFS (Data Analysis Facilitation Suite).

## Architecture

This application uses a **modular architecture** powered by **Claude (Anthropic API)**:

```
deployment/
├── app/
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Chainlit UI and event handlers
│   ├── agent.py          # Claude AI agent wrapper
│   ├── config.py         # Configuration management
│   ├── models.py         # Pydantic data models
│   └── prompts.py        # System prompts
├── requirements.txt      # Python dependencies
└── .env.example         # Environment variables template
```

## Setup

### 1. Install Dependencies

```bash
cd deployment
pip install -r requirements.txt
```

### 2. Configure Environment Variables

**Option A: Using .env file (local development)**
```bash
cp .env.example .env
# Edit .env and add your API key
```

**Option B: Set environment variables directly (production)**
```bash
export ANTHROPIC_API_KEY="your_api_key_here"
export CLAUDE_MODEL="claude-3-5-sonnet-20241022"
export TEMPERATURE="0.7"
export MAX_TOKENS="4096"
```

### 3. Run the Application

```bash
cd deployment
chainlit run app/main.py --host 0.0.0.0 --port 8000
```

## Configuration

All configuration is managed in `app/config.py` and can be set via environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Anthropic API key (required) | - |
| `ANTHROPIC_MODEL` | Claude model to use | `claude-sonnet-4-5-20250929` |
| `TEMPERATURE` | Sampling temperature (0-1) | `0.7` |
| `MAX_TOKENS` | Maximum tokens in response | `4096` |
| `DEBUG` | Enable debug mode | `false` |

## Modular Components

### `agent.py` - Claude AI Agent
- Wraps the Anthropic API
- Manages conversation history
- Handles chat interactions
- Provides both sync and async interfaces

### `config.py` - Configuration Management
- Centralized configuration
- Environment variable handling
- Validation and defaults

### `models.py` - Data Models
- Pydantic models for type safety
- ROI/SLAB data structures
- DAFS JSON output format
- Conversation messages

### `prompts.py` - System Prompts
- Medical imaging domain knowledge
- SLAB and ROI definitions
- Response formatting instructions
- Example interactions

### `main.py` - Chainlit Application
- User interface layer
- Event handlers (chat start, message, end)
- Error handling
- Session management

## Deployment on Render

### Environment Variables
Set the following in Render dashboard:
```
ANTHROPIC_API_KEY=your_actual_api_key
ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
```

### Build Command
```bash
pip install -r requirements.txt
```

### Start Command
```bash
cd deployment && chainlit run app/main.py --host 0.0.0.0 --port 8000
```

## Development

### Adding New Features

1. **Data models**: Add to `models.py`
2. **Prompt engineering**: Update `prompts.py`
3. **Agent logic**: Extend `agent.py`
4. **UI/UX**: Modify `main.py`
5. **Configuration**: Update `config.py`

### Testing Locally

```bash
# Set environment variables
export ANTHROPIC_API_KEY="your_test_key"

# Run the app (from project root)
cd deployment
chainlit run app/main.py

# Open browser to http://localhost:8000
```

## Migration from OpenAI/LlamaIndex

This version has been migrated from OpenAI + LlamaIndex to Claude API:

**Benefits:**
- ✅ Simpler architecture (no complex agent framework)
- ✅ Better medical domain understanding
- ✅ More reliable JSON generation
- ✅ Modular codebase for easier maintenance
- ✅ Direct API integration (no middleware)

## License

Developed by SFU Faisal Lab for Voronoi Health Analytics.
