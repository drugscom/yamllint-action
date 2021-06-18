import os


def debug(message: str, **params: str) -> None:
    send_command("debug", message, **params)


def error(message: str, **params: str) -> None:
    send_command("error", message, **params)


def get_input(name: str) -> str:
    name = f"INPUT_{name.replace(' ', '_').upper()}"
    return os.getenv(name, "").strip()


def send_command(name: str, value: str = "", **params: str) -> None:
    params_str = ",".join([f"{k}={v}" for k, v in params.items()])
    if params_str:
        params_str = f" {params_str}"

    print(f"::{name}{params_str}::{value}")


def warning(message: str, **params: str) -> None:
    send_command("warning", message, **params)


def start_group(name: str) -> None:
    send_command("group", name)


def end_group() -> None:
    send_command("endgroup")


class Group:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        start_group(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_group()
