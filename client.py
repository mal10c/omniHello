import sys
from omniORB import CORBA
import CosNaming, Comm

# Initialize the ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
	print "Failed to narrow the root naming context"
	sys.exit(1)

# Resolve the name "test.my_context/ExampleEcho.Object"
name = [CosNaming.NameComponent("test", "my_context"),
		CosNaming.NameComponent("ExampleEcho", "Object")]
try:
	obj = rootContext.resolve(name)

except CosNaming.NamingContext.NotFound, ex:
	print "Name not found"
	sys.exit(1)

# Narrow the object to a Comm::Echo
eo = obj._narrow(Comm.Echo)

if eo is None:
	print "Object reference is not a Comm::Echo"
	sys.exit(1)

print "Discovered the IOR:"
print orb.object_to_string(eo)
print ""

# Invoke the echoString operation
message = "Hello from Python"
result = eo.echoString(message)

print "I said '%s'.  The object said '%s'." % (message, result)
