#!/usr/bin/env python3
import click
from main import med

@click.command()
@click.argument('file', type=str, default="")
@click.option('--prompt', '-p', help='The prompt to display', type=str, default="")
@click.version_option(version='0.1.25')
@click.help_option('--help', '-h')

def main(file, prompt):
    """A line-oriented text editor that reads and writes from and to a FILE."""
    med(file, prompt)
    
if __name__ == '__main__':
    main()