import os
import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import Type, Optional
from .target_payload import OsOpenable
from .target_payload import EditorOpenable
from ..actions.action import Action
from ..actions.editor_open_action import EditorOpenAction
from ..actions.os_open_action import OsOpenAction
from .target import Target


@dataclass
class FileTargetPayload(OsOpenable, EditorOpenable):
    @property
    def file_or_url(self) -> str:
        return self.file_path


class ContentType(Enum):
    """three file types returned by unix `file` command"""
    TEXT = auto()
    DATA = auto()


@dataclass
class FileTarget(Target):
    file_path: str
    content_type: ContentType
    line_number: Optional[int] = None

    @property
    def payload(self) -> FileTargetPayload:
        return FileTargetPayload(
            file_path=self.file_path,
            line_number=self.line_number
        )

    @property
    def default_primary_action(self) -> Type[Action]:
        # if self.content_type == ContentType.TEXT and re.search('^n?vim', os.environ['EDITOR']):
        #     return SendToVimInTmuxPaneAction
        # else:
        #     return OsOpenAction
        return EditorOpenAction

    @property
    def default_secondary_action(self) -> Type[Action]:
        # return CopyToClipboardAction
        return OsOpenAction
