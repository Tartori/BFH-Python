#ifndef COUNTER_HPP
#define COUNTER_HPP

class Counter
{
    int count;
  public:
    Counter() : count(0) {}
    // counting operation implemented as application operator ()
    // the counter thus is a function object (a functor)
    int operator()();
    int getCount() const { return count; }
};

#endif // COUNTER_HPP
