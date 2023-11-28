import subprocess

# Execute o primeiro script
subprocess.run(["python", "./src/scripts/create_DB.py"])

# Execute o segundo script
subprocess.run(["python", "./src/scripts/create_records.py"])
