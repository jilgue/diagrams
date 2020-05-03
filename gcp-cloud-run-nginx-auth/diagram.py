from diagrams import Diagram
from diagrams.gcp.compute import Run

with Diagram("Nginx Auth", show=False):
    Run("Nginx (public)") >> [Run("Front (private)"),
                              Run("Back (private)")]
