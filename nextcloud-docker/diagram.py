from diagrams import Diagram
from diagrams.onprem.container import Docker
from diagrams.onprem.compute import Server

with Diagram("Nextcloud containerized", show=False):
    Server("Debian") >> Docker("Haproxy") >> Docker("Nextcloud") >> Docker("Mariadb")
