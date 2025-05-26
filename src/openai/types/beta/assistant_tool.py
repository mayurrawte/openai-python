# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .function_tool import FunctionTool
from .file_search_tool import FileSearchTool
from .code_interpreter_tool import CodeInterpreterTool
from .mcp_tool import McpTool

__all__ = ["AssistantTool"]

AssistantTool: TypeAlias = Annotated[
    Union[CodeInterpreterTool, FileSearchTool, FunctionTool, McpTool],
    PropertyInfo(discriminator="type"),
]
