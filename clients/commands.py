import click

@click.group()
def clients():
    """Manage de clients lifecycle."""
    pass

@click.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """ Create a new Client. """
    pass

@click.command()
@click.pass_context
def list(ctx):
    """ List all Clients. """
    pass

@click.command()
@click.pass_context
def update(ctx, client_uid):
    """ Update a Client. """
    pass

@click.command()
@click.pass_context
def delete(ctx, client_uid):
    """ Delete a Client. """
    pass


all = clients
