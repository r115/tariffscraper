import click
from tariffscraper.banks.kcb.kcb_parser import KcbTariffParser

@click.command()
@click.argument('year', nargs=1)
@click.argument('bank', nargs=1)
def run(year, bank):
    allowed_years = ["2023"]

    if allowed_years.count(year) == 0:
        click.echo("Year not allowed")
        exit()

    click.echo("We are going to scrape some data.")

    commander = None

    match bank:
        case "kcb":
            commander = KcbTariffParser(year)

    if commander is not None:
        commander.parse()


if __name__ == '__main__':
    run()
