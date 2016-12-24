from app import constants


def is_default_branch(data):
    pushed_branch = data['ref'].split('/')[-1]
    master_branch = data['repository']['master_branch']
    return pushed_branch == master_branch
