from grako.walkers import NodeWalker
from parser import SimpleLangParser
from model import SimpleLangModelBuilderSemantics

class SimpleLangWalker(NodeWalker):
	def __init__(self):
		self.refs = {}
	def deref(self, value):
		if (type(value) is str):
			return self.refs[str]
		else:
			return value
	def walk_object(self, node):
		return node
	def walk_Number(self, node):
		print (node.value)
		return float(node.value)
	def walk_Identifier(self, node):
		return node
	def walk_Add(self, node):
		return self.deref(node.left) + self.deref(node.right)
	def walk_Sub(self, node):
		return self.deref(node.left) - self.deref(node.right)
	def walk_Multply(self, node):
		return self.deref(node.left) * self.deref(node.right)
	def walk_Divide(self, node):
		return self.deref(node.left) / self.deref(node.right)
	def walk_Assign(self, node):
		self.refs[node.left] = node.right
		return node.right
	def walk_Expression(self, node):
		print(self.deref(node))
		return node

if __name__ == "__main__":
	from sys import argv
	src = open(argv[1]).read()
	parser = SimpleLangParser(semantics = SimpleLangModelBuilderSemantics())
	model = parser.parse(src)
	SimpleLangWalker().walk(model)
