import os
import re
import yaml
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('config.yml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

work_directory = config['work_directory']
file_patterns = config['file_patterns']
replacements = config['replacements']

for root, _, files in os.walk(work_directory):
    for file_name in files:
        if any(re.search(pattern, file_name) for pattern in file_patterns):
            file_path = os.path.join(root, file_name)
            logging.info(f'正在处理文件: {file_path}')
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for replacement in replacements:
                replace_count = replacement.get('replace_count', -1)
                
                if 'exact_match' in replacement:
                    if replacement['exact_match'] in content:
                        logging.info(f'精确匹配替换: "{replacement["exact_match"]}" -> "{replacement["replace_with"]}"，替换次数: {replace_count}')
                    content = content.replace(replacement['exact_match'], replacement['replace_with'], replace_count)
                
                elif 'regex_match' in replacement:
                    pattern = replacement['regex_match']
                    replacement_text = replacement['replace_with']
                    
                    def replace_func(match):
                        result = replacement_text
                        for i in range(1, len(match.groups()) + 1):
                            result = result.replace(f'${i}', match.group(i))
                        return result
                    
                    if re.search(pattern, content):
                        logging.info(f'正则表达式替换: "{pattern}" -> "{replacement_text}"，替换次数: {replace_count}')
                    content = re.sub(pattern, replace_func, content, count=replace_count)
                    
                    logging.debug(f'替换后的内容: {content}')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logging.info(f'完成处理文件: {file_path}')

logging.info("所有替换操作完成")
