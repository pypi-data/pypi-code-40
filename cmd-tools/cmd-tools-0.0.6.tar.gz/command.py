import json
from pathlib import Path
from subprocess import PIPE, call, run

import click


@click.command()
def hello():
    click.echo('hello world', nl=False)


@click.command()
@click.argument('command', nargs=-1)
def cmd(command):
    command = " ".join(command)
    result = run_command(command, useage='run')
    click.echo(result, nl=False)


def run_command(command, useage='run', **kwargs):
    if useage == 'run':
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True, **kwargs)
        output = result.stdout
        return output if output else result.stderr
    elif useage == 'call':
        result = call(command.split(' '), **kwargs)
        return result


def load_config(path=Path.home() / Path('.cmdrc.json')):
    if not path.exists():
        raise ValueError('~/.cmdrc.json not exist')
    with open(path, 'r') as f:
        config = f.read()

    try:
        config = json.loads(config)
    except json.decoder.JSONDecodeError:
        raise ValueError(f'{path} file format error')
    return config


@click.command()
@click.option('-n', '--name', type=str, help='name from json config', required=True)
def define(name):
    config = load_config()
    command, useage = config[name]['command'], config[name]['useage']
    result = run_command(command, useage)
    if useage == 'run':
        click.echo(result, nl=False)
