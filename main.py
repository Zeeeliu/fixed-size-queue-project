import argparse
from src.cli import run_cli
from src.api.queue_api import app as api_app


def main():
    parser = argparse.ArgumentParser(description="Fixed Size Queue Application")
    parser.add_argument("--mode", choices=["cli", "api"], default="cli",
                        help="Run mode: cli for Command Line Interface (capacity can be entered as an input, "
                             "api for REST API (default capacity is 5)")
    args = parser.parse_args()

    if args.mode == "cli":
        run_cli()
    else:
        api_app.run(debug=True, host='0.0.0.0', port=5001)


if __name__ == "__main__":
    main()
