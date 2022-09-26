#include <stdio.h>

int main(void)
{
	int a = 10;
	int b = 10;
	printf("%d : %p\n", a, &a);
	printf("%d : %p\n", b, &b);
	return 0;
}
