from subprocess import Popen, PIPE, check_output

def shell_run(*args):
    """run command on shell, return unicode"""
    return check_output(shell=True, *args).decode("utf-8").rstrip("\n")

def execute(cmd_list):
    process = Popen(cmd_list, stdout=PIPE, stderr=PIPE, shell=False)
    stdout, stderr = process.communicate()
    if stderr != b'':
        type = "stderr"
        msg = stderr
    else:
        type = "stdout"
        msg = stdout
    return [type,msg]

