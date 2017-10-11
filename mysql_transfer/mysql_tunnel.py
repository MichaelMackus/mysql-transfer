from mysql_params import Params

import sshtunnel

def open_tunnel(ssh_params, remote_params, local_params=None):
    """
    Open SSH tunnel to remote host.


    ARGUMENTS:

    ssh_params - remote SSH server parameters (instance of SSHParams)
    remote_params - remote MySQL server (instance of Params)
    local_params - local MySQL server to listen on (instance of Params)
    """

    return sshtunnel.SSHTunnelForwarder(
        (ssh_params.host, ssh_params.port),
        ssh_username=ssh_params.user,
        ssh_pkey=ssh_params.key,
        remote_bind_address=(remote_params.host, remote_params.port),
        local_bind_address=(
            local_params.host if local_params is not None else '127.0.0.1',
            local_params.port if local_params is not None else 3306))


class SSHParams(Params):
    """
    Parameters for SSH tunnel.
    """

    def __init__(self, host, username='root', key=None, port=22):
        super(self.__class__, self).__init__(host, port, user=username)
        self.key = key

