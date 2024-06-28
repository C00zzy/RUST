section .data
    prompt_msg db 'Enter an character', 0x0A
    input_buffer resb 1
section .text
    global _start

_start:
    mov eax, 4
    mov ebx, 1
    mov ecx, prompt_msg
    mov edx, 17
    int 0x80

    mov eax, 3
    mov ebx, 0
    mov ecx, input_buffer
    mov edx, 1
    int 0x80
    mov eax, 4
    mov ebx, 1
    mov ecx, input_buffer
    mov edx, 1
    int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80