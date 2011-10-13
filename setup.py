
from distutils.core import setup

if __name__ == '__main__':
    setup(name='Area53',
          version='0.91',
          description='Python Interface to Route53',
          author='Marius Voila',
          author_email='myself@mariusv.com',
          url='https://github.com/mariusv/area53',
          package_dir = {'': '..'},
          packages = ['area53', 'area53.route53'],
          requires=['boto (>=2.0)']
    )
