# ROI-SLAB Retrieval Engine

**[Live Demo](https://vha-roi-slab-retrieval-engine.onrender.com)**

An AI-powered chatbot that converts plain English medical imaging requests into structured JSON for the Data Analysis Facilitation Suite (DAFS).

## Overview

SFU Faisal Lab specializes in AI-based medical image analysis software, focusing on their Data Analysis Facilitation Suite (DAFS). DAFS is designed for automated analysis of CT and PET/CT images, offering powerful tools for body composition, organ, and tissue measurements. The software is 100% on-premise, ensuring data privacy and security. It is widely used in research institutes for applications in oncology, cardiac health, and clinical trials.

This chatbot eliminates the need for doctors to memorize complex ROI/SLAB combinations by translating natural language requests into the JSON format DAFS expects.

## How It Works

1. **Doctor inputs a request** in plain English
2. **AI identifies** the anatomical location (SLAB) and region of interest (ROI)
3. **JSON output** is generated for DAFS to process

### Example

**Input:** "I'm a doctor and I want to see patient A full scan of liver please?"

**AI Response:**
- **Slab**: FULL_SCAN
- **ROI**: LIV

**JSON Output:**
```json
{
  "publish": {
    "slabs": "FULL_SCAN",
    "rois": "LIV",
    "cross_sectional_area": "true",
    "volume": "true",
    "hu": "true"
  }
}
```

## Available Combinations

### SLAB (Anatomical Locations)

| SLAB | Description |
|------|-------------|
| `FULL_SCAN` | Full Body Scan |
| `T1` - `T12` | Thoracic vertebrae 1 through 12 |
| `L1` - `L5` | Lumbar vertebrae 1 through 5 |
| `SACRUM` | Sacrum |
| `avg-L3mid[1]` | Average at the midpoint of the third lumbar vertebra |
| `T12start-to-L5end` | Range from T12 start to L5 end |

**Point-Specific SLABs:**

| Vertebra | Points |
|----------|--------|
| T12 | `t12start`, `t12mid`, `t12end` |
| L1 | `l1start`, `l1mid`, `l1end` |
| L2 | `l2start`, `l2mid`, `l2end` |
| L3 | `l3start`, `l3mid`, `l3end` |
| L4 | `l4start`, `l4mid`, `l4end` |
| L5 | `l5start`, `l5mid`, `l5end` |
| Sacrum | `sacrumstart`, `sacrummid`, `sacrumend` |

### ROI (Regions of Interest)

| ROI | Description |
|-----|-------------|
| `FULL_SCAN` | Full Scan |
| `ALLSKM` | All Skeletal Muscle |
| `SAT` | Subcutaneous Adipose Tissue |
| `ALLFAT` | All Fat Tissue |
| `ALLIMAT` | All Imaging Material |
| `VAT` | Visceral Adipose Tissue |
| `EpAT` | Epidural Adipose Tissue |
| `PaAT` | Paravertebral Adipose Tissue |
| `ThAT` | Thoracic Adipose Tissue |
| `LIV` | Liver |
| `SPL` | Spleen |
| `AOC` | Abdominal Oblique Composite |
| `CAAC` | Combined Abdominal Adipose Compartment |

### Modifiers

| Modifier | Description |
|----------|-------------|
| `NOARMS` | Excludes arm measurements (append with underscore, e.g., `ALLSKM_NOARMS`) |
| `[min,max]` | Measurement range in Hounsfield Units (e.g., `ALLSKM[-29,150]`) |

## Example Requests

| Request | SLAB | ROI | JSON Output |
|---------|------|-----|-------------|
| "Full scan of liver" | `FULL_SCAN` | `LIV` | `{"slabs": "FULL_SCAN", "rois": "LIV", ...}` |
| "L3 midpoint all skeletal muscle" | `l3mid` | `ALLSKM` | `{"slabs": "l3mid", "rois": "ALLSKM", ...}` |
| "Average L3 mid for skeletal muscle at -29 to 150 without arms" | `avg-L3mid[1]` | `ALLSKM[-29,150]_NOARMS` | `{"slabs": "avg-L3mid[1]", "rois": "ALLSKM[-29,150]_NOARMS", ...}` |
| "T12 start to L5 end for all imaging materials" | `T12start-to-L5end` | `ALLIMAT` | `{"slabs": "T12start-to-L5end", "rois": "ALLIMAT", ...}` |
| "Visceral adipose tissue at sacrum" | `SACRUM` | `VAT` | `{"slabs": "SACRUM", "rois": "VAT", ...}` |
| "Spleen at L2" | `L2` | `SPL` | `{"slabs": "L2", "rois": "SPL", ...}` |

## Tech Stack

- **LLM**: Claude Sonnet 4.5 (Anthropic API)
- **Framework**: [Chainlit](https://chainlit.io/) (Chat UI)
- **Architecture**: Modular Python application with direct API integration
- **Deployment**: [Render](https://render.com/)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/SFU_Faisal_Lab_roi_slab_retrieval_engine.git
   cd SFU_Faisal_Lab_roi_slab_retrieval_engine
   ```

2. Install dependencies:
   ```bash
   cd deployment
   pip install -r requirements.txt
   ```

3. Set environment variables:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key"
   export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"
   ```

4. Run the application:
   ```bash
   cd deployment
   chainlit run app/main.py --host 0.0.0.0 --port 8000
   ```

## Project Structure

```
├── deployment/
│   ├── app/
│   │   ├── __init__.py      # Package initialization
│   │   ├── main.py          # Chainlit UI and handlers
│   │   ├── agent.py         # Claude AI agent wrapper
│   │   ├── config.py        # Configuration management
│   │   ├── models.py        # Pydantic data models
│   │   └── prompts.py       # System prompts
│   ├── requirements.txt     # Production dependencies
│   ├── .env.example        # Environment variables template
│   └── README.md           # Deployment documentation
├── chainlit/               # Legacy implementations (archived)
├── src/
│   └── run_demo.ipynb     # Jupyter notebook demo
└── README.md              # This file
```

## License

This project is developed by SFU Faisal Lab.
