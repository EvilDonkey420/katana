from unit import BaseUnit
from collections import Counter
import sys
from io import StringIO
import argparse
from pwn import *
import subprocess
import os
import units.stego

class Unit(units.stego.StegoUnit):

	@classmethod
	def prepare_parser(cls, config, parser):
		pass

	def evaluate(self, target):

		p = subprocess.Popen(['steghide', 'extract', '-sf', target, '-p', '', '-f'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
		output = bytes.decode(p.stdout.read(),'ascii')
		error = bytes.decode(p.stderr.read(),'ascii')
		result = {
			"stdout": output,
			"stderr": error,
		}
		
		return result
