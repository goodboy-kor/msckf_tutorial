# click.py로 파일명을 설정하면 라이브러리 이름과 같아서 attruibute error가 생김
import click #cli(command line interface)도구를 만들 수 있게 도와주는 라이브러리

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