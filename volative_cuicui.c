#include <stdio.h>
/*asm ( assembler template */
        /*: output operands                  [> optional <]*/
        /*: input operands                   [> optional <]*/
        /*: list of clobbered registers      [> optional <]*/


// gcc -masm=intel cuicui.c
int binconv(int num) {

    if (num == 0) {
        return 0;
    }

    return (num % 2) + 10 * binconv(num / 2);
}

int funcname(int arg1)
{
    int res = 0;


    __asm__ (
            "bswap  %%eax\n\t"
            "mov    %%eax, %%edx\n\t"
            "and    $0xf0f0f0f0, %%eax\n\t"
            "and    $0xf0f0f0f0, %%edx\n\t"
            "shr    $0x4, %%edx\n\t"
            "shl    $0x4, %%eax\n\t"
            "or     %%edx, %%eax\n\t"
            "mov    %%eax, %%edx\n\t"
            "and    $0x33333333, %%eax\n\t"
            "and    $0xcccccccc, %%edx\n\t"
            "shr    $0x2, %%edx\n\t"
            "shl    $0x2, %%eax\n\t"
            "or     %%edx, %%eax\n\t"
            "mov    %%eax, %%edx\n\t"
            "and    $0x55555555, %%eax\n\t"
            "and    $0xaaaaaaaa, %%edx\n\t"
            "add    %%eax, %%eax\n\t"
            "shr    $1, %%edx\n\t"
            "or     %%edx, %%eax\n\t"
            : "=a" (res)
            : "a"  (arg1)
    );

    return res;
}

int main(int argc, const char *argv[])
{
    int ex1 = 5;
    printf("%d -> %d\n", ex1, binconv(ex1));
    printf("%d -> %d\n", funcname(ex1), binconv(funcname(ex1)));

    return 0;
}
