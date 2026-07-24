# 🔐 Caesar Cipher in Python

A simple **Python implementation of the Caesar Cipher**, one of the oldest and most well-known encryption techniques. This project allows users to encrypt and decrypt messages using a custom shift key through a command-line interface.

---

# 📖 What is the Caesar Cipher?

The **Caesar Cipher** is a classical substitution cipher named after the Roman general **Julius Caesar**, who reportedly used it to send secret military messages.

It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

### Example

If the shift key is **3**:

| Plain Text | Encrypted Text |
|------------|----------------|
| A | D |
| B | E |
| C | F |
| X | A |
| Y | B |
| Z | C |

For example:

**Plain Text**
```text
hello
```

**Shift Key**
```text
3
```

**Cipher Text**
```text
khoor
```

During decryption, the same shift is applied in the opposite direction to recover the original message.

---

# 🚀 Features

- 🔒 Encrypt messages using the Caesar Cipher.
- 🔓 Decrypt encrypted messages.
- 🔑 User-defined shift key.
- 🔁 Perform multiple encrypt/decrypt operations without restarting the program.
- 🌍 Preserves spaces, numbers, and special characters.
- ♻️ Uses modulo arithmetic to handle large shift values efficiently.

---

# 🛠️ Technologies Used

- Python 3

---

# 📂 Project Structure

```text
Caesar-Cipher/
│
├── main.py
└── README.md
```

---

# ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Caesar-Cipher.git
```

### 2. Navigate to the Project Folder

```bash
cd Caesar-Cipher
```

### 3. Run the Program

```bash
python main.py
```

---

# 💻 Sample Output

```text
Type 'encrypt' for encryption, type 'decrypt' for decryption:
encrypt

Type your message:
hello world

Enter the shift key:
5

text after encryption : mjqqt btwqi

Do you want to continue? (yes/no)
yes

Type 'encrypt' for encryption, type 'decrypt' for decryption:
decrypt

Type your message:
mjqqt btwqi

Enter the shift key:
5

text after decryption : hello world
```

---

# 🧮 Algorithm

## Encryption

Each letter is shifted forward by the specified key.

```python
new_position = (current_position + shift_key) % 26
```

## Decryption

Each letter is shifted backward by the specified key.

```python
new_position = (current_position - shift_key) % 26
```

The modulo (`% 26`) operation ensures that letters wrap around the alphabet.

---

# ⏱️ Time Complexity

| Operation | Complexity |
|----------|------------|
| Encryption | O(n) |
| Decryption | O(n) |

Where **n** is the length of the input string.

---

# 📚 Concepts Used

- Python Functions
- Loops
- Lists
- Strings
- Conditional Statements
- Modulo Arithmetic
- User Input
- Indexing

---

# ⚠️ Limitations

- Supports only lowercase English letters (`a-z`).
- Uppercase letters are not encrypted.
- Not suitable for modern secure communication.
- Can be broken easily using brute-force or frequency analysis.

---

# 🔒 Why Learn the Caesar Cipher?

Although the Caesar Cipher is no longer considered secure, it is an excellent introduction to cryptography. It helps understand important concepts such as:

- Encryption
- Decryption
- Secret Keys
- Substitution Ciphers
- Modular Arithmetic

These concepts are the foundation of modern encryption algorithms used in cybersecurity.

---

# 🚀 Future Improvements

- ✅ Support uppercase letters.
- ✅ Encrypt entire files.
- ✅ Add brute-force attack mode.
- ✅ Build a GUI using Tkinter.
- ✅ Support custom alphabets.
- ✅ Improve input validation.

---

## ⭐ If you found this project useful, don't forget to give it a Star!