import time
import os
import datetime
import uuid
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
console=Console()
def time_save()->str:
        time=datetime.datetime.now().isoformat(timespec="seconds")
        iso_time=str(time.replace("T","/"))
        return iso_time
def generate_id()->str:
        id=uuid.uuid4().hex[:10]
        id_1=str(id)
        return id_1
def clear_menu()->None:
        command=("cls"if os.name=="nt" else "clear")
        os.system(command)

def show_intro() -> None:
    console.print(Panel("[bold cyan]Privacy-first. Fully Offline. Your data stays on your machine.[/bold cyan]",title="Neo Data Manager v1.7",subtitle="No cloud. No internet required."))
