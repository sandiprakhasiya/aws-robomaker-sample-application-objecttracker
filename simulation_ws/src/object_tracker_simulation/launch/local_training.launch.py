# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import sys

import launch
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))  # noqa
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'launch'))  # noqa


#############################
##  Local Training Worker  ##
#############################

def generate_launch_description():

    ###########################
    ##  Create World Launch  ##
    ###########################
    object_tracker_simulation_dir = get_package_share_directory('object_tracker_simulation')
    object_tracker_simulation_launch = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            os.path.join(object_tracker_simulation_dir, 'launch', 'create_world.launch.py')))

    ###################################
    ##  Reinforcement Learning Node  ##
    ###################################
    rl_agent = launch_ros.actions.Node(
        package='object_tracker_simulation', node_executable='run_local_rl_agent.sh', output='screen',
        node_name='rl_agent', name='training')

    ########################
    ##  Launch Evalution  ##
    ########################
    ld = launch.LaunchDescription([object_tracker_simulation_launch, rl_agent])
    return ld


if __name__ == '__main__':
    generate_launch_description()
