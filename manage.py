import server
from pospax import manager


@manager.command
def runserver():
    server.run_server()


if __name__ == '__main__':
    manager.run()
