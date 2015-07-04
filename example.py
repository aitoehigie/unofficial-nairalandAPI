import click
import api

@click.command()
@click.option("--name", prompt="Username")
@click.option("--password", prompt="password")
def nairaland_login(name, password):
    user = api.NairalandUser(name, password)
    print user

if __name__ == "__main__":
    nairaland_login()
