#include "counter.hpp"

int Counter::operator()() 
{ 
    return ++count; 
}
