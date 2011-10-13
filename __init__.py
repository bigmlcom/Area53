
import boto
from area53.route53 import *

try:
    route53 = boto.connect_route53()
except:
    pass

connect_route53 = boto.connect_route53

del boto
