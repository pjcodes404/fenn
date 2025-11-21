def init(args: argparse.Namespace) -> None:
    root = Path(args.path).resolve()


    if root.exists() and any(root.iterdir()) and not args.force:
        raise SystemExit(
            f"Refusing to init non-empty directory: {root}. Use --force to override."
        )


    root.mkdir(parents=True, exist_ok=True)


    # Folders
    (root / "logger").mkdir(exist_ok=True)


    # Config
    config_path = root / "smle.yaml"
    if config_path.exists() and not args.force:
        raise SystemExit("smle.yaml already exists; use --force to overwrite.")
    config_path.write_text(CONFIG_TEMPLATE)


    # Example training script
    train_path = root / "main.py"
    if not train_path.exists() or args.force:
        train_path.write_text(SCRIPT_TEMPLATE)


    print(f"Initialized smle project in {root}")