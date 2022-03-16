DEVICE=stm32f405rgt6

EXCLUDED_SCHEMES = \
    mupq/pqclean/crypto_kem/mceliece% \
    mupq/pqclean/crypto_kem/rainbow% \
    crypto_sign/rainbow% \
    mupq/crypto_sign/falcon-1024% \
    crypto_sign/falcon-1024% \
    mupq/pqclean/crypto_sign/rainbow% \

include mk/opencm3.mk
