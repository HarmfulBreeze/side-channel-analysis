#include "crypto_verify_1847.h"


int PQCLEAN_SNTRUP1277_CLEAN_crypto_verify_1847(const unsigned char *x, const unsigned char *y) {
    unsigned int differentbits = 0;
    int i;

    for (i = 0; i < PQCLEAN_SNTRUP1277_CLEAN_crypto_verify_1847_BYTES; ++i) {
        differentbits |= x[i] ^ y[i];
    }

    return (int) (1 & ((differentbits - 1) >> 8)) - 1;
}
