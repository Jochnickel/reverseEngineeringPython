import Wrapper_Descriptor
import Object

class Type:
	__init__ = Wrapper_Descriptor()
	def __init__(self, object_or_name: str, bases: tuple, dict: dict):
		# TypeError: type() takes 1 or 3 arguments
		pass
		# TypeError: type.__new__() argument 1 must be str, not int
		# TypeError: type.__new__() argument 2 must be tuple, not int
		# TypeError: type.__new__() argument 3 must be dict, not int
		# TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
		# TypeError: descriptor '__init__' requires a 'type' object but received a 'dict'
	__call__ = Wrapper_Descriptor()
	__base__ = Object

# type() is different from type.__init__()
# Wrapper_Descriptor