import os
import datetime
import logging
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
        print("No log files found")
        return
    with open(LOG_PATH,"r",encoding="utf-8") as g:
        lines=g.readlines()
        if filter_type=="errors":
            result=[l for l in lines if "ERROR" in l or "CRITICAL" in l]
        elif filter_type=="today":
            result=[l for l in lines if today in l]
        else:
            result=lines
        if not result:
            print("No log record found")
            return
        for lines in result:
            print(lines.strip())
def clear_log():
    try:
        with open(LOG_PATH,"w",encoding="utf-8") as f:
            f.truncate(0)
            print("Logs cleared successfully")
            log_info("Logs cleared by user", level="WARNING")
    except Exception as e:
        print("An Unknown Error Occured")
        log_his(f"ERROR : {e}",level="CRITICAL")
def log_menu():
    while True:
        try:
            print("="*25+"LOG MENU"+"="*25)
            print("1. Today's Log")
            print("2. View Error log")
            print("3. Clear log")
            print("4. Return to  Main Menu")
            choice=int(input("Please enter your choice in integers : ").strip())
            if choice==1:
                log_his("today")
            elif choice==2:
                log_his("errors")
            elif choice==3:
                clear_log()
            elif choice==4:
                return
        except ValueError:
            log_info("User Entered an Invalid Input",level="WARNING")
        except Exception as e:
            log_info(f"ERROR : {e}",level="CRITICAL")
            print("An Unknown Error Occured")