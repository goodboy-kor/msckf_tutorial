import click # cli(Command Line Interface) 도구를 만들게 해주는 라이브러리

# @는 데코레이터, 예약어를 만들어서 나중에 실행 할 수 있게 함
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()