import click
import pandas as pd


@click.command()
@click.option(
    "--file-path",
    required=True,
    type=click.Path(exists=True),
    help="Path to the Ames housing dataset file (.parquet)."
)
def inspect_ames_data(file_path: str) -> None:
    df = pd.read_parquet(file_path)

    print(df.head())


if __name__ == "__main__":
    inspect_ames_data()
