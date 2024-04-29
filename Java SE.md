# Java SE 基础知识

## 一、Java虚拟机（JVM）

![JVM](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292239671.png)

## 二、Java的加载与执行原理

![加载与执行原理](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292239825.png)

## 三、JDK、JRE、JVM分别是什么？他们的关系是什么？

1. **JDK（Java Development Kit）：**   
   JDK 是 Java 开发工具包，它是 Java 开发者用来开发 Java 应用程序的核心组件。JDK 包括了 Java 编译器（javac）、Java 运行时环境（JRE）、Java 文档生成器（Javadoc）以及其他一些开发工具和库。简而言之，JDK 提供了开发 Java 应用程序所需的所有工具和资源。

2. **JRE（Java Runtime Environment）：**    
   JRE 是 Java 运行时环境，它是在运行 Java 应用程序时所必需的环境。JRE 包含了 Java 虚拟机（JVM）以及 Java 核心类库和支持文件。当用户想要运行一个已编译的 Java 应用程序时，他们需要安装 JRE。JRE 提供了 Java 应用程序的运行环境，但不包含开发工具。

3. **JVM（Java Virtual Machine）：**   
   JVM 是 Java 虚拟机，它是 Java 程序的运行环境。JVM 负责在实际的硬件平台上执行 Java 字节码（即编译后的 Java 代码）。JVM 负责加载字节码、解释执行或即时编译字节码为本地机器代码，并管理内存、执行垃圾回收等任务。JVM 的存在使得 Java 能够实现“一次编写，到处运行”的特性。

   ![JVM](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292239468.png)

## 四、class和public class的区别    

1. 一个 Java 源文件可以定义多个 class。
2. 编译之后，一个 class 就会对应生成一个 class 字节码文件。
3. 如果一个类是 public，类名必须要和源文件名保持一致。
4. public 类可以没有，如果有的话也只能有一个。
5. 每个类中都可以编写入口 main 方法。在实际开发中，入口一般只有一个。

```java
class A{
    public static void main(String[] args) {
        System.out.println("A执行了");
    }
}
class B{
    public static void main(String[] args) {
        System.out.println("B执行了");
    }
}
public class X{
    public static void main(String[] args) {
        System.out.println("X执行了，这个 Java 源文件名为 X.java");
    }
}
```

## 五、Java标识符命名规范

遵循驼峰式命名方法。   

- **类名、接口名：** 首字母大写吗，后面每个单词首字母大写。 `StudentService`    
- **变量名、方法名：** 首字母小写，后面每个单词首字母大写。 `productPrice`    
- **常量名：** 全部大写，每个单词之间采用"_"分隔。 `LOGIN_SUCCESS`    
- **包名：** 全部小写。 `com.camellia.javase.extends`    

## 六、Java中的加号运算符

```java
public class PlusTest{
    public static void main(String[] args) {
        int a=10;
        int b=20;
        String str="10";
        // 字符串拼接
        System.out.println(str + b); // 1020;
        
        str="30";
        // 当一个表达式中出现多个+，若没有（），遵循从左到右。
        System.out.println(a + b + str); // 3030;
        
        // 添加了（）优先级比较高。
        System.out.println(a+(b+str)); // 102030
        
    }
}
```

## 七、变量的分类 

- **局部变量（Local Variables）：**   
  在方法、代码块或构造方法中声明的变量称为局部变量。局部变量只在其声明的范围内可见，超出该范围就无法访问。局部变量的生命周期仅在其声明的代码块、方法或构造方法执行期间。当代码块或方法执行完毕时，局部变量将被销毁。    

- **成员变量（Instance Variables）：**    
  在类中声明的变量，但在方法之外，类的任何地方都可以访问，称为成员变量或实例变量。每个对象都有一份成员变量的副本，它们属于对象的状态。成员变量的生命周期与对象的生命周期相同。它们随着对象的创建而创建，随着对象的销毁而销毁。    

- **静态变量（Static Variables）：**   
  使用 static 关键字声明的成员变量称为静态变量。静态变量属于类而不是对象，在类加载时初始化，并且所有对象共享同一份静态变量。静态变量的生命周期与类的生命周期相同。它们在类加载时初始化，随着类的卸载而销毁。    

```java
/*
 变量可以根据定义/声明的位置来进行分类，可以分为两大类：
        1、局部变量
        2、成员变量
          - 静态变量
         

 - 实例变量
 */
public class VarClassify {
    public static void main(String[] args) {
        // 凡是在方法体中定义的变量，一定是局部变量。
        // 局部变量只在当前方法体中有效。
        int a=100;
    }

    // 在类中定义的变量叫做成员变量。
    // 实例变量
    int b=200;
    // 静态变量
    static int c=300;
}
```

**总结：**
Java 是一种混合型语言，既有编译阶段也有解释阶段。









# 变量类型

## 一、整型变量

byte < short < int < long < float < double

> 在 Java 中任何一个整数型字面量都会被默认被当做 int 类型来处理。

```java
public class IntTest {
    public static void main(String[] args) {
        // 100 是 4 个字节，b 是八个字节。
        // 所以存在自动类型类型转换。
        long b=100;
        // 这个不存在类型转换。
        long c=100L;
        // 这个会报错，原因是 = 右边先执行，这个整型字面量会以 int 类型处理，显然超过了 int 范围所以报错。其错误的原因在这。
        long e=2147483648;
    }
}
```

### 1.1、自动类型转换

可以理解为从小容量到大容量。程序员不需要明确地指定转换操作，而是由编程语言的规则自动执行。

### 1.2、 强制类型转换

大容量转换为小容量，可能会有精度损失。Java 编程语言不会自动转换，由程序员自己强制转换。

```java
// 经典的例子
class Test{
    public static void main(String[] args) {
        int k=128;
        byte e=(byte)k; //-128
        int m=129;
        byte n=(byte)m; -127
    }
}
```

---

* 注意：
  * 当一个整数型字面量没有超过对应变量类型范围时，可以直接赋值给对应变量类型的变量。
  * byte 和 short 混合运算的时候，先各自转换为 int 再做运算。(byte+byte-->int、 byte+short-->int、 short+short-->int)
  * 当一个整数型字面量没有超过对应变量类型范围时，可以直接赋值给对应变量类型的变量。
  * 注意强转时前后都要加（），因为优先级不同。

```java
public class ByteTest {
    public static void main(String[] args) {
        byte b=1;
        byte a=127;
        // 按道理这个由 int 转换为 byte 没有强转的话因该报错。
        // 其实这是 Java 语言开发者给程序员的优化措施。
        // 规则：当一个整数型字面量没有超过对应变量类型范围时，可以直接赋值给对应变量类型的变量。
        
        short m=10;
        byte n=3;
        // 编译器报错，最后结果是 int 类型，不能用 short 变量接收。（注意和字面量的区别）
        short result=m+n;

        byte c=10/3;
        // 10/3 都是字面量，所以会在编译器就计算出来。即在源码 ByteTest.java 中是 byte c=10/3,但是在编译后 ByteTest.class 中 byte c=3;


        byte x=10;
        byte y=3;
        byte d=x/y;
        // 编译器报错,在编译阶段只能知道 x/y 结果为 int，只有在正式运行才知道 x,y 里面存的是什么。
    }
}
```

## 二、浮点型变量

* float：单精度，可以精确到 7 位小数。    
* double：双精度，可以精确到 15 位小数。   
* 浮点型的字面量默认当做 double 类型处理，要用 float 类型处理需要在字面量后面加 F/f。
* 浮点型数据有两种表示形式：十进制、科学计数法。

```java
// 不存在类型转换
float f=3.14F;
// 借助强制类型转换
float f=(float)3.14;
```

### 2.1、浮点型数据存储原理

浮点型数据存储原理涉及到计算机中的浮点数表示方法。通常情况下，浮点数由两部分组成：尾数（mantissa）和指数（exponent），以及一个符号位（sign bit），用来表示正负。

常见的浮点数表示方法是 IEEE 754 标准，它定义了单精度浮点数（32 位）和双精度浮点数（64 位）的存储格式。
在 IEEE 754 标准中，单精度浮点数的存储结构如下：
- 符号位：1 位
- 指数位：8 位
- 尾数位：23 位

双精度浮点数的存储结构如下：
- 符号位：1 位
- 指数位：11 位
- 尾数位：52 位

浮点数的实际值通过指数和尾数来表示。指数用来表示浮点数的数量级，尾数用来表示浮点数的精度。符号位用来表示浮点数的正负。

浮点数的存储原理基于科学计数法，即一个数可以表示为尾数乘以基数的指数次方。例如，对于单精度浮点数，可以表示为：
$$
(-1)^{\text{sign}} \times (1 + \text{mantissa}) \times 2^{\text{exponent} - \text{bias}}
$$

其中，sign 是符号位，mantissa 是尾数，exponent 是指数，bias 是偏置值（用于使指数可以表示负数）。这个公式基本上适用于双精度浮点数，只是指数偏置和尾数位数不同。

## 三、字符型

### 3.1、char

Java 中的 char 类型使用 Unicode 编码来表示字符。每个字符对应一个

唯一的 Unicode 码点，可以通过 \u 后跟 4 位十六进制数来表示。

### 3.2、转义字符

* \n： 换行符（newline），在输出时表示换行。    
* \t： 制表符（tab），在输出时表示水平制表。    
* \r： 回车符（carriage return），在输出时表示回车。    
* '： 单引号（single quote），用于表示单引号字符。    
* "： 双引号（double quote），用于表示双引号字符。    
* \： 反斜杠（backslash），用于表示反斜杠字符本身。    

### 3.3、乱码

乱码通常是由于文本数据的编码方式与解码方式不匹配或者编码过程中出现了错误所致。    
所以一定要保持编码与解码一致。

### 3.4、char 参与运算

byte、short、char 混合运算的时候，先各自转换为 int 再做运算。    
多种数据类型混合运算的时候放，先各自转换为最大的再做运算。   

## 四、boolean 类型

在 Java 中，boolean 的值只有 true、false。（与 C、C++ 有所不同）

**总结：基本数据类型转换规则**   

> 1、八种基本数据类型除了 boolean 类型之外，都可以互相转换。    
> 2、小容量可以自动转换为大容量，容量排序为：byte < short,char < int < long < float < double     
> 3、大容量不能自动转换为小容量，必须添加强制类型转换符，才能编译通过，但是运行时可能损失精度。    
> 4、当整数型字面量没有超过 byte、short、char 的范围时，可以将其赋值给 byte、short、char 类型的变量。      
> 5、byte、short、char 混合运算时，各自先转换为 int 再做运算。    
> 6、多种数据类型混合运算的时候放，先各自转换为最大的再做运算。    

**注意：**
>1、long e=2147483648; 这个属于一个经典面试题，其错误的原因是 = 右边先执行，这个整型字面量会以 int 类型处理，显然超过了 int 范围所以报错。    
>2、理解 byte a=10/3; 不报错，但是 byte b=10; byte c=3; a=b/3; 报错。







# 字节码解读

## 一、基础概念

1. Windows cmd 查看程序字节码指令：`javap -c`
2. 局部变量表、操作数栈、槽位
    - 在 Java 语言中，任何一个方法执行时，都会专门为这个方法分配所属的内存空间，供这个方法的使用。
    - 每个方法都有自己独立的内存空间，这个内存空间有两块比较重要的内存空间：**局部变量表、操作数栈**
    - 此外，**局部变量表中还管理着槽位**，在 Java 虚拟机的线程栈中，局部变量、操作数栈和返回值等数据存储在称为“**槽位**”的内存单元中。
    - 每个槽位通常可以容纳一个基本类型值或者是一个引用。
3. `bipush`、`istore`、`iload`、`iinc`
    - `bipush` 是 Java 虚拟机（JVM）中的一个字节码指令，用于将一个字节（byte）常量推送到操作数栈顶。
    - `istore` 是 Java 虚拟机（JVM）中的一个字节码指令，用于将整数类型的值从操作数栈顶存储到局部变量表中的指定位置。
    - `iload` 是 Java 虚拟机（JVM）中的一个字节码指令，用于将整数类型的值从局部变量表中加载到操作数栈顶。
    - `iinc` 是 Java 虚拟机（JVM）中的一个字节码指令，用于对局部变量表中的整数值进行增量操作。

## 二、引例

### 2.1、局部变量表、操作数栈、槽位、字节码解读（详细）

- **源码：**

```java
public class ReadClass {
    public static void main(String[] args) {
        int i=10;
        int j=i;
        j++;
    }
}
```

- **字节码：**

```java
Compiled from "ReadClass.java"
public class ReadClass {
    public ReadClass();
    Code:
            0: aload_0
            1: invokespecial #1                  // Method java/lang/Object."<init>":()V
            4: return

    public static void main(java.lang.String[]);
    Code:
            0: bipush        10
            2: istore_1
            3: iload_1
            4: istore_2
            5: iinc          2, 1
            8: return
}
```

<img height="300" src="https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292257734.png" width="600"/>

- **解读：**   
    - `bipush 10`: 将 10 这个字面量压入操作数栈中。    
    - `istore_1`: 将操作数栈顶元素弹出，然后将其存储到局部变量表的一号槽位上。    
    - `iload_1`: 将局部变量表 1 号槽位上的数据复制一份，压入操作数栈。    
    - `istore_2`: 将操作数栈顶元素弹出，然后将其存储到局部变量表的二号槽位上。   
    - `iinc 2, 1`: 将局部变量表的 2 号槽位上的数加一。   

    <img height="300" src="https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292257738.png" width="600"/>

### 2.2、i++、++i 字节码角度剖析

- **i++ 源码：**

```java
public class ReadClass1 {
    public static void main(String[] args) {
        int i=10;
        int j=i++;  //先引用 i 的值，后执行自增操作。
    }
}
```

- **i++ 字节码：**

```java
Compiled from "ReadClass1.java"
public class ReadClass1 {
    public ReadClass1();
    Code:
            0: aload_0
            1: invokespecial #1                  // Method java/lang/Object."<init>":()V
            4: return

    public static void main(java.lang.String[]);
    Code:
            0: bipush        10     // 向操作数栈压入 10。
            2: istore_1             // 将操作数栈顶元素弹出，然后将其存储到局部变量表的 1 号槽位上。
            3: iload_1              // 将局部变量表 1 号槽位上的数据复制一份，压入操作数栈。压入的是                                                                                           10。
            4: iinc          1, 1   // 将局部变量表的 1 号槽位上的数加一。  
            7: istore_2             // 将操作数栈顶元素弹出，然后将其存储到局部变量表的 2 号槽位上。
            8: return
```

- **++i 源码：**

```java
public class ReadClass2 {
    public static void main(String[] args) {
        int i=10;
        int j=++i;   // 先执行自增操作，后引用 i 的值。
    }
}
```

- **++i 字节码：**

```java
Compiled from "ReadClass2.java"
public class ReadClass2 {
    public ReadClass2();
    Code:
            0: aload_0
            1: invokespecial #1                  // Method java/lang/Object."<init>":()V
            4: return

    public static void main(java.lang.String[]);
    Code:
            0: bipush        10      // 向操作数栈压入 10。
            2: istore_1              // 将操作数栈顶元素弹出，然后将其存储到局部变量表的 1 号槽位上。
            3: iinc          1, 1    // 将局部变量表的 1 号槽位上的数加一。 此时一号槽位上的数是 11。
            6: iload_1               // 将局部变量表 1 号槽位上的数据复制一份，压入操作数栈。压入的                                                                                          11。                     
            7: istore_2              // 将操作数栈顶元素弹出，然后将其存储到局部变量表的 2 号槽位上。
            8: return
```







# Switch 语句

## 一、case 语句可以合并

case 后面只能是字面量值这样的值，不能使用变量。    

```java
import java.util.Scanner;

public class SwitchTest01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer month = sc.nextInt();
        String str;
        switch(month) {
            case 3: case 4: case 5:
                str="春天";
                break;
            case 6 : case 7: case 8:
                str="夏天";
                break;
            case 9: case 10: case 11:
                str="秋天";
                break;
            case 12: case 1: case 2:
                str="冬天";
                break;
            default: str="请输入正确月份";
        }
        System.out.println(str);
    }
}
```

## 二、Java12 中 switch 的新特性

增强的 switch 语句是 Java 12 中引入的一项语言特性，它在 Java 14 中得到了进一步改进。这个特性的目的是提供更简洁、灵活和易读的 switch 语法。   

传统的 switch 语句在处理多个条件分支时可能存在一些问题，例如需要使用 break 语句显式地结束每个分支，容易出现忘记添加 break 而导致多个分支执行的情况。

增强的 switch 语句解决了这些问题，并引入了一些新的语法特性。     

**增强的 switch 语句的特点如下：**
- 使用表达式作为分支条件：增强的 switch 语句允许在每个 case 分支中使用表达式，而不仅限于常量。这使得代码更加灵活，可以更方便地处理各种条件。
- 无需显式 break：在传统的 switch 语句中，每个 case 分支必须以 break 语句结束，否则会继续执行下一个分支。而增强的 switch 语句不需要显式地使用 break，每个分支会自动结束，不会继续执行下一个分支。
- 使用箭头(->)：在增强的 switch 语句中，分支的语法使用箭头(->)来连接分支的条件和执行语句，这使得代码更加简洁和易读。
- 引入 yield 关键字：在 Java 14 中，增强的 switch 语句引入了 yield 关键字，用于在分支中返回值。这使得 switch 语句可以像表达式一样返回值，增强了其功能性。

```java
public class EnhancedSwitchExample {
    public static void main(String[] args) {
        int day = 3;
        String dayType = switch (day) {
            case 1, 2, 3, 4, 5 -> "Weekday"; // 使用表达式作为分支条件
            case 6, 7 -> "Weekend";
            default -> { // default 分支
                yield "Invalid day"; // 使用 yield 返回值
            }
        };
        System.out.println("Day type: " + dayType);
    }
}
```

```java
class Switch01{
    public static void main(String[] args) {
        switch(expression){
            case 1-> System.out.println("switch");
            case 2 -> System.out.println("Change in");
            case 3 -> System.out.println("Java12");
            default -> System.out.println("default");
        }
    }
}
```

```java
class Switch02{
    public static void main(String[] args) {
        switch (expression){
            case 1,2,3 -> System.out.println("123");
            default -> System.out.println("default");
        }
    }
}
```

```java
class Switch03{
    public static void main(String[] args) {
        switch (expression){
            case 1 ->{
                System.out.println("Java");
                System.out.println("Wow!");
            }
        }
    }
}
```











# Method (方法)

## 一、静态方法什么时候需要用类名调用？
调用者和被调用者在同一个类中时，可以省略。    

```java
// 调用方法是，类名. 什么情况下可以省略。
public class MethodTest01 {
    public static void main(String[] args) {
        //调用method1
        method1();
        MethodTest01.method1();
        //调用method2
        /*method2(); 编译器报错*/
        MethodTest.method2();
    }
    public static void method1(){
        System.out.println("mothod1执行了！");
    }
}

class  MethodTest{
    public static void method2(){
        System.out.println("method2执行了！");
    }
}
```

## 二、方法语法的小细节

```java
public class MethodTest05 {

    // 缺少返回语句
    public static int m1() {
        int i = 100;
        if (i > 99) {
            return 1; //虽然这里有返回语句，但是有几率不执行if语句。所以编译器不通过。
        }
    }
}
```

## 三、方法执行的内存图
>**概念：** Java 的元空间（Metaspace）是 Java 虚拟机（JVM）用来存储类元数据的内存区域。在传统的 Java 虚拟机实现中，类元数据通常存储在永久代（Permanent Generation）中。但是，从 JDK 8 开始，永久代被移除，取而代之的是元空间。 
>
>**元空间与永久代相比有几个显著的不同点：**
>* 内存位置： 元空间不是在 Java 虚拟机的堆内存中，而是位于本地内存中。这使得元空间的大小不受堆内存的限制，可以动态地根据应用程序的需要调整大小。
>* 自动调整大小： 元空间的大小可以根据应用程序的需要动态调整，因此不容易出现类加载溢出的情况。在使用元空间时，不需要手动设置元空间的大小，JVM 会根据应用程序的需求自动调整。
>* 内存回收： 元空间的内存是由 JVM 进行管理的，不需要像永久代一样手动进行垃圾回收。当类加载器不再需要某些类的元数据时，JVM 会自动进行回收，而不会出现永久代中的内存泄漏问题。
>* 垃圾收集器： 元空间的垃圾收集与堆内存的垃圾收集不同，通常不会触发 Full GC。类加载器卸载类时，相关的元数据会被及时回收，不会等待垃圾收集器的触发。

```java
/*
1.方法如果只定义，不调用是不会分配内存空间。（从Java8开始，方法的字节码指令存储在元空间metaspace当中。元空间使用的是本地内存。）
2.方法调用的瞬间，会在JVM的栈内存当中分配活动场所，此时发生压栈动作。
3.方法一旦结束，给该方法分配的内存空间就会释放。此时发生弹栈动作。
*/
public class MethodTest02{
    public static void main(String[] args){
        System.out.println("main begin");
        m1();
        System.out.println("main over");
    }

    public static void m1(){
        System.out.println("m1 begin");
        m2();
        System.out.println("m1 over");
    }

    public static void m2(){
        System.out.println("m2 begin");
        m3();
        System.out.println("m2 over");
    }

    public static void m3(){
        System.out.println("m3 begin");
        System.out.println("m3 over");
    }
}
```

![JVM方法](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292304105.png)

## 四、方法重载

### 4.1、在 Java 中，方法重载需要满足以下条件：

1. **方法名称相同：** 重载方法的名称必须相同。
2. **参数列表不同：** 重载方法的参数列表必须不同，可以通过参数的数量、类型或者顺序来区分不同的重载方法。
3. **返回类型可以不同：** 重载方法的返回类型可以相同也可以不同。但是，仅仅通过返回类型的不同是无法实现方法重载的，因为 Java 中不允许仅通过返回类型的不同来区分不同的方法。
4. **访问修饰符、方法体、抛出的异常可以相同也可以不同：** 重载方法的访问修饰符、方法体、以及方法中可能抛出的异常可以相同也可以不同。
5. **方法重载与参数的名称无关：** 方法重载与参数的名称无关，只与参数列表的类型、数量和顺序有关。

### 4.2、方法重载示例代码

```java
/*
方法重载是编译阶段的机制还是运行阶段的机制？
	方法重载机制是编译阶段的机制。
	在编译阶段已经完成了方法的绑定。
	在编译阶段已经确定了要调用哪个方法了。

什么情况下我们考虑使用方法重载呢？
	在以后的开发中，在一个类中，如果两个方法的功能相似，建议将方法名定义为同一个名字。
	此时就使用了方法重载机制。
*/
public class MethodOverloadTest01 {
    public static void main(String[] args){
        m1();
        m1

("abc");

        m2(10, 20);
        m2(10L, 20L);

        m3("x", 10);
        m3(10, "x");
    }

    // 形参的个数不同
    public static void m1(){
        System.out.println("m1()");
    }
    public static void m1(String s){
        System.out.println("m1(String s)");
    }

    // 形参类型不同
    public static void m2(int a, int b){
        System.out.println("m2(int a, int b)");
    }
    public static void m2(long a, long b){
        System.out.println("m2(long a, long b)");
    }

    // 形参顺序不同
    public static void m3(String s, int a){
        System.out.println("m3(String s, int a)");
    }
    public static void m3(int a, String s){
        System.out.println("m3(int a, String s)");
    }

    // 以下这两个方法没有构成方法重载，属于方法重复定义了。语法错误，编译器报错。
	/*
	public static void doSome(int a, int b){
	
	}
	public static void doSome(int x, int y){
	
	}
	*/
}
```

### 4.3、println方法重载源码(部分)

```java
 /* Methods that do not terminate lines */

    /**
     * 打印布尔值。 {@link 生成的字符串
     * java.lang.String#valueOf（boolean）} 被转换为字节
     * 根据平台默认的字符编码，以及这些字节
     * 完全按照
     * {@link #write（int）} 方法。
     *
     * @param b 要打印的 {@code 布尔值}
     */
    public void print(boolean b) {
        write(String.valueOf(b));
    }

   /**
     * 打印字符。 该字符将转换为一个或多个字节
     * 根据给定给构造函数的字符编码，或
     * 平台的默认字符编码（如果未指定）。这些字节
     * 完全按照 {@link #write（int）} 方法的方式编写。
     *
     * @param c 要打印的 {@code 字符}
     */
    public void print(char c) {
        write(String.valueOf(c));
    }

    /**
     * 打印整数。 {@link 生成的字符串
     * java.lang.String#valueOf（int）} 被转换为字节
     * 根据平台默认的字符编码，以及这些字节
     * 完全按照
     * {@link #write（int）} 方法。
     *
     * @param i 要打印的 {@code int}
     * @see java.lang.Integer#toString（int）
     */
    public void print(int i) {
        write(String.valueOf(i));
    }

    /**
     * 打印长整数。 {@link 生成的字符串
     * java.lang.String#valueOf（long）} 被翻译成字节
     * 根据平台默认的字符编码，以及这些字节
     * 完全按照
     * {@link #write（int）} 方法。
     *
     * @param l 要打印的 {@code long}
     * @see java.lang.Long#toString（long）
     */
    public void print(long l) {
        write(String.valueOf(l));
    }

    /**
     * 打印浮点数。 {@link 生成的字符串
     * java.lang.String#valueOf（float）} 被转换为字节
     * 根据平台默认的字符编码，以及这些字节
     * 完全按照
     * {@link #write（int）} 方法。
     *
     * @param f 要打印的 {@code float}
     * @see java.lang.Float#toString（float）
     */
    public void print(float f) {
        write(String.valueOf(f));
    }

    /**
     * 打印双精度浮点数。 生成的字符串
     * {@link java.lang.String#valueOf（double）} 被翻译成
     * 字节根据平台的默认字符编码，这些
     * 字节的写入方式与 {@link
     * #write（int）} 方法。
     *
     * @param d 要打印的 {@code double}
     * @see java.lang.Double#toString（double）
     */
    public void print(double d) {
        write(String.valueOf(d));
    }

    /**
     *打印字符数组。 字符转换为字节
     * 根据给定给构造函数的字符编码，或
     * 平台的默认字符编码（如果未指定）。这些字节
     * 完全按照 {@link #write（int）} 方法的方式编写。
     *
     * @param s 要打印的字符数组
     *
     * @throws NullPointerException 如果 {@code s} 为 {@code null}
     */
    public void print(char s[]) {
        write(s);
    }

    /**
     * 打印字符串。 如果参数为 {@code null}，则字符串
     * {@code “null”} 被打印出来。 否则，字符串的字符为
     * 根据给定的字符编码转换为字节
     * 构造函数，或平台的默认字符编码（如果为否）
     *指定。这些字节的写入方式与
     * {@link #write（int）} 方法。
     *
     * @param s 要打印的 {@code String}
     */
    public void print(String s) {
        write(String.valueOf(s));
    }

    /**
     *打印对象。 由 {@link 生成的字符串
     * java.lang.String#valueOf（Object）} 方法转换为字节
     * 根据平台默认的字符编码，以及这些字节
     * 完全按照
     * {@link #write（int）} 方法。
     *
     * @param obj 要打印的 {@code 对象}
     * @see java.lang.Object#toString（）
     */
    public void print(Object obj) {
        write(String.valueOf(obj));
    }
```

## 五、方法的递归调用

### 5.1、概念

方法的递归调用是指在方法的执行过程中直接或间接地调用自己

。
递归是一种常用的编程技术，特别适用于解决可以被分解为相同问题的子问题的情况，例如树的遍历、阶乘计算、斐波那契数列等。

### 5.2、在使用递归调用时，需要注意以下几点

**1、递归终止条件：** 在递归方法中，必须包含递归终止条件，以避免无限递归调用，导致栈溢出。递归调用如果没有结束条件的话，会出现栈内存溢出错误： java.lang.StackOverflowError    
**2、递归调用栈**： 每次进行递归调用时，都会在调用栈上创建一个新的方法调用帧。因此，递归调用的层数不能太深，否则可能导致栈溢出错误。     
**3、性能考虑：** 递归调用可能会导致性能下降，因为每次递归调用都会涉及方法调用、栈帧的创建和销毁等操作。在某些情况下，使用迭代或其他方法可能更有效。    
**4、空间复杂度：** 递归调用的空间复杂度通常较高，因为需要在调用栈上保存每次方法调用的状态。在设计递归算法时，应该考虑到这一点。    
**5、测试和调试：** 递归调用的测试和调试可能比较困难，因为需要考虑递归的深度和复杂度。可以使用断点调试、打印调试信息等方法来帮助理解和调试递归算法。    

>在实际开发中，如果因为递归调用发生了栈内存溢出错误，该怎么办？
>首先可以调整栈内存的大小。扩大栈内存。
>如果扩大之后，运行一段时间还是出现了栈内存溢出错误。
>可能是因为递归结束条件不对。需要进行代码的修改。

```java

public class MethodRecursionTest01{

    public static void main(String[] args){
        int n = 5;
        int result = jieCheng(n);
        System.out.println("result = " + result);
    }

    public static int jieCheng(int n){
        if(n == 1){
            return 1;
        }
        return n * jieCheng(n - 1);
    }
}
```






# 类

## 一、类的定义

在计算机编程中，类（Class）是一种抽象数据类型（ADT），它是面向对象编程（OOP）的基本概念之一。类是对现实世界中对象的抽象，它定义了对象的属性（成员变量）和行为（成员方法）。

**类的定义通常包括以下几个要素：**

1. **类名（Class Name）**：类的名称用于标识该类，在代码中可以通过类名来引用该类。类名通常使用大驼峰命名法（Pascal Case）。

2. **成员变量（Member Variables）**：也称为属性或字段（Fields），用于描述类的状态或特征。成员变量可以是各种数据类型（如整数、浮点数、字符串等），它们代表了对象的各种属性。在类的定义中，成员变量通常以变量名和数据类型的形式列出。

3. **成员方法（Member Methods）**：也称为函数或操作（Methods），用于描述类的行为或功能。成员方法定义了对象可以执行的操作，它们可以操作对象的状态，并且可以被外部代码调用以执行特定的任务。在类的定义中，成员方法通常以方法名、参数列表和返回类型的形式列出。

4. **构造方法（Constructor）**：是一种特殊类型的成员方法，用于在创建对象时初始化对象的状态。构造方法的名称与类名相同，并且通常没有返回类型。在Java等编程语言中，通过调用构造方法可以创建类的实例。

5. **访问修饰符（Access Modifiers）**：用于控制类的成员对外部代码的可见性和访问权限。常见的访问修饰符包括public、protected、private等。

一个简单的类定义示例（使用Java语言）如下所示：

```java
public class MyClass {
    // 成员变量
    private int myNumber;
    private String myString;
    
    // 构造方法
    public MyClass(int number, String str) {
        this.myNumber = number;
        this.myString = str;
    }
    
    // 成员方法
    public void printDetails() {
        System.out.println("Number: " + myNumber);
        System.out.println("String: " + myString);
    }
}
/*
 在这个示例中，类名为MyClass，包含了两个成员变量（myNumber和myString）、一个构造方法（MyClass）和一个成员方法（printDetails）。
 这个类定义了一个简单的数据结构，表示了一个具有整数和字符串属性的对象，并且提供了一个方法用于打印对象的属性。       
 */
```


## 二、类对象的创建和使用

创建和使用类对象是面向对象编程中的基本操作，它们使我们能够使用类定义的属性和方法来操作对象。

**以下是创建和使用类对象的一般步骤：**

1. **类定义**：首先，我们需要定义一个类，其中包括类的属性（成员变量）和方法（成员方法）。
2. **对象实例化**：在程序中，通过使用类的构造方法来创建类的实例（对象）。构造方法会初始化对象的状态，并返回一个指向该对象的引用。
3. **访问成员变量**：一旦对象被创建，我们可以使用点操作符（`.`）来访问对象的成员变量，并为其赋值或获取值。
4. **调用成员方法**：同样，我们也可以使用**点操作符**来调用对象的成员方法，并向方法传递参数（如果需要）。

以下是一个简单的示例，演示了如何创建类对象并使用它：

```java
public class MyClass {
    // 成员变量
    private int myNumber;
    private String myString;
    
    // 构造方法
    public MyClass(int number, String str) {
        this.myNumber = number;
        this.myString = str;
    }
    
    // 成员方法
    public void printDetails() {
        System.out.println("Number: " + myNumber);
        System.out.println("String: " + myString);
    }
}

public class Main {
    public static void main(String[] args) {
        // 创建类对象
        MyClass obj = new MyClass(10, "Hello");
        
        // 访问成员变量
        int number = obj.myNumber;
        String str = obj.myString;
        System.out.println("Number: " + number);
        System.out.println("String: " + str);
        
        // 调用成员方法
        obj.printDetails();
    }
}
/*
 在这个示例中，我们首先定义了一个名为MyClass的类，其中包含了一个构造方法（用于初始化对象的状态）和一个成员方法（用于打印对象的属性）。
 然后，在Main类中，我们通过调用MyClass的构造方法创建了一个名为obj的对象。
 接着，我们通过点操作符访问对象的成员变量，并调用对象的成员方法来操作对象。 
 */
```

## 三、JVM内存分析

```java
package com.camellia.oop01;
/*实例变量属于成员变量，成员变量如果没有手动赋值，系统会赋默认值
    数据类型        默认值
    ----------------------
    byte            0
    short           0
    int             0
    long            0L
    float           0.0F
    double          0.0
    boolean         false
    char            \u0000
    引用数据类型      null
 */
public class Student {

    // 属性：姓名，年龄，性别，他们都是实例变量

    // 姓名
    String name;

    // 年龄
    int age;

    // 性别
    boolean gender;
}
```

```java
package com.camellia.oop01;

public class StudentTest01 {
    public static void main(String[] args) {
        // 局部变量
        int i = 10;

        // 通过学生类Student实例化学生对象

（通过类创造对象）
        // Student s1; 是什么？s1是变量名。Student是一种数据类型名。属于引用数据类型。
        // s1也是局部变量。和i一样。
        // s1变量中保存的是：堆内存中Student对象的内存地址。
        // s1有一个特殊的称呼：引用
        // 什么是引用？引用的本质上是一个变量，这个变量中保存了java对象的内存地址。
        // 引用和对象要区分开。对象在JVM堆当中。引用是保存对象地址的变量。
        Student s1 = new Student();

        // 访问对象的属性（读变量的值）
        // 访问实例变量的语法：引用.变量名
        // 两种访问方式：第一种读取，第二种修改。
        // 读取：引用.变量名 s1.name; s1.age; s1.gender;
        // 修改：引用.变量名 = 值; s1.name = "jack"; s1.age = 20; s1.gender = true;
        System.out.println("姓名：" + s1.name); // null
        System.out.println("年龄：" + s1.age); // 0
        System.out.println("性别：" + (s1.gender ? "男" : "女"));

        // 修改对象的属性（修改变量的值，给变量重新赋值）
        s1.name = "张三";
        s1.age = 20;
        s1.gender = true;

        System.out.println("姓名：" + s1.name); // 张三
        System.out.println("年龄：" + s1.age); // 20
        System.out.println("性别：" + (s1.gender ? "男" : "女")); // 男

        // 再创建一个新对象
        Student s2 = new Student();

        // 访问对象的属性
        System.out.println("姓名=" + s2.name); // null
        System.out.println("年龄=" + s2.age); // 0
        System.out.println("性别=" + (s2.gender ? "男" : "女"));

        // 修改对象的属性
        s2.name = "李四";
        s2.age = 20;
        s2.gender = false;

        System.out.println("姓名=" + s2.name); // 李四
        System.out.println("年龄=" + s2.age); // 20
        System.out.println("性别=" + (s2.gender ? "男" : "女")); // 女


    }
}

```

![在这里插入图片描述](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292313480.png)

从此图可以看出，开始将所有类的字节码存储到元空间当中，当对象被创建时就在堆内存中开辟一个空间，用于存储对象和实例变量等。然后通过引用实现对对象的一系列操作。
其中对象属性等的改变都发生在堆内存中，引用只不过保存了它的地址（这和C++中的指针很像）。

## 四、实例变量和实例方法的访问
1. 实例变量要想访问，必须先new对象。通过引用来访问实例变量。    
2. 实例变量是不能通过类名直接访问的。
3. 我们通常描述一个对象的行为动作时，不加static。 没有添加static的方法，被叫做：实例方法。（对象方法）
4. 空指针异常：一个空引用访问实例相关的，都会出现空指针异常。
```java
public class Pet {
    
    String name; // 实例变量
    // 出生日期
    String birth;
    // 性别
    char sex;

    // 方法：行为动作
    // 吃
    public void eat(){ // 实例方法
        System.out.println("宠物在吃东西");
    }
    // 跑
    public void run(){
        System.out.println("宠物在跑步");
    }
}
```
```java
public class PetTest02 {
    public static void main(String[] args) {
        // 创建宠物对象
        Pet dog = new Pet();

        // 给属性赋值
        dog.name = "小黑";
        dog.birth = "2012-10-11";
        dog.sex = '雄';

        // 读取属性的值
        System.out.println("狗狗的名字：" + dog.name);
        System.out.println("狗狗的生日：" + dog.birth);
        System.out.println("狗狗的性别：" + dog.sex);

        dog = null;

        // 注意：引用一旦为null，表示引用不再指向对象了。但是通过引用访问name属性，编译可以通过。
        // 运行时会出现异常：空指针异常。NullPointerException。这是一个非常著名的异常。
        // 为什么会出现空指针异常？因为运行的时候会找真正的对象，如果对象不存在了，就会出现这个异常。
        //System.out.println("狗狗的名字：" + dog.name);

        // 会出现空指针异常。
        dog.eat();

        // 会出现空指针异常。
        //dog.run();
    }
}
//java.lang.NullPointerException
```
>如果没有任何引用指向对象，该对象最终会被当做垃圾被GC回收。


## 五、方法调用时传递参数

### 5.1、方法调用时传递基本数据类型
```java
package com.camellia.oop04;

/**
 * 面试题：判断该程序的输出结果
 */
public class ArgsTest01 {
    public static void main(String[] args) {
        int i = 10;
        // 调用add方法的时候，将i传进去，实际上是怎么传的？将i变量中保存值10复制了一份，传给了add方法。
        add(i);
        System.out.println("main--->" + i); // 10
    }
    public static void add(int i){ // 方法的形参是局部变量。
        i++;
        System.out.println("add--->" + i); // 11
    }
}
```

![在这里插入图片描述](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292318843.png)

### 5.2、方法调用时传递引用数据类型

```java
package com.camellia.oop04;
public class User {
    int age;
}
```
```java
package com.camellia.oop04;

/**
 * 面试题：分析以下程序输出结果
 */
public class ArgsTest02 {
    public static void main(String[] args) {
        User u = new User();
        u.age = 10;
        // u是怎么传递过去的。实际上和i原理相同：都是将变量中保存的值传递过去。
        // 只不过这里的u变量中保存的值比较特殊，是一个对象的内存地址。
        add(u);
        System.out.println("main-->" + u.age); // 11
    }
    public static void add(User u) { // u是一个引用。
        u.age++;
        System.out.println("add-->" + u.age); // 11
    }
}
```

>这个和基本数据类型原理相同。首先明确引用数据类型中应用存储的是User的地址，所以add(User u);实质上是将main中的引用u里存储的值（就是new User();的地址）复制一份给add方法。



## * 六、封装
**概念：** 封装是面向对象编程中的一个重要概念，它指的是将数据和操作数据的方法捆绑在一起，并限制对数据的访问。
         封装的目的是隐藏对象的内部细节，只向外界暴露必要的接口，以防止外部代码直接访问对象的内部状态，从而提高代码的安全性和可维护性。    
**如何实现封装：**         
**数据隐藏（Data Hiding）：** 封装通过将对象的数据隐藏起来即属性私有化，只允许通过对象的方法来访问和修改数据，从而防止外部直接访问对象的内部状态。    
**访问控制（Access Control）：** 通常，封装会将对象的属性设置为私有（private），只允许通过公共（public）方法来访问和修改这些属性。    
```java
package com.camellia.oop07;
/**
 * 为了保证User类型对象的age属性的安全，我们需要使用封装机制。实现封装的步骤是什么？
 *      第一步：属性私有化。(什么是私有化？使用 private 进行修饰。)
 *      属性私有化的作用是：禁止外部程序对该属性进行随意的访问。
 *      所有被private修饰的，都是私有的，私有的只能在本类中访问。
 *
 *      第二步：对外提供setter和getter方法。
 *      为了保证外部的程序仍然可以访问age属性，因此要对外提供公开的访问入口。
 *      访问一般包括两种：
 *          读：读取属性的值
 *          改：修改属性的值
 *      那么应该对外提供两个方法，一个负责读，一个负责修改。
 *      读方法的格式：getter
 *          public int getAge(){}
 *      改方法的格式：setter
 *          public void setAge(int age){}
 */
public class User {
    private int age;

    // 读取age属性的值
    // getter方法是绝对安全的。因为这个方法是读取属性的值，不会涉及修改操作。
    public int getAge(){
        //return this.age;
        return age;
    }

    // 修改age属性的值
    // setter方法当中就需要编写拦截过滤代码，来保证属性的安全。
    // java有就近原则，若不加this关键字都默认是形参age。
    public void setAge(int age){
        if(age < 0 || age > 100) {
            System.out.println("对不起，您的年龄值不合法！");
            return;
        }
        // this. 大部分情况下可以省略。
        // this. 什么时候不能省略？用来区分局部变量和实例变量的时候。
        this.age = age;
    }
}
```
```java
package com.camellia.oop07;

public class UserTest {
    public static void main(String[] args) {
        User u = new User();
        // 读
        System.out.println("年龄：" + u.getAge());

        // 改
        u.setAge(-100);
        
        // 读
        System.out.println("年龄：" + u.getAge());
        
        //改
        u.setAge(50);
        
        //读
        System.out.println("年龄：" + u.getAge()); // 50
    }
}
```

## * 七、构造方法

### 7.1、构造方法的基本知识点

#### 1、构造方法的作用
**对象的创建：** 构造方法通过调用完成对象的创建。当使用 new 关键字实例化一个对象时，构造方法被调用，对象在内存中被创建并分配空间。    
**对象的初始化：** 构造方法用于给对象的所有属性赋值，即对象的初始化。它确保对象在创建后处于一个合适的状态，属性被赋予初始值，以便对象可以正常运行。   

#### 2、定义构造方法的方式
```java
[修饰符列表] 构造方法名(形参列表) {
构造方法体;
}
```
**注意事项：**    
* 构造方法名必须和类名一致，以便编译器能够识别并与类关联。    
* 构造方法不需要提供返回值类型，因为它的主要目的是创建对象，而不是返回值。    
* 如果提供了返回值类型，则该方法不再是构造方法，而是普通方法，不能用于对象的创建。    

#### 3、构造方法怎么调用呢？
*  使用new运算符来调用。
*  语法：new 构造方法名(实参);
*  注意：构造方法最终执行结束之后，会自动将创建的对象的内存地址返回。但构造方法体中不需要提供“return 值;”这样的语句。

#### 4、构造方法相关注意事项
* 在Java语言中，如果一个类没有显式定义构造方法，系统会默认提供一个无参数的构造方法。这个构造方法通常称为缺省构造器。
* 如果一个类显式定义了构造方法，系统则不再提供缺省构造器。因此，为了对象创建更加方便，建议手动编写一个无参数的构造方法。
* 在Java中，一个类可以定义多个构造方法，并且这些构造方法自动构成了方法的重载。这意味着可以根据不同的参数列表调用不同的构造方法来创建对象。
* 构造方法中给属性赋值是对象第一次创建时属性的初始值。然而，单独定义set方法给属性赋值的好处在于后期可以灵活地修改属性的值。这种方式允许在对象创建后，根据需要修改对象的属性，从而增加了对象的灵活性和可维护性。

#### 5、构造方法的执行原理

- 构造方法的执行包括两个重要的阶段：
    - 第一阶段：对象的创建
    - 第二阶段：对象的初始化

- 对象在什么时候创建的？
    - 当使用`new`关键字实例化一个对象时，在堆内存中直接开辟空间。这个过程中，会给对象的所有属性**赋默认值**，完成对象的创建。这一过程发生在构造方法体执行之前。
- 对象初始化在什么时候完成的？
    - 构造方法体开始执行时，标志着对象的初始化过程开始。在构造方法体中，可以对对象的属性进行赋值等初始化操作。构造方法体执行完毕，表示对象初始化完毕。此时，对象处于可用状态，可以被程序进一步操作和调用。

#### 6、构造代码块
- **语法格式：**
    - 构造代码块的语法格式为一对大括号`{}`，没有参数列表。

- **执行时机及次数：**
    - 每次在使用`new`关键字创建对象时，构造代码块都会被执行。
    - 构造代码块是在构造方法执行之前执行的，因此在对象的初始化过程中，构造代码块是首先被执行的。    
```java
public class Example {
    private int x;
    private int y;

    // 构造代码块
    {
        System.out.println("构造代码块被执行");
        x = 5;
        y = 10;
    }

    // 构造方法
    public Example() {
        System.out.println("构造方法被调用");
    }

    // 获取x的值
    public int getX() {
        return x;
    }

    // 获取y的值
    public int getY() {
        return y;
    }

    public static void main(String[] args) {
        // 创建对象
        Example obj = new Example();
        // 输出属性值
        System.out.println("x 的值为：" + obj.getX());
        System.out.println("y 的值为：" + obj.getY());
    }
}

```

#### 7、构造代码块的作用

构造代码块可以用于将对象初始化时共享的代码抽取出来，实现代码的复用。具体而言：
- 如果所有的构造方法在最开始的时候有相同的一部分代码，可以将这部分代码放入构造代码块中。
- 构造代码块会在每次对象创建时都执行，确保共享的代码被执行，并且避免了代码重复。
这样，通过构造代码块，可以提高代码的可维护性和可读性，减少代码冗余，提高代码复用性。

## *八、this关键字
this 本质上是一个引用。this 中保存的是当前对象的内存地址。
在Java中，`this` 是一个关键字，用于引用当前对象的实例。它通常用于区分实例变量和方法参数之间的命名冲突，或者在一个类的方法内部调用同一个类的另一个方法。下面详细解释 `this` 的几个常见用途：

1. **区分实例变量和方法参数**：当方法参数的名称与实例变量的名称相同时，使用 `this` 来引用当前对象的实例变量。这样可以明确指示要访问的是实例变量而不是方法参数。

   ```java
   public class MyClass {
       private int value;

       public void setValue(int value) {   //这个形参与属性value相同，若不加this则根据Java中的就近原则，方法中的value都是形参value。
           this.value = value; // 使用 this 引用实例变量
       }
   }
   ```

   这里 `this.value` 指的是当前对象的 `value` 实例变量，而 `value` 是方法的参数。

2. **在构造器中调用另一个构造器**：可以使用 `this` 调用**同一个类**的另一个构造器，且只能出现在第一行。这种方法通常被称为**构造器重载**。

   ```java
   public class MyClass {
       private int value;
       private String name;

       public MyClass() {
           //new MyClass(10,"giaogiao");  这么会创建一个新对象
           this(10,"giaogiao");// 调用另一个构造器
   
           /*这个的目的是什么？
             当要求类在初始化时，给它赋指定的默认值。
             EG：this.value=10;
                 this.name="giaogiao";
             这段代码其实是重复的。而通过this(10,"giaogiao");获取当前对象，调用MyClass(int value,String name)构造器以简化开发。
           */
            
       }

       public MyClass(int value,String name) {
           this.value = value;
           this.name=name;
       }
   }
   ```

   在这个例子中，无参构造器调用了带参构造器，以避免重复代码。

3. **传递当前对象的引用**：可以将当前对象的引用传递给其他方法，这在某些情况下很有用。

![在这里插入图片描述](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292320206.png)


```java
package com.camellia.oop6;

// 学生类
public class Student {
  // 私有成员变量 name
  private String name;

  // 带参构造方法，用于初始化 name
  public Student(String name) {
    this.name = name;
  }

  // 无参构造方法
  public Student() {
  }

  // 获取学生姓名的方法
  public String getName() {
    return name;
  }

  // 设置学生姓名的方法
  public void setName(String name) {
    this.name = name;
  }

  // 学习方法，打印当前对象的引用地址
  public void study(){
    System.out.println("study---->" + this);  // 验证this是当前对象的引用。
  }
}

```
```java
package com.camellia.oop6;

// 测试类
public class StudentTest {
  public static void main(String[] args) {
    // 创建学生对象s1，初始化姓名为"小吴"
    Student s1 = new Student("小吴");
    // 打印s1对象的引用地址
    System.out.println("main---->" + s1);
    // 调用s1对象的study()方法
    s1.study();

    // 创建学生对象s2，初始化姓名为"小花"
    Student s2 = new Student("小花");
    // 打印s2对象的引用地址
    System.out.println("main---->" + s2);
    // 调用s2对象的study()方法
    s2.study();
  }
}

```
>在Java中，当对象调用自己的方法时，方法体内的 this 关键字会引用该对象的实例。
>在方法被调用时，Java虚拟机会隐式地将当前对象的引用传递给方法，以便方法能够访问对象的成员变量和方法。
>因此，在普通方法中通过 this 关键字引用的就是调用该方法的当前对象。


## 九、static关键字
在Java中，使用static关键字声明的成员（变量、方法、代码块）是类级别的，而不是与类的每个实例相关联的。    
因此，它们可以通过类名直接访问，而无需创建类的实例。
### 9.1、静态变量存储图
   1、没使用静态变量是的存储图
```java
package com.camellia.oop7;

public class User {
    //用户id
    private String id;
    //用户国籍
    private String country="China";

    public User() {
    }

    public User(String id) {
        this.id = id;
    }
    public void PrintInfo(){
        System.out.println("ID: " + id+"\tCountry: " + country);
    }
}
```
```java
package com.camellia.oop7;

public class UserTest {
    public static void main(String[] args) {
        User user1 = new User("1001");
        user1.PrintInfo();
        User user2 = new User("1002");
        user2.PrintInfo();
        User user3 = new User("1003");
        user3.PrintInfo();
    }
}
```
![在这里插入图片描述](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292320213.png)



2、使用静态变量时的存储图

```java
package com.camellia.oop8;

public class User {
    //用户id
    private String id;
    //用户国籍
    //静态变量什么时候开劈空间（初始化）、存储在哪里？
    //类加载时初始化
    //JDK8之后：静态变量存储在堆内存之中

    private static String country="China";

    public User() {
    }

    public User(String id) {
        this.id = id;
    }
    public void PrintInfo(){
        System.out.println("ID: " + id+"\tCountry: " + country);
    }
}
```
```java
package com.camellia.oop8;

import com.camellia.oop7.User;

public class UserTest {
    public static void main(String[] args) {
        com.camellia.oop7.User user1 = new com.camellia.oop7.User("1001");
        user1.PrintInfo();
        com.camellia.oop7.User user2 = new com.camellia.oop7.User("1002");
        user2.PrintInfo();
        com.camellia.oop7.User user3 = new User("1003");
        user3.PrintInfo();
    }
}
```
![在这里插入图片描述](https://camelliaxiaohua-1313958787.cos.ap-shanghai.myqcloud.com/JavaSE-asserts/202404292320410.png)

### 9.2、Java中静态变量和方法的访问，以及静态变量不能使用this关键字
1. 静态变量和方法建议使用`类名.`调用。虽然用`引用.`也可以，但是实质还是通过类来调用，而且这样容易和实例变量和方法的访问相混淆。    
2. 静态方法不能使用 this 关键字是因为 this 关键字代表当前对象的实例，而静态方法是与类相关联的，不依赖于任何特定的实例。所以无法直接访问实例变量和方法。

### 9.3、静态代码块
静态代码块是使用 `static` 关键字声明的代码块，它在类被加载时执行，并且只执行一次。
静态代码块通常用于在类加载时进行初始化操作，例如初始化静态变量或执行静态方法。它们的执行顺序是在类加载时按照代码顺序执行。

**静态代码块的特点包括：**

1. **使用 `static` 关键字声明**：静态代码块使用 `static` 关键字进行声明，以标识它们是与类相关联的，而不是与类的实例相关联的。

2. **在类加载时执行**：静态代码块在类被加载时执行，并且只执行一次。类的加载是指当 JVM 第一次加载类时发生的操作，通常在首次创建类的实例之前。

3. **仅执行一次**：静态代码块只会在类加载时执行一次，即使没有创建类的实例也会执行。

示例：

```java
public class StaticTest01 { 

    // 实例方法
    public void doSome(){ 
        System.out.println(name);
    }

    // 实例变量
    String name = "zhangsan"; 

    // 静态变量
    static int i = 100;

    // 静态代码块
    static {
        // 报错原因：在静态上下文中无法直接访问实例相关的数据。
        //System.out.println(name);
        // 这个i可以访问，是因为i变量是静态变量，正好也是在类加载时初始化。
        System.out.println(i);
        System.out.println("静态代码块1执行了");
        // j无法访问的原因是：程序执行到这里的时候，j变量不存在。
        //System.out.println(j);

        System.out.println("xxxx-xx-xx xx:xx:xx 000 -> StaticTest01.class完成了类加载！");
    }

    // 静态变量
    static int j = 10000;

    // 静态代码块
    static {
        System.out.println("静态代码块2执行了");
    }

    public static void main(String[] args) {
        System.out.println("main execute!");
    }

    // 静态代码块
    static {
        System.out.println("静态代码块3执行了");
    }
}
//静态代码的执行顺序只能靠编写顺序的来确定，编写时在前的也就先执行。
```




# 单例模式
==**实现单例模式的步骤**==   

1. 私有化构造方法
确保外部不能直接通过构造方法来实例化对象，从而限制对象的创建。
2. 提供静态方法获取实例
通过一个静态方法来获取单例对象的实例，通常命名为 getInstance()。
3. 提供一个静态变量（对于饿汉和懒汉不同）

## 一、饿汉式单例模式

1. 私有化构造方法
   确保外部不能直接通过构造方法来实例化对象，从而限制对象的创建。
2. 提供静态方法获取实例
   通过一个静态方法来获取单例对象的实例，通常命名为 getInstance()。
3. 定义一个静态变量
   在类加载的时候，初始化静态变量。（只初始化一次）

```java
package com.camellia.singleton1;

/**
 * 饿汉单例模式
 */
public class Singleton {
    //饿汉式单例模式：类加载时对象就创建好了。不管这个对象用还是不用。提前先把对象创建好。
    private static Singleton instance = new Singleton();

    private Singleton() {
    }


    public static Singleton getInstance() {
        return instance;
    }
}
```
```java
package com.camellia.singleton1;

public class SingletionTest {
    public static void main(String[] args) {
        Singleton instance1 = Singleton.getInstance();
        Singleton instance2 = Singleton.getInstance();
        System.out.println(instance1 == instance2);   //比较引用存储的对象地址。
    }
}
```

## 二、懒汉式单例模式
1. 私有化构造方法
   确保外部不能直接通过构造方法来实例化对象，从而限制对象的创建。
2. 提供静态方法获取实例
   通过一个静态方法来获取单例对象的实例，通常命名为 getInstance()。
3. 定义一个静态变量
   但是这个变量值为null。

```java
package com.camellia.singleton2;

/**
 * 懒汉模式
 */
public class Singleton {
    private static Singleton instance;
    private Singleton(){}
    public static Singleton getInstance(){
        if(instance == null){
            instance = new Singleton();
        }
        return instance;
    }

}
```
```java
package com.camellia.singleton2;

public class SingletonTest {
    public static void main(String[] args) {
        Singleton instance1 = Singleton.getInstance();
        Singleton instance2 = Singleton.getInstance();
        System.out.println(instance1 == instance2);
    }
}
```





