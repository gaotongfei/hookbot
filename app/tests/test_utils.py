import json
import os

from django.test import TestCase
from django.conf import settings

import app
from app import constants
from app.utils import is_default_branch


class ParseWebhookJsonData(TestCase):
    APP_DIR = os.path.dirname(app.__file__)
    github_sample_file = os.path.join(APP_DIR, 'tests', 'data', 'sample-github.json')
    with open(github_sample_file, 'r') as f:
        github_json_data = json.load(f)

    def setUp(self):
        pass

    def test_github(self):
        data = self.github_json_data
        if is_default_branch(data):
            pass
