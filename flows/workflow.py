from prefect import flow, task, get_run_logger
import subprocess
import os

@task(log_prints=True)  # Ensures all prints are captured in logs
def run_task(script_name):
    logger = get_run_logger()
    
    # Define the full path to the script based on the project structure
    script_path = os.path.join(os.path.dirname(__file__), '../EdaAndPreprocessingTasks', script_name)
    
    try:
        # Run the external Python script using its full path
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        
        # Log both stdout and stderr
        if result.returncode == 0:
            logger.info(f"Successfully executed {script_name}:\n{result.stdout}")  # Log standard output
        else:
            logger.error(f"Error in {script_name}: {result.stderr}")  # Log standard error

        # Always print both stdout and stderr, regardless of success or failure
        print(result.stdout)
        print(result.stderr)

    except Exception as e:
        logger.error(f"Failed to execute {script_name}: {str(e)}")

    return 0

@flow
def main_flow():
    # Run tasks sequentially and capture the results
   data1 = run_task("BasicStats.py")
   data2 = run_task("Correlationcoefficient.py", wait_for=[data1])  
   data3 = run_task("Binning.py", wait_for=[data2]) 
   data4 = run_task("PearsonCorrelation.py", wait_for=[data3])
   data5 = run_task("FeatureImportance.py", wait_for=[data4])
   run_task("Visualization.py", wait_for=[data5])

# To run locally
if __name__ == "__main__":
    main_flow.serve(name="cardiovascular-ds-workflow",
                      tags=["cardiovascular datascience project workflow"],
                      parameters={},
                      interval=120)
