#!/usr/bin/env python

from mp import version
from distutils.core import setup

setup(name='ardupy-mpfshell',
      version=version.FULL,
      description='The lightweight version of the mpfshell is for pure CUI drivers.',
      author='Stefan Wendler & Juwan &Hongtai.Liu',
      author_email='junhuanchen@qq.com',
      url='https://github.com/Lynn/mpfshell-lite',
      install_requires=['pyserial', 'websocket_client'],
      packages=['mp'],
      scripts=['ardupy-mpfshell'],
      keywords=['ArduPy', 'micropython', 'shell', 'file transfer', 'development'],
      classifiers=[],
      entry_points={"console_scripts": ["mpfs=mp.mpfshell:main"]},
)
