class State:
	def __init__(self):
		self.stack = []
		self.vars = {}
	def deref(self, value):
		if (type(value) is str):
			return self.vars[value]
		else:
			return value
	def push(self, value):
		self.stack.append(value)
	def pop(self):
		return self.stack.pop()
	def peek(self):
		return self.stack[len(self.stack) - 1]
	def gettop(self):
		return len(self.stack)
	def settop(self, top):
		del self.stack[top:]
	def clear(self):
		del self.stack[:]
	def popderef(self):
		return self.deref(self.pop())
	def setvar(self, var, val):
		if (type(var) is str):
			self.vars[var] = val
		else:
			raise ReferenceException("Attempt assignment to non-reference value '{}'.".format(var))

class ReferenceException(Exception):
	pass
