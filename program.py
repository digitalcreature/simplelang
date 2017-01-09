from state import State
import instructions

import re


class Program():

	_instr_pattern = re.compile(r'([A-Z]+)(\s+([^;#]+))?')

	def __init__(self):
		self.instructions = []
	@classmethod
	def fromfile(cls, fname):
		with open(fname) as src:
			program = cls()
			for line in src:
				m = cls._instr_pattern.match(line.strip())
				if (m):
					program.instructions.append(m.group(1, 3))
			return program
	def run(self, state=None):
		state = state or State()
		for instr in self.instructions:
			ifunc = getattr(instructions, instr[0])
			if (ifunc):
				ifunc(state, instr[1])
