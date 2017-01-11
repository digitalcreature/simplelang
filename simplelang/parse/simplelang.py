from grako.walkers import NodeWalker
from parser import SimpleLangParser
from model import SimpleLangModelBuilderSemantics

class SimpleLangWalker(NodeWalker):
	def __init__(self):
		self.refs = {}
	def deref(self, value):
		if (type(value) is str):
			return self.refs[value]
		else:
			return value
	def walk_object(self, node):
		for expr in node:
			print(self.deref(self.walk(expr)))
	def walk_Number(self, node):
		return float(node.value)
	def walk_Identifier(self, node):
		return node.id
	def walk_Add(self, node):
		return self.deref(self.walk(node.left)) + self.deref(self.walk(node.right))
	def walk_Subtract(self, node):
		return self.deref(self.walk(node.left)) - self.deref(self.walk(node.right))
	def walk_Multiply(self, node):
		return self.deref(self.walk(node.left)) * self.deref(self.walk(node.right))
	def walk_Divide(self, node):
		return self.deref(self.walk(node.left)) / self.deref(self.walk(node.right))
	def walk_Assign(self, node):
		right = self.walk(node.right)
		self.refs[self.walk(node.left)] = self.deref(right)
		return right

if __name__ == "__main__":
	from sys import argv
	src = open(argv[1]).read()
	parser = SimpleLangParser(semantics = SimpleLangModelBuilderSemantics())
	model = parser.parse(src)
	SimpleLangWalker().walk(model)
