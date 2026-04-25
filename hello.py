#!/usr/bin/env python3
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    ИЗМЕНЕННЫЙ КОММЕНТАРИЙ В MASTER ВЕТКЕ ДЛЯ КОНФЛИКТА!
    Этот комментарий отличается от того, что в patch2.
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
