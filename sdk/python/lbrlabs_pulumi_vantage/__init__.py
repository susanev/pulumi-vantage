# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .aws_provider import *
from .get_aws_provider_info import *
from .provider import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import lbrlabs_pulumi_vantage.config as __config
    config = __config
else:
    config = _utilities.lazy_import('lbrlabs_pulumi_vantage.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "vantage",
  "mod": "index/awsProvider",
  "fqn": "lbrlabs_pulumi_vantage",
  "classes": {
   "vantage:index/awsProvider:AwsProvider": "AwsProvider"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "vantage",
  "token": "pulumi:providers:vantage",
  "fqn": "lbrlabs_pulumi_vantage",
  "class": "Provider"
 }
]
"""
)
