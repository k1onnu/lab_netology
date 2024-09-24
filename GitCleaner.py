import subprocess

rep_path = 'path here'

# Очистка отслеживаемых изменений
subprocess.run(['git', 'reset', '--hard'], cwd=rep_path)
subprocess.run(['git', 'clean', '-fd'], cwd=rep_path)

print("Репозиторий был успешно очищен.")