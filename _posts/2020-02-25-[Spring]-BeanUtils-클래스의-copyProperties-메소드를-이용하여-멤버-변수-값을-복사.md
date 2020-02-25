---
published: true
title: "[Spring] BeanUtils 클래스의 copyProperties 메소드를 이용하여 멤버 변수 값을 복사"
categories:
  - Spring
date: 2020-02-25T10:22:00.000Z
tags:
  - Spring
  - Spring Boot
---

## 1. 개요
 * Spring으로 개발 중 Entity의 멤버 변수 값을 Dto로 복사하고 싶을때가 있습니다.
 * BeanUtils 클래스의 copyProperties 메소드를 이용하여 멤버 변수 값을 복사하는 방법을 소개합니다.
 
## 2. copyProperties 메소드 설명

``` JAVA
 /**
  * Copy the property values of the given source bean into the target bean.
  * <p>Note: The source and target classes do not have to match or even be derived
  * from each other, as long as the properties match. Any bean properties that the
  * source bean exposes but the target bean does not will silently be ignored.
  * <p>This is just a convenience method. For more complex transfer needs,
  * consider using a full BeanWrapper.
  * @param source the source bean
  * @param target the target bean
  * @throws BeansException if the copying failed
  * @see BeanWrapper
  */
 public static void copyProperties(Object source, Object target) throws BeansException {
 	copyProperties(source, target, null, (String[]) null);
 }
```

 * 첫번째 인자인 source 클래스에는 Getter가 있어야 합니다.
 * 두번째 인자인 target 클래스에는 Setter가 있어야 합니다.

## 2. 예제 코드

``` JAVA
package kr.webgori.lolien.discord.bot.unit;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

import org.junit.Test;
import org.springframework.beans.BeanUtils;

public class BeanUtilsUnitTest {
  @Test
  public void test01_Should_EqualsMemberVariables_When_UseBeanUtilsCopyPropertiesMethodTest() {
    SourceClass sourceClass = new SourceClass(1, "sourceName", 20);

    TargetClass targetClass = new TargetClass();

    BeanUtils.copyProperties(sourceClass, targetClass);

    assertThat(sourceClass.idx, is(targetClass.idx));
    assertThat(sourceClass.name, is(targetClass.name));
    assertThat(sourceClass.age, is(targetClass.age));
  }

  static class SourceClass {
    private int idx;
    private String name;
    private int age;

    SourceClass(int idx, String name, int age) {
      this.idx = idx;
      this.name = name;
      this.age = age;
    }

    public int getIdx() {
      return idx;
    }

    public String getName() {
      return name;
    }

    public int getAge() {
      return age;
    }
  }

  private static class TargetClass {
    private int idx;
    private String name;
    private int age;

    public void setIdx(int idx) {
      this.idx = idx;
    }

    public void setName(String name) {
      this.name = name;
    }

    public void setAge(int age) {
      this.age = age;
    }
  }
}
```
 
## 3. 테스트 결과

{% include lightbox.html src="[Spring] BeanUtils 클래스의 copyProperties 메소드를 이용하여 멤버 변수 값을 복사/testResult.png" data="group" %}

