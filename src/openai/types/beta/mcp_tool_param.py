from __future__ import annotations

from typing import Dict, List, Optional, Union
from typing_extensions import Literal, Required, TypedDict, TypeAlias

__all__ = [
    "McpToolParam",
    "McpAllowedTools",
    "McpAllowedToolsMcpAllowedToolsFilter",
    "McpRequireApproval",
    "McpRequireApprovalMcpToolApprovalFilter",
    "McpRequireApprovalMcpToolApprovalFilterAlways",
    "McpRequireApprovalMcpToolApprovalFilterNever",
]


class McpAllowedToolsMcpAllowedToolsFilter(TypedDict, total=False):
    tool_names: List[str]
    """List of allowed tool names."""


McpAllowedTools: TypeAlias = Union[List[str], McpAllowedToolsMcpAllowedToolsFilter]


class McpRequireApprovalMcpToolApprovalFilterAlways(TypedDict, total=False):
    tool_names: List[str]
    """List of tools that require approval."""


class McpRequireApprovalMcpToolApprovalFilterNever(TypedDict, total=False):
    tool_names: List[str]
    """List of tools that do not require approval."""


class McpRequireApprovalMcpToolApprovalFilter(TypedDict, total=False):
    always: McpRequireApprovalMcpToolApprovalFilterAlways
    """A list of tools that always require approval."""

    never: McpRequireApprovalMcpToolApprovalFilterNever
    """A list of tools that never require approval."""


McpRequireApproval: TypeAlias = Union[McpRequireApprovalMcpToolApprovalFilter, Literal["always", "never"]]


class McpToolParam(TypedDict, total=False):
    server_label: Required[str]
    """A label for this MCP server, used to identify it in tool calls."""

    server_url: Required[str]
    """The URL for the MCP server."""

    type: Required[Literal["mcp"]]
    """The type of the MCP tool. Always `mcp`."""

    allowed_tools: Optional[McpAllowedTools]
    """List of allowed tool names or a filter object."""

    headers: Optional[Dict[str, str]]
    """Optional HTTP headers to send to the MCP server.

    Use for authentication or other purposes.
    """

    require_approval: Optional[McpRequireApproval]
    """Specify which of the MCP server's tools require approval."""

