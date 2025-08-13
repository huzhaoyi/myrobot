from glob import glob
import os
from setuptools import find_packages, setup

package_name = 'rov_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 安装URDF文件到share/rov_description/urdf目录
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        # 安装meshes目录下的所有STL模型
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.STL')),
        # launch文件，
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='huzy',
    maintainer_email='huzy@todo.todo',
    description='ROV robot model description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
