import sys
import os
from cx_Freeze import setup, Executable

files = ['assets/']
settings = Executable(
    script='app.py',
    icon='extras\\icone.ico',
)

setup(
    name='Automating exclusion of spams',
    version='1.0',
    description='This program automates exclusion of spams on Poczta email accounts.',
    author='Jonatas Lopes de Sousa',
    options= {'build_exe': {
        'include_files': files,
        'include_msvcr': True
    }},
    executables=[settings]
    )

""" import sys
import os
from cx_Freeze import setup, Executable

files = ['assets/user_data.txt']
settings = Executable(
    script='app.py',
    icon='extras/icone.ico'
)

setup(
    name='Automating exclusion of spams',
    version='1.0',
    description='This program automates exclusion of spams on Poczta email accounts.',
    author='Jonatas Lopes de Sousa',
    options= {'build_exe': {
        'include_files': files,
        'include_msvcr': True


    }},
    executables=[settings]
    ) """