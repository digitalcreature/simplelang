def PUSHFLOAT(state, value):
	state.push(float(value))
def PUSHREF(state, ident):
	state.push(str(ident))
def POP(state, count):
	count = count or 1
	state.settop(state.gettop() - count)
def CLEAR(state, arg):
	state.clear()
def ASSIGN(state, arg):
	val = state.popderef()
	var = state.pop()
	state.setvar(var, val)
	state.push(val)
def __ARITH(state, op):
	right = state.popderef()
	left = state.popderef()
	state.push(op(left, right))
def ADD(state, arg):
	__ARITH(state, lambda l, r: l + r)
def SUB(state, arg):
	__ARITH(state, lambda l, r: l - r)
def MULT(state, arg):
	__ARITH(state, lambda l, r: l * r)
def DIV(state, arg):
	__ARITH(state, lambda l, r: l / r)
def PRINT(state, arg):
	print(state.peek())
