import os
import warnings

#from distutils.core import setup
from setuptools import setup


with open(os.path.join('fpdf', '__init__.py')) as init_:
    for line in init_:
        if '__version__' in line:
            version = line.split('=')[-1].strip().replace('"','')
            break
    else:
        version = 'unknown'
        warnings.warn('Unable to find version, using "%s"' % version)
        input("Continue?")

    
setup(name='py3fpdf',
      version=version,
      description='Simple PDF generation for Python',
      author='Olivier PLATHEY/Max Pat',
      author_email='maxpat78@yahoo.it',
      maintainer = "Joel Rivera",
      maintainer_email = "rivera@joel.mx",
      url="https://bitbucket.org/cyraxjoe/py3fpdf",
      packages=['fpdf', ],
      package_data={'fpdf': ['font/*.ttf', 'font/*.txt']},
      classifiers = ['Development Status :: 2 - Pre-Alpha'
                     "Intended Audience :: Developers",
                     "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
                     "Programming Language :: Python",
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.0'
                     "Programming Language :: Python :: 3.1",
                     "Programming Language :: Python :: 3.2",
                     "Operating System :: OS Independent",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                     "Topic :: Multimedia :: Graphics"],
      keywords="pdf unicode png jpg")

