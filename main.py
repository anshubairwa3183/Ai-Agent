import subprocess
import re
from ai_engine import generate_plan  #import the Ai plan generator function

def extract_code_block(plan):
    #Extracts the Python code block from the AI's response
    match = re.search(r"```python(.*?)```", plan, re.DOTALL)
    return match.group(1).strip() if match else None

def execute_python_script(code, filename="generated_script.py"):
    print(f"Writing code to {filename}...")
    with open(filename, "w") as f:
        f.write(code)
    
    try:
        print(f"Running {filename}...")
        result = subprocess.run(["python", filename], capture_output=True, text=True)
        print("📤 Output:")
        print(result.stdout)  #Show the output from running the script
        if result.stderr:
            print("⚠️ Errors:")
            print(result.stderr)  #Show any errors if they occur
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        return False

def main():
    print("📝 What task should I do?")
    task = input()  #Take task input from the user

    if not task:
        print("❌ No task entered. Exiting.")
        return

    print(f"\nYou entered task: {task}")
    
    #Generate the plan for the task using the AI engine
    plan = generate_plan(task)

    #If no plan returned, exit
    if not plan:
        print("❌ No plan generated. Exiting.")
        return
    
    print("\n📋 Proposed Plan:\n")
    print(plan)

    #Ask user for approval of the plan
    approve = input("\n✅ Approve this plan? (y/n): ").lower()

    if approve != 'y':
        print("❌ Plan not approved. Exiting.")
        return

    print("\n🚀 Executing...")

    #Extract the code from the plan
    code = extract_code_block(plan)

    if code:
        print("🔧 Code extracted, running...")
        success = execute_python_script(code)
    else:
        print("❌ No code found to execute.")
        success = False

    #Ask the user if the task was successful
    was_successful = success and input("\n✅ Was the task successful? (y/n): ").lower() == "y"

    if was_successful:
        print("🎉 Done!")
    else:
        print("🔁 Let’s refine and retry (feature coming next!)")

if __name__ == "__main__":
    main()
