# test_sfp_reversewhois.py
import pytest
import unittest

from modules.sfp_reversewhois import sfp_reversewhois
from sflib import SpiderFoot
from spiderfoot import SpiderFootEvent, SpiderFootTarget


@pytest.mark.usefixtures
class TestModulereversewhois(unittest.TestCase):
    """
    Test modules.sfp_reversewhois
    """

    def test_opts(self):
        module = sfp_reversewhois()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        """
        Test setup(self, sfc, userOpts=dict())
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_reversewhois()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_reversewhois()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_reversewhois()
        self.assertIsInstance(module.producedEvents(), list)

    @unittest.skip("todo")
    def test_handleEvent(self):
        """
        Test handleEvent(self, event)
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_reversewhois()
        module.setup(sf, dict())

        target_value = 'spiderfoot.net'
        target_type = 'DOMAIN_NAME'
        target = SpiderFootTarget(target_value, target_type)
        module.setTarget(target)

        event_type = 'ROOT'
        event_data = 'example data'
        event_module = ''
        source_event = ''
        evt = SpiderFootEvent(event_type, event_data, event_module, source_event)

        result = module.handleEvent(evt)

        self.assertIsNone(result)
