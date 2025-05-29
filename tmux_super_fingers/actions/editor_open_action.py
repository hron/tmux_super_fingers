import sys
import os
import subprocess
from ..actions.action import Action
from ..targets.target_payload import EditorOpenable


class EditorOpenAction(Action):
    def __init__(self, target_payload: EditorOpenable):
        self.target_payload = target_payload

    def perform(self):
        path = self.target_payload.file_path

        if self.target_payload.line_number:
            path = f'+{self.target_payload.line_number} {path}'

        subprocess.Popen(
            f'emacs {path}',
            shell=True,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            close_fds=True,
            preexec_fn=os.setpgrp
        )
