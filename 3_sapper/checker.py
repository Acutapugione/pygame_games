# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import threading
# from pathlib import Path

# from config import *


# class Checker:
#     def __init__(self) -> None:
#         pass

#     def check_sq_size(self):
#         if WIDTH / SQ_AMOUNT < 10:
#             print(True)
#             raise Exception("Square size cant be lower than 10px!")


# class FileSaveHandler(FileSystemEventHandler):
#     def __init__(self) -> None:
#         self.checker = Checker()
#         self.path_to_watch = "C:/Users/ОК/Desktop/road to fullstack developer/BACKEND/python/30 days - 30 projects/day_3_sapper"

#     def on_modified(self, event):
#         if Path(event.src_path) == Path(f"{self.path_to_watch}/config.py"):
#             print("file {} has been modified".format(event.src_path.split('\\')[-1]))
#             self.checker.check_sq_size()


# def start_observer():
#     filesave_handler = FileSaveHandler()
#     observer = Observer()
#     observer.schedule(filesave_handler,
#                       filesave_handler.path_to_watch, recursive=False)
#     observer.start()
#     observer.join()


# if __name__ == "__main__":
#     observer_thread = threading.Thread(target=start_observer)
#     # Це дозволить програмі завершитися, коли завершиться основний потік
#     observer_thread.daemon = True
#     observer_thread.start()

#     try:
#         while True:
#             time.sleep(5)
#             print("No changes detected...")
#     except KeyboardInterrupt:
#         print("Bye-Bye")
