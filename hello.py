#!/usr/bin/env python3
"""
Hello AppSec World Application

This module demonstrates a modern CLI application using Typer
for the AppSec laboratory work.
"""
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    
    Args:
        name: Имя пользователя (обязательный аргумент)
        lastname: Фамилия пользователя (опциональный)
        formal: Флаг формального приветствия
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    # Запуск Typer CLI приложения
    typer.run(main)
