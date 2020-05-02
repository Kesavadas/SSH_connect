import subprocess
import sys


def login_ssh:
    HOST = "10.0.2.15"
    # Ports are handled in ~/.ssh/config since we use OpenSSH
    COMMAND = "uname -a"

    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if not result:
        error = ssh.stderr.readlines()
        print(sys.stderr, "ERROR: %s" % error)
    else:
        print(result)
