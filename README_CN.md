# MSMAP

Msmap是一个内存马生成器，兼容多种容器、组件、编码器、*WebShell / Proxy / Killer* 和管理客户端。

[English](README.md)

![](img/a.png)

<details>
<summary>功能 [WIP]</summary>

### Function

- [x] 动态菜单
- [x] 自动编译
- [x] 生成脚本
- [ ] 精简模式
- [ ] 图形界面

### Container

- Java
  - [ ] Tomcat7
  - [x] Tomcat8
  - [x] Tomcat9
  - [x] Tomcat10
  - [ ] Resin
  - [ ] Weblogic
- .NET
  - [ ] IIS

### WebShell / Proxy / Killer

- WebShell
  - [x] CMD / SH
  - [x] AntSword
  - [x] JSPJS
  - [ ] Behinder
  - [ ] Godzilla
- Proxy
  - [ ] Neo-reGeorg
  - [ ] wsproxy
- Killer(As-Exploits)
  - [x] java-memshell-scanner
  - [x] ASP.NET-Memshell-Scanner

### Decoder / Decryptor / Hasher

- Decoder
  - [x] Base64
  - [ ] Hex
- Decryptor
  - [x] RC4
  - [x] AES128
  - [x] AES256
  - [ ] RSA
- Hasher
  - [x] MD5
  - [x] SHA128
  - [x] SHA256

</details>

## 用法

``` bash
git clone git@github.com:hosch3n/msmap.git
cd msmap
python generator.py
```

> [注意] 尽量用独一无二的密码；各选项大小敏感

### 进阶

编辑 `config/environment.py`

``` python
# 自动编译
auto_build = True

# Base64编码类字节码
b64_class = True

# 生成脚本
generate_script = True

# 编译器绝对路径
java_compiler_path = r"~/jdk1.6.0_04/bin/javac"
dotnet_compiler_path = r"C:\Windows\Microsoft.NET\Framework\v2.0.50727\csc.exe"
```

编辑 `gist/java/container/tomcat/servlet.py`

``` java
// Servlet路径匹配规则
private static String pattern = "*.xml";
```

WsFilter暂不支持自动编译。如果使用了加密编码器，密码需要与路径相同（如`/passwd`）

## 示例

<details>
<summary>CMD / SH</summary>

系统**命令** 搭配 **Base64** 编码器 | 注入到 Tomcat Valve

`python generator.py Java Tomcat Valve Base64 CMD passwd`

</details>

<details>
<summary>蚁剑</summary>

**JSP**类型 搭配 **default** 编码器 | 注入到 Tomcat Valve

`python generator.py Java Tomcat Valve RAW AntSword passwd`

**JSP**类型 搭配 **[aes_128_ecb_pkcs7_padding_md5](extend/AntSword/encoder/aes_128_ecb_pkcs7_padding_md5.js)** 编码器 | 注入到 Tomcat Listener

`python generator.py Java Tomcat Listener AES128 AntSword passwd`

**JSP**类型 搭配 **[rc_4_sha256](extend/AntSword/encoder/rc_4_sha256.js)** 编码器 | 注入到 Tomcat Servlet

`python generator.py Java Tomcat Servlet RC4 AntSword passwd`

</details>

## Reference

[GodzillaMemoryShellProject](https://github.com/BeichenDream/GodzillaMemoryShellProject)

[AntSword-JSP-Template](https://github.com/AntSwordProject/AntSword-JSP-Template)

[As-Exploits memshell_manage](https://github.com/yzddmr6/As-Exploits/tree/master/core/memshell_manage)

[Behinder](https://github.com/rebeyond/Behinder) | [wsMemShell](https://github.com/veo/wsMemShell) | [ysomap](https://github.com/wh1t3p1g/ysomap)