CFLAGS = -std=c99
LFLAGS = 

TARGET = hoppity
OBJS = hoppity.o 

TARGET: $(OBJS)
	gcc  $^  -o $(TARGET)  $(CFLAGS) $(LFLAGS)
	
%.o: %.c
	gcc -c $< $(CFLAGS) $(LFLAGS) 
	
clean:
	rm $(OBJS) $(TARGET)

