#ifndef PQCLEAN_SNTRUP953_AVX2_CRYPTO_CORE_MULT3SNTRUP953_H
#define PQCLEAN_SNTRUP953_AVX2_CRYPTO_CORE_MULT3SNTRUP953_H

#include <stdint.h>
#define PQCLEAN_SNTRUP953_AVX2_crypto_core_mult3sntrup953_OUTPUTBYTES 953
#define PQCLEAN_SNTRUP953_AVX2_crypto_core_mult3sntrup953_INPUTBYTES 953
#define PQCLEAN_SNTRUP953_AVX2_crypto_core_mult3sntrup953_KEYBYTES 953
#define PQCLEAN_SNTRUP953_AVX2_crypto_core_mult3sntrup953_CONSTBYTES 0

int PQCLEAN_SNTRUP953_AVX2_crypto_core_mult3sntrup953(unsigned char *outbytes, const unsigned char *inbytes, const unsigned char *kbytes);
#endif
