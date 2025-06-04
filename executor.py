import subprocess

def run_command(command):
    try:
        print(f"🛠 Running: {command}")
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print(f"⚠️ Error:\n{result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"Execution failed: {e}")
        return False
