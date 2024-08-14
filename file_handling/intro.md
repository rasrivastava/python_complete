`seek`: Moves the file pointer to a specific byte position.
`read`: Reads a specified number of bytes from the current file pointer position.
`tell`: Returns the current position of the file pointer.

`seek(offset, whence)`

- The seek method is used to move the file pointer (or cursor) to a specific position within a file.

- Parameters:
  - `offset`: The number of bytes to move the file pointer. It can be a positive or negative integer:
    - `Positive`: Moves the pointer forward in the file.
    - `Negative`: Moves the pointer backward in the file.
  - `whence`: Specifies the reference point for the offset. It can take one of three values:
    - `0`: Start of the file (default). The offset is measured from the beginning of the file.
    - `1`: Current position of the file pointer. The offset is added to the current position.
    - `2`: End of the file. The offset is measured from the end of the file. Typically, the offset is negative when using this value.

- `file.seek(10)`: **Moves the pointer to the 10th byte from the beginning.**
- `file.seek(-5, 1)`: **Moves the pointer 5 bytes back from wherever it currently is.**
- `file.seek(-10, 2)`: **Moves the pointer to 10 bytes before the end of the file.**

