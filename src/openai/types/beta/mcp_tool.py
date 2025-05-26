from __future__ import annotations

from typing import Optional, List, Dict, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "McpTool",
    "McpAllowedTools",
    "McpAllowedToolsMcpAllowedToolsFilter",
    "McpRequireApproval",
    "McpRequireApprovalMcpToolApprovalFilter",
    "McpRequireApprovalMcpToolApprovalFilterAlways",
    "McpRequireApprovalMcpToolApprovalFilterNever",
]


class McpAllowedToolsMcpAllowedToolsFilter(BaseModel):
    tool_names: Optional[List[str]] = None
    """List of allowed tool names."""


McpAllowedTools: TypeAlias = Union[List[str], McpAllowedToolsMcpAllowedToolsFilter, None]


class McpRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    tool_names: Optional[List[str]] = None
    """List of tools that require approval."""


class McpRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    tool_names: Optional[List[str]] = None
    """List of tools that do not require approval."""


class McpRequireApprovalMcpToolApprovalFilter(BaseModel):
    always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways] = None
    """A list of tools that always require approval."""

    never: Optional[McpRequireApprovalMcpToolApprovalFilterNever] = None
    """A list of tools that never require approval."""


McpRequireApproval: TypeAlias = Union[McpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"], None]


class McpTool(BaseModel):
    server_label: str
    """A label for this MCP server, used to identify it in tool calls."""

    server_url: str
    """The URL for the MCP server."""

    type: Literal["mcp"]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[McpAllowedTools] = None
    """List of allowed tool names or a filter object."""

    headers: Optional[Dict[str, str]] = None
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[McpRequireApproval] = None
    """Specify which of the MCP server's tools require approval."""

