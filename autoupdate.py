#imports
import git, time, os

def update():
    repo = git.Repo('./')
    update = repo.remotes.origin
    update.pull()
    os.system('python UI.py')
    time.sleep(2)
    window.destroy
update()
