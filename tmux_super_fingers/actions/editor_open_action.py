import sys
import os
import subprocess
from ..actions.action import Action
from ..targets.target_payload import EditorOpenable


class EditorOpenAction(Action):
    def __init__(self, target_payload: EditorOpenable):
        self.target_payload = target_payload

    def perform(self):
        command = self.emacs_command()
        if os.environ.get('ZED_TERM') == "true":
            command = self.zed_command()

        subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            close_fds=True,
            preexec_fn=os.setpgrp
        )

    def zed_command(self):
        path = self.target_payload.file_path

        if self.target_payload.line_number:
            path = f'{path}:{self.target_payload.line_number} '
        return f'zed --add {path}'

    def emacs_command(self):
        path = self.target_payload.file_path

        if self.target_payload.line_number:
            path = f'+{self.target_payload.line_number} {path}'
        return f'emacs {path}'
