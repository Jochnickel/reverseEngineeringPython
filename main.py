import json
import builtins


import os

os.system("ls -a")


def readFile(filename):
    try:
        with open(filename, 'r') as fnm:
            return fnm.read()
    except:
        return None


def completeDocs(docs_dict: dict, objClass):
	if objClass.__class__ == type and type(objClass.__doc__) == str:
		print(objClass)
		docs_dict[objClass.__name__] = objClass.__doc__
	else:
		print("NOO",objClass, objClass.__doc__.__class__)


docs = json.loads(readFile("docs.json") or "{}")


def asd()-> bool:
    print("asd")


dict1 = {}
tuple1 = (1,2)
int1 = (1)
bool1 = False
noneType1 = (None)
type1 = (type)
list1 = []
float1 = 1.2
str1 = "a"
bytes1 = bytes(1)
complex1 = 1j
range1 = range(1)
set1 = set({})
frozenset1 = frozenset({})
bytearray1 = bytearray(1)
function1 = lambda: 1
code1 = function1.__code__

memoryview1 = memoryview(bytes1)
wrapper_descriptor1 = type1.__init__
method_wrapper1 = dict1.__iter__
dict_keyiterator1 = dict1.__iter__()

print("lol",object.__class__.__base__)


with open("docs.json", 'w') as fd:
    fd.write(json.dumps(docs))
