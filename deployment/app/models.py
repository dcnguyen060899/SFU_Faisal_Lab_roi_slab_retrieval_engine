"""
Data models for ROI-SLAB combinations and JSON responses
"""
from typing import List, Literal
from pydantic import BaseModel, Field


class RoiSlab(BaseModel):
    """Single ROI-SLAB combination"""
    slabs: str = Field(..., description="Anatomical location (SLAB)")
    rois: str = Field(..., description="Region of interest (ROI)")


class RoiSlabList(BaseModel):
    """List of ROI-SLAB combinations"""
    roislabsList: List[RoiSlab] = Field(
        default_factory=list,
        description="List of ROI-SLAB combinations"
    )


class DAFSPublishConfig(BaseModel):
    """DAFS publish configuration for JSON output"""
    slabs: str = Field(..., description="Anatomical location (SLAB)")
    rois: str = Field(..., description="Region of interest (ROI)")
    cross_sectional_area: Literal["true", "false"] = Field(
        default="true",
        description="Include cross-sectional area measurement"
    )
    volume: Literal["true", "false"] = Field(
        default="true",
        description="Include volume measurement"
    )
    hu: Literal["true", "false"] = Field(
        default="true",
        description="Include Hounsfield Units measurement"
    )


class DAFSOutput(BaseModel):
    """Complete DAFS JSON output structure"""
    publish: DAFSPublishConfig


class ConversationMessage(BaseModel):
    """Represents a single message in the conversation"""
    role: Literal["user", "assistant"]
    content: str
