CC            = /usr/bin/g++
CPPFLAGS      = -g -c
LDFLAGS       = -g
OMNI_HOME 	  = /usr/local
OMNI_INCLUDES = -I$(OMNI_HOME)/include
OMNI_LIB_DIR  = $(OMNI_HOME)/lib
OMNIIDL       = $(OMNI_HOME)/bin/omniidl
INCLUDES      = $(OMNI_INCLUDES)
LIBS          = -lomniORB4 -lomnithread -lomniDynamic4
SERVER_OBJECTS       = echoSK.o server.o
CLIENT_OBJECTS       = echoSK.o client.o

all: client server

server: $(SERVER_OBJECTS)
	$(CC) $(LDFLAGS) -o server $(SERVER_OBJECTS) $(LIBS)

server.o: server.cpp
	$(CC) $(CPPFLAGS) $(INCLUDES) $(LIBS) server.cpp

client: $(CLIENT_OBJECTS)
	$(CC) $(LDFLAGS) -o client $(CLIENT_OBJECTS) $(LIBS)

client.o: client.cpp
	$(CC) $(CPPFLAGS) $(INCLUDES) $(LIBS) client.cpp

echoSK.o: echoSK.cc
	$(CC) $(CPPFLAGS) $(INCLUDES) $(LIBS) echoSK.cc

echoSK.cc: echo.idl
	$(OMNIIDL) -bcxx echo.idl

clean:
	rm -rf *.o
	rm -rf *.hh
	rm -rf *SK.cc
	rm -rf server
	rm -rf client