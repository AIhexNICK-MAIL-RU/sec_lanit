#!/usr/bin/env python3
"""
AppSec Lab - Hello World Application.
"""
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="User's last name"),
    formal: bool = typer.Option(False, "--formal", "-f", help="Use formal greeting"),
):
    """
    Greet the user with a personalized message.
    (Style: camelCase variables, different comment style)
    """
    userLastname = lastname
    isFormal = formal
    
    if isFormal == True:
        greeting = f"Добрый день, {name} {userLastname}!"
    else:
        greeting = f"Привет, {name}!"
    
    print(greeting)

if __name__ == "__main__":
    typer.run(main)
