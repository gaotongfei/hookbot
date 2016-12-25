import envoy
from celery.decorators import task


@task(bind=True)
def pull_from_remote(branch):
    res = envoy.run('git pull origin {branch}'.format(branch=branch))
    assert res == 0

@task(bind=True)
def run_test():
    pass
