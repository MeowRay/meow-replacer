# meow-replacer 


设定指定目录递归替换指定文件中符合条件的字符串

* 需求前置 pyyaml

![image](https://github.com/user-attachments/assets/1e6d842e-3484-4062-a633-7b245a723b0d)



```
work_directory: "./replacer-work"
file_patterns: ['\.txt$', '\.yml$', '\.conf$', '\.sql$']
replacements:
  - exact_match: "INSERT INTO settings VALUES(2,'webPort','{{xuiPort}}');"
    replace_with: "INSERT INTO settings VALUES(2,'webPort','23333');"
    # 最多替换1次，如果不设置或为-1，则替换所有匹配项
    replace_count: 1  
    
  - exact_match: "INSERT INTO settings VALUES(6,'webBasePath','{{xuiPath}}');"
    replace_with: "INSERT INTO settings VALUES(6,'webBasePath','/114514/');"
    replace_count: 1




    # key=regex_match 为正则匹配
  - regex_match: "('us-1)([a-zA-Z0-9-_]+)(')"
    replace_with: "'{{prefix}}$2'"
    replace_count: -1

```
