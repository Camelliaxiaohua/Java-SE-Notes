# GROUP_CONCAT

`GROUP_CONCAT` 是 MySQL 中的一个聚合函数，用于将分组中的多个值连接成一个字符串。它在进行数据汇总时特别有用，比如将某一列的多个值连接成一个以逗号分隔的字符串。

### 基本语法

```sql
SELECT GROUP_CONCAT(column_name)
FROM table_name
[WHERE condition]
[GROUP BY column_name2];
```

### 示例

假设有一个名为 `students` 的表，结构和数据如下：

| id | name  | course     |
|----|-------|------------|
| 1  | Alice | Math       |
| 2  | Bob   | Science    |
| 3  | Alice | History    |
| 4  | Bob   | Math       |
| 5  | Alice | Science    |

我们想要得到每个学生所选课程的一个列表。可以使用 `GROUP_CONCAT` 来实现：

```sql
SELECT name, GROUP_CONCAT(course) AS courses
FROM students
GROUP BY name;
```

### 结果

| name  | courses            |
|-------|---------------------|
| Alice | Math,History,Science|
| Bob   | Science,Math        |

### 可选参数

`GROUP_CONCAT` 函数还有一些可选参数可以用来改变其行为：

1. **`SEPARATOR`**：指定分隔符，默认为逗号 `,`。

    ```sql
    SELECT name, GROUP_CONCAT(course SEPARATOR ' | ') AS courses
    FROM students
    GROUP BY name;
    ```

2. **`DISTINCT`**：去重，防止重复值。

    ```sql
    SELECT name, GROUP_CONCAT(DISTINCT course) AS courses
    FROM students
    GROUP BY name;
    ```

3. **`ORDER BY`**：指定连接值的排序方式。

    ```sql
    SELECT name, GROUP_CONCAT(course ORDER BY course ASC) AS courses
    FROM students
    GROUP BY name;
    ```

4. **`LIMIT`**：限制结果的长度（不常用）。

### 综合示例

```sql
SELECT name, GROUP_CONCAT(DISTINCT course ORDER BY course ASC SEPARATOR ' | ') AS courses
FROM students
GROUP BY name;
```

### 结果

| name  | courses                |
|-------|-------------------------|
| Alice | History | Math | Science|
| Bob   | Math | Science          |

通过以上方式，`GROUP_CONCAT` 可以灵活地将多行数据合并成一个字符串，满足各种需求。