CC = gcc
CFLAGS = -Wall -Werror -fdiagnostics-color=always

SOURCES = $(wildcard *.c)
OBJECTS = $(SOURCES:.c:.o)
TARGETS = motion_estimation

all: $(TARGETS)

motion_estimation: $(OBJECTS)

clean:
	rm -f $(TARGETS) $(OBJECTS) vgcore*
