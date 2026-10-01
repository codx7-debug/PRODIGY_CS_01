# Caesar Cipher

A simple Python program that encrypts and decrypts text using the Caesar Cipher algorithm.

## Task

Implement a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm.

## Features

- Encrypt text using a shift value.
- Decrypt encrypted text using the same shift value.
- User can choose between encryption and decryption.
- Uses modular arithmetic (`% 26`) to handle alphabet wrapping.

## How It Works

The Caesar Cipher shifts each letter by a specified number of positions.

For example, with a shift of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
