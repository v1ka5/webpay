from django import test
from django.conf import settings
from django.core.urlresolvers import reverse

import json

import mock
from nose.tools import eq_

from pyquery import PyQuery as pq

TEST_JS_SETTINGS = {'foo': 'bar'}

class TestJsSettingsOutput(test.TestCase):

    def setUp(self):
        super(TestJsSettingsOutput, self).setUp()
        self.client = test.Client()

    @mock.patch.object(settings, 'TEST_PIN_UI', True)
    @mock.patch.object(settings, 'JS_SETTINGS', TEST_JS_SETTINGS)
    def test_js_error_settings_output(self):
        url = reverse('pay.lobby')
        res = self.client.get(url)
        eq_(res.status_code, 200)
        doc = pq(res.content)
        js_settings = json.loads(doc('body').attr('data-settings'))
        eq_(js_settings, TEST_JS_SETTINGS)
