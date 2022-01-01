# ----------------
# Python
# ----------------
import os
import sys
import time
import json
import shutil
import logging
import ast
import re
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from jinja2 import Environment, FileSystemLoader
from general_functionalities import ParseLearnFunction

# ----------------
# Get logger for script
# ----------------

log = logging.getLogger(__name__)

# ----------------
# Template Directory
# ----------------

template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_sh_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect()

# ----------------
# Test Case #1 - Make Mind Map
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed:
            if device.type != 'switch':
                self.learned_routing = ParseLearnFunction.parse_learn(steps, device, "routing")

            # ---------------------------------------
            # Create JSON, YAML, CSV, MD, HTML, HTML Mind Map files from the Parsed Data
            # ---------------------------------------         
            
            with steps.start('Store data',continue_=True) as step:

                ## create per device informational MindMap
                formatted_device_map_template = env.get_template('formattedDeviceMap.j2')

                if self.learned_routing is None:
                    self.learned_routing = 'No Routes'
                
                parsed_output_type = formatted_device_map_template.render(
                    inventory_hostname=device.alias,
                    device_os=device.os,
                    to_parse_routing = self.learned_routing['vrf']
                    )

                with open(f"MindMap.md", "w") as fh:
                    fh.write(parsed_output_type)               
                    fh.close()                

        with steps.start('Disconnect from devices',continue_=True) as step:
            testbed.disconnect()