import subprocess


def run(cmd):
    return subprocess.run(
        cmd.split(' '),
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8')
