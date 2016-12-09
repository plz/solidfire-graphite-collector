# solidfire-graphite-collector

Daemon to collect performance metrics from a SolidFire cluster and send 
them to Graphite.


Current Release
---------------

Version 1.0.2


Description
-----------

The SolidFire Graphite collector is a simple utility to collect metrics 
from Element OS 8.x and store them in graphite.   The dashboards directory
contains a set of sample Grafana dashboards utilizing the collected metrics.


Required Libraries
------------------

| Component                                                        | Version   |
|------------------------------------------------------------------|-----------|
| solidfire-sdk-python <https://github.com/solidfire/solidfire-sdk-python/> | 1.1   |
| Requests <http://docs.python-requests.org/en/master/>            | 2.12.1+   |
| graphyte <https://github.com/Jetsetter/graphyte/>                | 1.1       |
| python-daemon<https://pypi.python.org/pypi/python-daemon/>       | 2.1.2     |



Usage
-----

The script is called from the command line using the parameters shown below.  
You can run multiple instances of the script in parallel if you have more than one 
cluster to monitor.


    usage: python solidfire_graphite_collector.py [-h] [-s SOLIDFIRE] [-u USERNAME]
                                           [-p PASSWORD] [-g GRAPHITE] [-t PORT]
                                           [-m METRICROOT]

      -h, --help            show this help message and exit

      -s SOLIDFIRE, --solidfire SOLIDFIRE
                        hostname of SolidFire array from which metrics should
                        be collected

      -u USERNAME, --username USERNAME
                        username for SolidFire array.  default admin

      -p PASSWORD, --password PASSWORD   
                        password for SolidFire array.  default password

      -g GRAPHITE, --graphite GRAPHITE
                        hostname of Graphite server to send to.  default localhost

      -t PORT, --port PORT  port to send message to.  default 2003



To have it automatically startup on server boot, make use of an rc.d script (or upstart) 
as appropriate for your OS version.   

To stop this script, simply kill the process.  A sample command to do so is shown below:

    ps -ef | grep solidfire_graphite_collector.py | grep -v grep | awk {'print $2'} \
    | xargs kill




**License**
-----------

Copyright © 2016 NetApp, Inc. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
