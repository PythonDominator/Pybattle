from inspect import getframeinfo, stack
from logging import DEBUG, FileHandler, Formatter, getLogger
from os import mkdir
from pathlib import Path

logger = getLogger('global')

logger.setLevel(DEBUG)

__handler = FileHandler(Path('log.log'), mode='w')
__formatter = Formatter(
    "%(levelname)s: %(message)s")  # LEVEL: message

__handler.setFormatter(__formatter)

logger.addHandler(__handler)


# class FileLogger:
#     """A logger for a file. When you log it also goes into a global log file."""

#     def __init__(self, file_name: str = ..., default_level: int = DEBUG) -> None:
#         if file_name == ...:
#             file_name = getframeinfo(stack()[1][0]).filename  # The file path
#         self.default_level = default_level

#         # ...\tester.py -> tester
#         # tester.py -> tester
#         # tester -> tester
#         name = Path(file_name).stem

#         logger = getLogger(name)

#         if not logger.hasHandlers():  # If logger has been created (it has no handlers)
#             logger.setLevel(default_level)

#             handler = FileHandler(Path('Loggers/' + name + '.log'), mode='w')
#             formatter = Formatter(
#                 "%(levelname)s: %(message)s")  # LEVEL: message

#             handler.setFormatter(formatter)

#             logger.addHandler(handler)

#         self.logger = logger

#     def log(self, msg: str, level: int = ...) -> None:
#         if level is ...:
#             level = self.default_level
#         self.logger.log(level, msg)
#         logger.log(level, msg)

#     def debug(self, msg: str) -> None:
#         self.logger.debug(msg)
#         logger.debug(msg)

#     def warning(self, msg: str) -> None:
#         self.logger.warning(msg)
#         logger.warning(msg)

#     def info(self, msg: str) -> None:
#         self.logger.info(msg)
#         logger.info(msg)