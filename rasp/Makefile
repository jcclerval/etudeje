##############################################
#Definitions
##############################################

VERSION = DEBUG
PRODUCT =
PREFIX =

CC = $(PREFIX)g++
LD = $(PREFIX)ld
AR = $(PREFIX)ar
RANLIB = $(PREFIX)ranlib

VPATH  = ..
INCLUDE  = -I../../skyetek-c-api-for-linux/SkyeTekAPI
LIBS = -L../../skyetek-c-api-for-linux/SkyeTekAPI/unix -lstapi
CFLAGS = -g -O0 -Wall -DDEBUG 
EXE = example
OBJS += example.o

OS = $(shell uname -s)
ifeq ($(OS),Linux)
  CFLAGS += -DLINUX
  LIBS += -lusb
endif

##############################################
#Rules
##############################################

all: build_msg $(EXE) 
	@echo; echo $(VERSION) build complete; echo

stapi:
	(cd ../../skyetek-c-api-for-linux/SkyeTekAPI/unix; $(MAKE) -j8)

$(EXE): $(OBJS) stapi
	$(CC) -o ../../example $(OBJS) $(LIBS)
	@echo

%.a: %.o
	$(RANLIB) $@
	@echo

%.o: %.c
	$(CC) -c $(INCLUDE) $(CFLAGS) $<
	@echo

clean:
	rm -f *.o *.elf *.lst *.s *.i *.a $(EXE)

realclean: clean
	rm -f $(EXE)
	(cd ../../skyetek-c-api-for-linux/SkyeTekAPI/unix; $(MAKE) clean)

build_msg:
	@echo; echo $(VERSION); echo
