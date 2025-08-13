import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/huzy/rov_moveit2_ws/src/rov_description/install/rov_description'
