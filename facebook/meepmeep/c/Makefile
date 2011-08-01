CFLAGS =  
LFLAGS = 

TARGET = meepmeep
OBJS = meepmeep.o 

TARGET: $(OBJS)
	gcc  $^  -o $(TARGET)  $(CFLAGS) $(LFLAGS)
	
%.o: %.c
	gcc -c $< $(CFLAGS) $(LFLAGS) 
	
clean:
	rm $(OBJS) $(TARGET)

