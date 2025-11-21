import argparse
from pathlib import Path
from importlib.resources import files
from colorama import Fore, Style
import sys

def execute(args: argparse.Namespace) -> None:

    root_dir = Path(args.path).resolve()
    # Get the path to the 'templates' folder relative to the current package
    templates_path = files(__package__).joinpath('templates')

    if root_dir.exists() and any(root_dir.iterdir()) and not args.force:
        print(f"{Fore.RED}[SMLE] Refusing to init non-empty directory {Fore.LIGHTYELLOW_EX}{root_dir}{Fore.RED}. Use {Fore.LIGHTYELLOW_EX}--force{Fore.RED} to override.{Style.RESET_ALL}")
        sys.exit(1)

    root_dir.mkdir(parents=True, exist_ok=True)

    dirs = [
        "logger",
        "dataset",
        "models"
    ]

    for d in dirs:
        (root_dir / d).mkdir(exist_ok=True)

    # Config
    config_path = root_dir / "smle.yaml"
    with open(templates_path/"smle.yaml", "r") as f:
        config_template = f.read()
    config_path.write_text(config_template)


    # Template script
    script_path = root_dir / "main.py"

    with open(templates_path/ f"{args.template}.py", "r") as f:
        script_template = f.read()
    script_path.write_text(script_template)

    print(f"{Fore.GREEN}[SMLE] Initialized {Fore.LIGHTYELLOW_EX}{args.template}{Fore.GREEN} template in {Fore.LIGHTYELLOW_EX}{root_dir}{Fore.GREEN} directory.{Style.RESET_ALL}")