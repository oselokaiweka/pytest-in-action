#!/usr/bin/env python
import click

from mylib.mkchange import change


@click.command()
@click.option(
    "--amount",
    prompt="Amount",
    help = "This is my change calculation"
)
def make_change(amount):
    "Gives correct change in cents"

    result = change(float(amount))
    click.echo(click.style(f"Change for ${amount}: ", fg="red"))
    for correct_change in result:
        for num,coin in correct_change.items():
            click.echo(click.style(f" {num} {coin}", fg="green"))

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    make_change()