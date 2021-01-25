import os
import subprocess
import click
from src.utils.git import get_repo_abspath, get_url
from src.utils.shell import shell_run
from src.utils.config_file import read_config
from src.commands import hotfix_command, feature_command, release_command
from src.utils.config_file import CONFIG_FILE_NAME
from src.settings import color


failed_color = color.RED
succeed_color = color.GREEN
disable_color = color.END


def echo(output,verbose):
    verbose_output = output[0]
    note = output[1]
    status = output[2]
    if verbose:
        click.echo(verbose_output)
    if status == "succeed":
        color = succeed_color
    else:
        color = failed_color
    click.echo(color + note + disable_color)


@click.group()
@click.pass_context
def githubflow(ctx):
    ctx.obj["url"] = get_url()

@githubflow.command()
@click.option('-a','--action',required=True,help="create / ready / done")
@click.option('--verbose', '-v', is_flag=True, help="Verbose output.")
@click.argument('branch_name')
def hotfix(action,branch_name,verbose):
    """
    Manage Hotfix branch workflow. (READ MORE: https://documentation/hotfix)
    """
    output = hotfix_command.main(action, branch_name)
    echo(output, verbose)

@githubflow.command()
@click.option('-a','--action',required=True,help="create / ready / done")
@click.option('--verbose', '-v', is_flag=True, help="Vebose output.")
@click.argument('branch_name')
def feature(action,branch_name,verbose):
    """
    Manage Feature branch workflow. (READ MORE: https://documentation/feature)
    """
    output = feature_command.main(action, branch_name)
    echo(output, verbose)

@githubflow.command()
@click.option('-a','--action',required=True,help="create / publish")
@click.option('--verbose', '-v', is_flag=True, help="Vebose output.")
@click.argument('branch_name')
def release(action,branch_name,verbose):
    """
    Manage Release branch workflow. (READ MORE: https://documentation/release)
    """
    output = release_command.main(action, branch_name)
    echo(output, verbose)


def main():
    githubflow(obj={})


if __name__ == "__main__":
    main()