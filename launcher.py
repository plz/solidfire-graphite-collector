#!/usr/bin/python
# launcher.py
#
# Version 1.0.1
# Author: Colin Bieberstein
#
# Copyright &copy; 2016 NetApp, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import time
import os
import configparser
import subprocess 

config = configparser.ConfigParser()
config.read("./sgc.config")

# Each section is a solidfire array to monitor
for arr in config.sections():
    # username and password are mandatory fields
    if not (config.has_option(arr,'username') and 
            config.has_option(arr,'password')):
        print("Error: config section ", arr, 
                "missing required elements. Skipping.\n")
        continue

    argstring = "-s " + arr
    argstring = argstring + " -u " + config.get(arr,'username')
    argstring = argstring + " -p " + config.get(arr,'password')

    if config.has_option(arr,'graphite'):
        argstring = argstring + " -g " + config.get(arr,'graphite')

    if config.has_option(arr,'port'):
        argstring = argstring + " -t " + config.get(arr,'port')

    if config.has_option(arr,'metricroot'):
        argstring = argstring + " -m " + config.get(arr,'metricroot')

    subprocess.run(["python", "solidfire_graphite_collector.py", argstring]) 

