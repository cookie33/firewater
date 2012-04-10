#!/usr/bin/env python
#
#   firewater.py    WJ111
#
#   firewater by Walter de Jong <walter@heiho.net> (c) 2012
#
#   firewater COMES WITH NO WARRANTY. firewater IS FREE SOFTWARE.
#   firewater is distributed under terms described in the GNU General Public
#   License.

import distutils.sysconfig

from distutils.core import setup

import firewater.globals

setup(
	name = 'firewater',
	version = firewater.globals.VERSION,
	
	description = 'firewater hostbased firewall configuration tool',
	long_description = 'firewater hostbased firewall configuration tool',
	author = 'Walter de Jong',
	author_email = 'walter@heiho.net',
	url = 'http://www.heiho.net/software/',
	license = 'GPLv3',
	
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Natural Language :: English',
		'Operating System :: Unix',
		'Programming Language :: Python',
		'Topic :: System :: Networking :: Firewalls'
	],
	
	package_dir={'firewater': 'firewater'},
	packages = ['firewater'],
	
	scripts = ['scripts/firewater'],
	data_files = [
		( '/etc/firewater.d', [ 'firewater.d/anti_spoofing.rules' ]),
	],
)

# EOB

