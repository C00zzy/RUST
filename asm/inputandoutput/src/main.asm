section .data
    prompt1 db 'Enter first number:  ', 0
    prompt2 db 'Enter first number:  ', 0
    prompt3 db 'Enter operator:  ', 0
    result_msg db 'Result: ', 0
    error_msg 'Error: Invalid', 0

section .bss
    number1 resb 10
    number2 resb 10
    operation resb 1
    result resb 10

section .text
    global _start
_start:
    mov eax, 1
    xor ebx, ebx
    int 0x80
