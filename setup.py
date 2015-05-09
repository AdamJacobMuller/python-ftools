from distutils.core import setup, Extension

setup(name='ftools',
    version='0.2',
    author='David Stainton',
    author_email='dstainton415@gmail.com',
    ext_modules=[
          Extension('ftools', ['ftools.c']),
      ],
      scripts=['scripts/python_fincore','scripts/python_fadvise','scripts/pages_by_time','scripts/report_filechanges']
)

