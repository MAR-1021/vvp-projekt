from setuptools import setup, find_packages

setup(
    name='simulaceplanet',
    version='1.0.0',
    author='Šimon Marek',
    description='Simulace pohybu planet ve 2D prostoru',
    packages=find_packages(),
    install_requires=['numpy','matplotlib',],
    extras_require={'dev': ['pytest', 'sphinx']} 
)
