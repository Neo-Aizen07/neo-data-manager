import os
import datetime
import logging
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
console=Console()
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
LOG_PATH=os.path.join(BASE_DIR,"error.log")
logger=logging.getLogger(__name__)
handler=logger.setLevel(logging.DEBUG)
handler=logging.FileHandler(LOG_PATH)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)
def log_info(message,level="INFO"):
    if level=="WARNING":
        logger.warning(message)
    elif level=="INFO":
        logger.info(message)
    elif level=="CRITICAL":
        logger.critical(message)
    elif level=="ERROR":
        logger.error(message)
def log_his(filter_type="all"):
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    if not os.path.exists(LOG_PATH):
        console.print(Text("No log records found", style="yellow"))
        return
    with open(LOG_PATH,"r",encoding="utf-8") as g:
        lines=g.readlines()
        if filter_type=="errors":
            result=[l for l in lines if "ERROR" in l]
        elif filter_type=="today":
            result=[l for l in lines if today in l]
        elif filter_type=="info":
            result=[l for l in lines if "INFO" in l]
        elif filter_type=="warning":
            result=[l for l in lines if "WARNING" in l]
        elif filter_type=="critical":
            result=[l for l in lines if "CRITICAL" in l]
        else:
            result=lines
        if not result:
            console.print(Text("No log records found", style="yellow"))
            return
        for line in result:
            line=line.strip()
            if "CRITICAL" in line:
                console.print(Text(line, style="bold red"))
            elif "ERROR" in line:
                console.print(Text(line, style="red"))
            elif "WARNING" in line:
                console.print(Text(line, style="yellow"))
            else:
                console.print(Text(line, style="white"))
def clear_log():
    try:
        with open(LOG_PATH,"w",encoding="utf-8") as f:
            f.truncate(0)
            console.print(Text("Logs cleared successfully", style="green"))
            log_info("Logs cleared by user", level="WARNING")
    except Exception as e:
        console.print(Text("Failed to clear logs", style="bold red"))
        log_his(f"ERROR : {e}",level="CRITICAL")
def log_menu():
    while True:
        try:
            console.print(Panel(
                "[1] Today's Logs\n"
                "[2] Error Logs\n"
                "[3] Warning Logs\n"
                "[4] Info Logs\n"
                "[5] Critical Logs\n"
                "[6] All Logs\n"
                "[7] Clear Logs\n"
                "[8] Return to Main Menu",
                title="Log Menu",
                style="magenta"))
            choice=int(input("Please enter your choice in integers : ").strip())
            if choice==1:
                log_his("today")
            elif choice==2:
                log_his("errors")
            elif choice==3:
                log_his("warning")
            elif choice==4:
                log_his("info")
            elif choice==5:
                log_his("critical")
            elif choice==6:
                log_his("all")
            elif choice==7:
                clear_log()
            elif choice==8:
                return
            else:
                console.print(Text("Please enter a valid number",style="yellow"))
                log_info(f"User Entered an Invalid Input{choice}",level="WARNING")
        except ValueError:
            console.print(Text("Please enter a valid number", style="bold red"))
            log_info("User Entered an Invalid Input",level="WARNING")
        except Exception as e:
            console.print(Text("An error occurred", style="bold red"))
            log_info(f"ERROR : {e}",level="CRITICAL")