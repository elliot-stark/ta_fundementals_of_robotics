from setuptools import find_packages, setup

package_name = 'lab1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/pub.launch.py']),
        ('share/' + package_name, ['launch/pubsub.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='estark',
    maintainer_email='estark@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'lab1_publisher = lab1.publisher:main',
            'lab1_2_pubsub = lab1.lab1_2_pubsub:main',
        ],
    },
)
