from typing import Optional

from sshtunnel import SSHTunnelForwarder

from src.settings import settings


class Tunnel(object):
    _tunnel_port: int = 0
    _tunnel: Optional[SSHTunnelForwarder] = None

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Tunnel, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._tunnel = SSHTunnelForwarder(
            (settings.SSH_HOST, settings.SSH_PORT),
            ssh_username=settings.SSH_USERNAME,
            ssh_password=settings.SSH_PASSWORD,
            remote_bind_address=(settings.MYSQL_HOST, settings.MYSQL_PORT),
        )

    def get_tunnel(self):
        return self._tunnel

    def start(self):
        if self._tunnel is None:
            self.get_tunnel()
        self._tunnel.start()  # type: ignore
        self._tunnel_port = self._tunnel.local_bind_port  # type: ignore

    def stop(self):
        self.get_tunnel().stop()  # type: ignore

    def get_local_port(self):
        return self._tunnel_port
