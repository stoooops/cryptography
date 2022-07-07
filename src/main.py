#!/usr/bin/env python3
import binascii
import hashlib

import whirlpool
from Crypto.Hash import keccak


def hash(text: str = "hello") -> None:

    data: bytes = text.encode("utf8")
    print(f"{text} -> {data}")

    ripemd160: bytes = hashlib.new("ripemd160", data).digest()
    print(f"RIPEMD-160: {binascii.hexlify(ripemd160)}")

    sha224hash: bytes = hashlib.sha224(data).digest()
    print(f"SHA-224:    {binascii.hexlify(sha224hash)}")

    sha3_224: bytes = hashlib.sha3_224(data).digest()
    print(f"SHA3-224:   {binascii.hexlify(sha3_224)}")

    sha256hash: bytes = hashlib.sha256(data).digest()
    print(f"SHA-256:    {binascii.hexlify(sha256hash)}")

    sha3_256: bytes = hashlib.sha3_256(data).digest()
    print(f"SHA3-256:   {binascii.hexlify(sha3_256)}")

    blake2s: bytes = hashlib.new("blake2s", data).digest()
    print(f"BLAKE2s:    {binascii.hexlify(blake2s)}")

    keccak256: bytes = keccak.new(data=data, digest_bits=256).digest()
    print(f"Keccak-256: {binascii.hexlify(keccak256)}")

    sha3_384: bytes = hashlib.sha3_384(data).digest()
    print(f"SHA3-256:   {binascii.hexlify(sha3_384)}")

    keccak384: bytes = keccak.new(data=data, digest_bits=384).digest()
    print(f"Keccak-384: {binascii.hexlify(keccak384)}")

    whirlpool_digest: bytes = whirlpool.new(data).digest()
    print(f"Whirlpool:  {binascii.hexlify(whirlpool_digest)}")


def main() -> None:
    hash()


if __name__ == "__main__":
    main()
