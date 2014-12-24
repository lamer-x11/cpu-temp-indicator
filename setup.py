from setuptools import setup, find_packages

setup(name='cpu-temp-indicator',
      version='0.1',
      description='Displays an indicator of the cpu\'s temperature.',
      author='Lamer',
      author_email='lamer@l-x11.com',
      url='https://github.com/lamer-x11/cpu-temp-indicator',
      packages=find_packages(),
      install_requires=['setuptools'],
      package_data={'src': ['icons/*.png']},
      entry_points={'console_scripts': ['cpu-temp-indicator = src:main']})
