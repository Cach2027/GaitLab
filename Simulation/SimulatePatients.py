from gaitLabEnv import GaitEnv
import pandas as pd

# Create environment and load simulated patients
env = GaitEnv(data_file="Data/gait_lab_dataset.csv", train=False, use_dof_model=True)

# Save simulated patient data to a CSV file
simulated_df = env.df.copy()
simulated_df.to_csv("Data/simulated_patients.csv", index=False)

# Console output to confirm the process
print(f"✅ {len(simulated_df)} simulated patients saved to 'Data/simulated_patients.csv'")
print("📋 Preview of simulated data:")
print(simulated_df.head(5).to_string(index=False))
