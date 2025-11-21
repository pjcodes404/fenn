import traceback
import sys
from colorama import Fore, Style

from smle.args import Parser
from smle.logging import Logger
from smle.utils import generate_haiku_id

class SMLE:

    """
    The base SMLE application
    """

    def __init__(self):
        self._session_id = generate_haiku_id()
        self._entrypoint_fn = None
        self._parser = Parser()
        self._args = self._parser.load_configuration()
        self._args["session_id"] = self._session_id
        self._logger = Logger(self._args)

    def entrypoint(self, entrypoint_fn):
        """
        The decorator to register the main execution function.
        """
        self._entrypoint_fn = entrypoint_fn
        return entrypoint_fn

    def run(self):
        """
        The method that executes the application's core logic.
        """

        if not self._entrypoint_fn:
            print(f"{Fore.RED}[SMLE] No main function registered. {Style.RESET_ALL}")
            print(f"{Fore.RED}[SMLE] Please use {Fore.LIGHTYELLOW_EX}@app.entrypoint{Fore.RED} to register your main function{Style.RESET_ALL}")
            sys.exit(1)

        self._logger.start()

        self._parser.print()

        try:
            # The execution of the decorated user function
            print(f"{Fore.GREEN}[SMLE] Application starting from {Fore.LIGHTYELLOW_EX}{self._entrypoint_fn.__name__}{Fore.GREEN} entrypoint.{Style.RESET_ALL}")
            return self._entrypoint_fn(self._args)
        except Exception:
            # Print the traceback on failure
            print(traceback.format_exc())
            sys.exit(1)
        finally:
            self._logger.stop()