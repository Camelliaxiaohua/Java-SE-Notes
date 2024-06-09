#SUBSTRING_INDEX

`SUBSTRING_INDEX` 是 MySQL 中用于截取字符串的函数，可以根据指定的分隔符将字符串拆分并返回特定部分。该函数非常适用于需要从字符串中提取特定子字符串的场景。

### 基本语法

```sql
SUBSTRING_INDEX(str, delim, count)
```

- **`str`**：要处理的字符串。
- **`delim`**：字符串中的分隔符。
- **`count`**：指定要返回的部分。正数表示从左到右，负数表示从右到左。

### 示例

假设我们有一个表 `users`，其中有一列 `email` 存储用户的电子邮件地址：

| id | email                |
|----|----------------------|
| 1  | john.doe@example.com |
| 2  | jane.smith@test.com  |
| 3  | alice@domain.org     |

我们想要从电子邮件地址中提取用户名（即 `@` 符号前的部分）。可以使用 `SUBSTRING_INDEX` 实现：

```sql
SELECT email, SUBSTRING_INDEX(email, '@', 1) AS username
FROM users;
```

### 结果

| email                | username |
|----------------------|----------|
| john.doe@example.com | john.doe |
| jane.smith@test.com  | jane.smith|
| alice@domain.org     | alice    |

### 详细示例

1. **从字符串中提取域名（`@` 符号后的部分）**：

    ```sql
    SELECT email, SUBSTRING_INDEX(email, '@', -1) AS domain
    FROM users;
    ```

    结果：

    | email                | domain       |
    |----------------------|--------------|
    | john.doe@example.com | example.com  |
    | jane.smith@test.com  | test.com     |
    | alice@domain.org     | domain.org   |

2. **从URL中提取协议（假设表中有一列 `url`）**：

    ```sql
    SELECT url, SUBSTRING_INDEX(url, '://', 1) AS protocol
    FROM websites;
    ```

    如果 `websites` 表如下：

    | id | url                         |
    |----|-----------------------------|
    | 1  | https://www.example.com     |
    | 2  | http://test.com             |
    | 3  | ftp://files.domain.org      |

    结果：

    | url                         | protocol |
    |-----------------------------|----------|
    | https://www.example.com     | https    |
    | http://test.com             | http     |
    | ftp://files.domain.org      | ftp      |

3. **提取某个字符串中的第一个单词**：

    ```sql
    SELECT sentence, SUBSTRING_INDEX(sentence, ' ', 1) AS first_word
    FROM phrases;
    ```

    如果 `phrases` 表如下：

    | id | sentence                  |
    |----|---------------------------|
    | 1  | Hello world!              |
    | 2  | OpenAI develops AI models |
    | 3  | SQL is fun                |

    结果：

    | sentence                  | first_word |
    |---------------------------|------------|
    | Hello world!              | Hello      |
    | OpenAI develops AI models | OpenAI     |
    | SQL is fun                | SQL        |

### 使用注意事项

- 如果 `count` 为正数，则从字符串左边开始计数。
- 如果 `count` 为负数，则从字符串右边开始计数。
- 如果 `count` 超出分隔符的数量，则返回整个字符串。

`SUBSTRING_INDEX` 是处理字符串的强大工具，通过合理设置分隔符和计数，可以方便地提取出所需的子字符串。