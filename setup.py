from distutils.core import setup

setup(name='ipyviz',
      version='1.0',
      description='Visualisation package for IPython Notebooks',
      author='Martin Zellner',
      author_email='martin.zellner@gmail.com',
      packages=['ipyplots',],
      requires=['numpy',
                'seaborn',
                'matplotlib',
                'networkx',
                'IPython',
                ])
