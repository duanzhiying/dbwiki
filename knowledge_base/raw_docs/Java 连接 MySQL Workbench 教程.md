# Java 连接 MySQL Workbench 教程

---

## 一、概述

本教程将指导你如何使用 Java 连接 MySQL 数据库，而 MySQL Workbench 作为数据库管理工具，用于创建和管理数据库结构。我们将使用 intellij idea 来帮助实现 Java 与 MySQL 的连接。

---

## 二、准备工作

### 1. 安装工具

*   **Java 开发环境（JDK）**：确保已安装 JDK（建议使用 JDK 8 或以上版本）。
    
*   **MySQL 数据库**：安装 MySQL Server。
    
*   **MySQL Workbench**：用于可视化管理 MySQL 数据库。
    
*   **IntelliJ IDEA。**
    

## 三、配置数据库（使用 MySQL Workbench）

1.  打开 MySQL Workbench。
    
2.  连接本地或远程的 MySQL 服务器。
    
3.  准备数据库。
    

---

**四、创建maven目录，连接数据库并执行SQL语句。**

**1、打开idea，点击文件—新建—项目。**

![屏幕截图 2026-01-04 202256.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/e9c5f07d-44e3-4f40-ae2f-369e9d433fe4.png)

**2、选择maven，点击创建。**![屏幕截图 2026-01-04 202427.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/d9590f1e-e169-4492-b5d6-0f2e3b663d67.png)

**3、双击打开pom.xml,复制粘贴下方代码块。**

```java
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>mysql-connect-demo</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>8</maven.compiler.source>
        <maven.compiler.target>8</maven.compiler.target>
    </properties>

    <dependencies>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.33</version> <!-- 无空格的有效版本 -->
            <scope>runtime</scope>
        </dependency>

    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>25</source>
                    <target>25</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>

```

![屏幕截图 2026-01-04 202635.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/7a7afc86-3715-45e4-8d23-1485a45251b2.png)

**4、选择java—新建—Java类，自由命名。**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/3bcb3be4-01ce-4361-9302-daf36d34976f.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/6c230b9a-1a4e-4d54-b95c-bf9f7425df68.png)

**5、复制粘贴如下代码。**

```java
package mysql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class mysqlutil {
    static void main() {
        String url = "jdbc:mysql://localhost:3306/online_sales_system?serverTimezone=Asia/Shanghai&useSSL=false&allowPublicKeyRetrieval=true";
        String user = "root";
        String password = "wh944555";

        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection(url, user, password);
            System.out.println("数据库连接成功，查询全表数据：");

            // 查items表所有数据
            String sql = "SELECT item_id, item_name FROM items"; // 补充实际字段名
            pstmt = conn.prepareStatement(sql);
            rs = pstmt.executeQuery();

            // 遍历结果集（用getString获取item_id的字符串值）
            while (rs.next()) {
                String itemId = rs.getString("item_id"); // 关键修正
                String itemName = rs.getString("item_name"); // 按实际字段类型选择方法
                System.out.println("商品ID：" + itemId + "，商品名称：" + itemName);
            }

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            // 关闭资源
            try {
                if (rs != null) rs.close();
                if (pstmt != null) pstmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}

```

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/875be6ec-0895-4e26-ae6b-3281c2e0e45d.png)

**6、注意！！！如遇错误可自行修改。**

![屏幕截图 2026-01-04 203811.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/f3f08235-5453-4c2d-a5c5-802b9dcf6147.png)

**7、填写数据库名称、账号和密码，用SQL语句作查询操作。**

![屏幕截图 2026-01-04 204250.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/9535f8bf-035d-442d-9d1a-60e58ef45a98.png)

**8、连接且成功查询。（例）**

![屏幕截图 2026-01-04 201816.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/4a644d51-a3b4-4599-b1ef-1ee5f5154f1a.png)

**over**

**彩蛋：（使用IntelliJ IDEA，无代码版）**

1、打开**IntelliJ IDEA。**

![屏幕截图 2026-01-04 124914.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/7ace3b34-ff85-466c-a98e-3e5b7f2c0367.png)

2、新建项目。![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/b1525b31-27ec-4f97-8b82-2f0716927ca8.png)

3、自由命名项目。![屏幕截图 2026-01-04 125557.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/bd2b0dc5-b158-4be1-b311-d746fe682976.png)

4、选择**datebase。**![屏幕截图 2026-01-04 125903.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/71eb690e-58cf-4c60-9421-a517f6b93679.png)

5、选择**新建。**

![屏幕截图 2026-01-04 130035.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/86c9816d-1638-465e-97e8-5ad6bed95acc.png)

**6、**找到**MySQL。**

![屏幕截图 2026-01-04 130206.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/29c28da9-9b81-4628-8209-224bdbac99d4.png)

**7、**输入MySQL workbench**用户名、密码**和所要连接的**数据库名称。**

![屏幕截图 2026-01-04 130430.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/f0180423-9f1d-4241-a406-1f5c9d8922d9.png)

**8、成功连接数据库，直接输入SQL语句执行即可。（例：）**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/1X3lE5jaZ9Y79lJb/img/86a3d3cd-7d53-46ac-adb1-5a5b83a01294.png)

---