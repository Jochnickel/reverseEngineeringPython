import Builtin_Function_Or_Method
import Method_Wrapper

class Object:
	__base__ = None # this is correct
	__class__ = object
	__setattr__ = Method_Wrapper()
	__delattr__ = Method_Wrapper()
	__eq__ = Method_Wrapper()
	__gt__ = Method_Wrapper()
	__lt__ = Method_Wrapper()
	__dir__ = Builtin_Function_Or_Method() 
	__subclasshook__ = Builtin_Function_Or_Method()
	__format__ = Builtin_Function_Or_Method()
	__str__ = Method_Wrapper()