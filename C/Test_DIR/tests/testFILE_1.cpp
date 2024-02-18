#include <gtest/gtest.h>
#include "isPrime.h"

TEST(IsPrimeTest, CheckPrimes) {
    EXPECT_TRUE(isPrime(2));
    EXPECT_TRUE(isPrime(17));
    EXPECT_TRUE(isPrime(29));
    EXPECT_TRUE(isPrime(7919));
}

TEST(IsPrimeTest, CheckNonPrimes) {
    EXPECT_FALSE(isPrime(1));
    EXPECT_FALSE(isPrime(4));
    EXPECT_FALSE(isPrime(15));
    EXPECT_FALSE(isPrime(100));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

