__author__ = "Ricardo Wurmus"
__copyright__ = "Copyright 2023, Ricardo Wurmus"
__email__ = "ricardo.wurmus@mdc-berlin.de"
__license__ = "MIT"


class Guix:

    """Run command inside a containerized Guix shell"""

    def __init__(self, guix_command="guix"):
        self.default_guix_shell_args = [
            "--container",
            "--network",
            "--emulate-fhs"
        ]
        self.guix = guix_command

    def shellcmd(self, manifest, cmd):
        """Return shell command with given modules loaded."""
        command = "{guix} shell {guix_shell_args} -m {manifest} -- /bin/sh -c '{cmd}'".format(
            guix=self.guix,
            guix_shell_args=" ".join(self.default_guix_shell_args),
            cmd=cmd.replace("'", r"'\''"),
        return command
