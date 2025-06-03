# Using this script run Terraform Command One by One Automatically...

import subprocess #This imports Python’s built-in module `subprocess`, which is used to run external shell commands (like Terraform CLI commands) from within Python.


def terraform_run(command, step_name):
    try:
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(process.stdout.decode())
        print(f"{step_name} completed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error during {step_name}:")
        print(e.stderr.decode())
        exit(1)

directory = "/home/tuhin/Documents/VS Code_Code/TS_Python/terraform2/code"

# Step 1: Init
terraform_run(f'terraform -chdir="{directory}" init', "Terraform Init")

# Step 2: Plan
terraform_run(f'terraform -chdir="{directory}" plan', "Terraform Plan")

# Step 3: Apply
terraform_run(f'terraform -chdir="{directory}" apply -auto-approve', "Terraform Apply")


