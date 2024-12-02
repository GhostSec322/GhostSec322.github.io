---
title: C언어 개념정리
date: 2024-11-15 08:16:30
categories: [Computer Science, Programing]
tags: [C, Coding]
---

## 1. Hello World 분석

```c
#include<stdio.h>
int main(void) {
    printf("Hello World");
    return 0;
}
```

- 위 코드는 `Hello World`라는 문자열을 출력하는 C언어 소스코드입니다.

### 1-1. `#include<stdio.h>`

- `#include`는 **전처리기 지시문**으로, 프로그램이 컴파일되기 전에 처리됩니다.
- `stdio.h`는 **표준 입출력 라이브러리**로, `printf`와 `scanf` 같은 함수를 사용하기 위해 포함되어야 하는 파일입니다.
- `stdio`는 **Standard Input/Output**의 약자입니다.
- 컴파일러는 `#include<stdio.h>`를 만나면 해당 헤더 파일에 정의된 함수와 매크로를 프로그램에 삽입합니다.

```c
#include<stdio.h>
```

### 1-2. 메인 함수

- C/C++에서는 다양한 함수가 사용될 수 있으나, 프로그램은 항상 메인 함수로부터 시작합니다.
- 함수는 반환값이 없을 수도 있으나, 메인 함수에서는 일반적으로 `0`을 반환하는 것이 관례입니다.

```c
int main(void) {
    return 0;
}
```

### 1-3. 출력 함수 [`printf`]

- C언어는 사용자에게 특정한 문자열을 출력하기 위해 `printf`를 사용합니다.
- `printf`는 `stdio.h` 헤더 파일에 포함되어 있습니다.

```c
printf("Hello World");
```

---

## 2. 변수와 상수

- **변수(Variable)**: 변할 수 있는 데이터입니다.
- **상수(Constant)**: 변하지 않는 데이터입니다.

### 2-1. 변수의 선언

- 변수를 선언할 때 자료형과 변수명을 입력합니다.
- 원하는 경우 초기값을 적용할 수 있습니다.

```c
int a;
int a = 7;
```

### 2-2. 기본 출력

- `stdio.h` 헤더 파일에 선언된 `printf`를 이용하여 정수 데이터를 출력할 수 있습니다.

```c
#include <stdio.h>
int main(void) {
    int a = 7;
    printf("The number is %d.", a);
    return 0;
}
```

### 2-3. 기본적인 자료형

| 자료형      | 설명                                              |
| ----------- | ------------------------------------------------- |
| `int`       | 일반적인 정수형을 표현할 때 사용합니다. (억 단위) |
| `long long` | 긴 정수형을 표현할 때 사용합니다.                 |
| `double`    | 일반적인 실수형을 표현할 때 사용합니다.           |
| `string`    | 문자열을 표현할 때 사용합니다.                    |
| `bool`      | 참/거짓을 표현할 때 사용합니다.                   |
| `char`      | 한 문자를 표현할 때 사용합니다.                   |

### 2-4. 예약어와 식별자

- **식별자**란 변수, 함수 등 고유한 이름을 지정할 때 사용합니다.
- C언어 문법에 의해 정해진 **예약어**는 식별자로 사용할 수 없습니다.

---

## 3. `scanf`

- C언어에서는 사용자로부터 데이터를 입력받을 때 `scanf` 함수를 사용합니다.

```c
#include <stdio.h>
int main(void) {
    int a;
    scanf("%d", &a);
    printf("입력한 숫자는 %d입니다.
", a);
    return 0;
}
```

### 3-1. 형식 지정자

| 데이터 타입 | 크기      | 형식 지정자            | 입력 형식 예시         | 출력 형식 예시         |
| ----------- | --------- | ---------------------- | ---------------------- | ---------------------- |
| `long long` | 8 Bytes   | `%lld`                 | `scanf("%lld", &var);` | `printf("%lld", var);` |
| `int`       | 4 Bytes   | `%d`                   | `scanf("%d", &var);`   | `printf("%d", var);`   |
| `double`    | 8 Bytes   | 입력: `%lf` 출력: `%f` | `scanf("%lf", &var);`  | `printf("%f", var);`   |
| `float`     | 4 Bytes   | `%f`                   | `scanf("%f", &var);`   | `printf("%f", var);`   |
| `string`    | 제한 없음 | `%s`                   | `scanf("%s", var);`    | `printf("%s", var);`   |
| `char`      | 1 Byte    | `%c`                   | `scanf(" %c", &var);`  | `printf("%c", var);`   |

- `%` 자체를 문자로 출력하고 싶은 경우, `%%`를 사용하여 출력할 수 있습니다.

```c
#include <stdio.h>

int main() {
    // % 문자를 출력하기 위해 %%를 사용
    printf("This is how you print a percentage sign: %%
");
    return 0;
}
```
