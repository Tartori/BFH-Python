CXX=clang++
CXXFLAGS=-Wall --std=c++11 -O3

OBJ=counter.o counter_perf.o

counter_perf: $(OBJ)
	$(CXX) -o $@ $^
  
$(OBJ): %.o: %.cpp
	$(CXX) -c $(CXXFLAGS) -o $@ $< 


.phony: clean
clean:
	rm -f $(OBJ) counter_perf
