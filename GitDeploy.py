import subprocess
import os

rep_path = r'path'
tag_name = 'v1.0.0'


os.chdir(rep_path)

#merge
subprocess.run(['git', 'checkout', 'prd'])
subprocess.run(['git', 'merge', 'dev'])
subprocess.run(['git', 'tag', tag_name])

#push
subprocess.run(['git', 'push', 'origin', 'prd'])
subprocess.run(['git', 'push', 'origin', tag_name])

print(f"Успешное обновлены ветки prd. тег: {tag_name}.")