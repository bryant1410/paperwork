#!/usr/bin/env python

from distutils.core import setup

setup(name="DtGrep",
      version="0.1",
      description="Grep for dead trees",
      author="Jerome Flesch",
      author_email="jflesch@gmail.com",
      packages=['dtgrep'],
      package_dir={ 'dtgrep': 'src' },
      data_files=[('share/dtgrep', [
          'src/aboutdialog.glade',
          'src/mainwindow.glade',
          'src/searchwindow.glade',
          'src/settingswindow.glade',
      ])],
      scripts=['scripts/dtgrep'],
     )
