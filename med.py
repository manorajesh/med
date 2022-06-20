#!/usr/bin/env python
import click
from main import med

@click.command()
@click.option('file', help='The file to read', type=click.File('r'))
@click.option('--prompt', '-p', help='The prompt to display', type=str)
@click.version_option(version='0.0.1')
@click.help_option('--help', '-h')

def main(file, prompt):
    '''A line-oriented text editor that reads and writes from and to a FILE.'''
    med(file, prompt)
    
if __name__ == '__main__':
    main()