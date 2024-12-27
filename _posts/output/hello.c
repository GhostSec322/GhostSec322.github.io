#include <stdio.h>

int swapfun(int *a, int *b) {
    int c = *a;  // `a`가 가리키는 값을 저장
    printf("c is ...%d\n", c);

    *a = *b;  // `a`가 가리키는 값을 `b`가 가리키는 값으로 변경
    printf("a is ...%d\n", *a);

    *b = c;  // `b`가 가리키는 값을 `c`로 변경
    printf("b is ...%d\n", *b);

    return 0;
}

int main(void) {
    int a1 = 0;
    int b2 = 3;

    swapfun(&a1, &b2);  // 주소를 전달하여 값 교환
    printf("%d %d\n", a1, b2);  // 결과 출력

    return 0;
}
