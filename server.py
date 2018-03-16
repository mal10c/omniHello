import sys
from omniORB import CORBA, PortableServer
import CosNaming, Comm, Comm__POA

# Define an implementation of the Echo interface
class Echo_i (Comm__POA.Echo):
	def echoString(self, msg):
		print "echoString() called with message: ", msg
		return msg

# Initialize the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of Echo_i and an Echo object reference
ei = Echo_i()
eo = ei._this()

print "IOR of servant:"
print orb.object_to_string(eo)
print ""

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
	print "Failed to narrow the root naming context"
	sys.exit(1)

# Bind a context named "test.my_context" to the root context
name = [CosNaming.NameComponent("test", "my_context")]
try:
	testContext = rootContext.bind_new_context(name)
	print "New test context bound"

except CosNaming.NamingContext.AlreadyBound, ex:
	print "Test context already exists"
	obj = rootContext.resolve(name)
	testContext = obj._narrow(CosNaming.NamingContext)
	if testContext is None:
		print "test.my_context exists but is not a NamingContext"
		sys.exit(1)

# Bind the Echo object to the test context
name = [CosNaming.NameComponent("ExampleEcho", "Object")]
try:
	testContext.bind(name, eo)
	print "New ExampleEcho object bound"

except CosNaming.NamingContext.AlreadyBound:
	testContext.rebind(name, eo)
	print "ExampleEcho binding already existed -- rebound"

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block forever (or until ORB is shut down)
orb.run()
