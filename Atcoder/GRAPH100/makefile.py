import subprocess
for i in range(1,101):
    subprocess.call([f"touch",f"{i}.py"])