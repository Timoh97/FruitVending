from app import create_app, db
from flask_script import Manager, Server
from app.models import *
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')
manager=Manager(app)
manager.add_command('db',MigrateCommand)
migrate = Migrate(app,db)

manager.add_command('server',Server)
#this flask-script shell allows debugging is below
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)
#flask-script is above
if __name__ == '__main__':
    manager.run()