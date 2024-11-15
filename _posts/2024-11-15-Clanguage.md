---
title: C언어 개념정리
date: 2025-11-15 20:16:30 +09:00
categories: [Computer Science, Programing]
tags: [C, Coding]
---

# 1. printf scanf

```c
int  printf (  const  char* format , var1,var2,... ) ;
```

- 위 코드는 C언어 printf함수이다.
- printf는 데이터, 문자열 등을 출력하는 함수 입니다.
- const char\* format 이 영역에는 출력할 데이터를 정의하는 영역입니다. 아래는 Hello GhostSec 이라는 문자열을 출력하는 예제 코드 입니다.

```c
#include<stdio.h>
int main(void){
    printf("Hello GhostSec\n");
    return 0;
}
```

- 이 방법외에 다른 방법으로 작성을 해 보겠습니다.

```c
#include<stdio.h>
int main(void){
    char name[]= "GhostSec";
    printf("Hello %s\n",name);
    return 0;
}
```

이렇게 하면 위 코드와 같은 결과값을 나타냅니다. 이 둘의 차이점은 변수를 사용한 것과 변수를 사용하지 않았다는 차이점이 있습니다.

- name에 "GhostSec"이라는 문자열을 대입하게 됩니다. 이때 사용되는 것이 바로 변수 라는 것 입니다.
- 이때 서식문자와 두번째 파라미터에 출력할 변수명을 지정하면 됩니다.

# C언어 데이터 타입 및 포맷 지정자

| 포맷 지정자 | 데이터 타입                                  | 설명                          |
| ----------- | -------------------------------------------- | ----------------------------- |
| `%c`        | 문자(char)                                   | 문자 출력                     |
| `%s`        | 문자열(char[])                               | 문자열 출력                   |
| `%f`        | 실수(float)                                  | 소수점 포함 실수 출력         |
| `%lf`       | 실수(double)                                 | 소수점 포함 실수 출력         |
| `%u`        | 부호 없는 10진 정수(unsigned int)            | 양의 정수 출력                |
| `%d`        | 부호 있는 10진 정수(int)                     | 정수 출력                     |
| `%o`        | 부호 없는 8진 정수(unsigned int)             | 8진수 출력                    |
| `%x`        | 부호 없는 16진 정수(unsigned int)            | 16진수 출력                   |
| `%lu`       | 부호 없는 long 정수(unsigned long)           | 부호 없는 long 정수 출력      |
| `%ld`       | 부호 있는 long 정수(long)                    | 부호 있는 long 정수 출력      |
| `%llu`      | 부호 없는 long long 정수(unsigned long long) | 부호 없는 long long 정수 출력 |
| `%lld`      | 부호 있는 long long 정수(long long)          | 부호 있는 long long 정수 출력 |

# C언어 특수 문자 이스케이프 시퀀스

| 이스케이프 시퀀스 | 의미                     | 설명                     |
| ----------------- | ------------------------ | ------------------------ |
| `\'`              | 작은따옴표               | 작은따옴표를 출력합니다. |
| `\"`              | 큰따옴표                 | 큰따옴표를 출력합니다.   |
| `\?`              | 물음표                   | 물음표를 출력합니다.     |
| `\\`              | 백 슬래시(\\)            | 백 슬래시를 출력합니다.  |
| `\n`              | 줄 바꿈, 개행 (new line) | 새 줄로 이동합니다.      |
| `\t`              | 수평 탭 (tab)            | 수평 탭을 추가합니다.    |
