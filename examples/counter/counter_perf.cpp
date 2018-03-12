#include <chrono>
#include <iostream>

#include "counter.hpp"

int main(void)
{
    Counter counter;
    constexpr auto repetitions = 10000000;

    std::cout << "invoking counter " << repetitions << " times.\n";
    auto startTime = std::chrono::steady_clock::now();
    for (auto i = 0; i < repetitions; ++i)
    {
        counter();
    }
    auto endTime = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsedSeconds = endTime - startTime;

    std::cout << "counter value: " << counter.getCount() << std::endl;
    std::cout << "counter overhead: "
              << (elapsedSeconds.count() / repetitions * 1e9)
              << " ns/call (avg)\n";
    return 0;
}