# Databricks notebook source
# MAGIC %md This notebook sets up the companion cluster(s) to run the solution accelerator. It also creates the Workflow to create a Workflow DAG and illustrate the order of execution. Feel free to interactively run notebooks with the cluster or to run the Workflow to see how this solution accelerator executes. Happy exploring!
# MAGIC 
# MAGIC The pipelines, workflows and clusters created in this script are user-specific, so you can alter the workflow and cluster via UI without affecting other users. Running this script again after modification resets them.
# MAGIC 
# MAGIC **Note**: If the job execution fails, please confirm that you have set up other environment dependencies as specified in the accelerator notebooks. Accelerators sometimes require the user to set up additional cloud infra or data access, for instance. 

# COMMAND ----------

# DBTITLE 0,Install util packages
# MAGIC %pip install git+https://github.com/databricks-academy/dbacademy-rest git+https://github.com/databricks-academy/dbacademy-gems git+https://github.com/databricks-industry-solutions/notebook-solution-companion

# COMMAND ----------

from solacc.companion import NotebookSolutionCompanion

# COMMAND ----------

job_json = {
        "timeout_seconds": 7200,
        "max_concurrent_runs": 1,
        "tags": {
            "usage": "solacc_testing",
            "group": "MFG"
        },
        "tasks": [
        {
            "job_cluster_key": "ship2ship_cluster",
            "libraries": [],
            "notebook_task": {
                "notebook_path": f"00_README"
            },
            "task_key": "ship2ship_00",
            "description": ""
        },
        {
            "job_cluster_key": "ship2ship_cluster",
            "notebook_task": {
                "notebook_path": f"01_Data Prep"
            },
            "task_key": "ship2ship_01",
            "depends_on": [
                {
                    "task_key": "ship2ship_00"
                }
            ]
        },
        {
            "job_cluster_key": "ship2ship_cluster",
            "notebook_task": {
                "notebook_path": f"02_Data Ingestion",
                "base_parameters": {
                    "holdout days": "90"
                }
            },
            "task_key": "ship2ship_02",
            "depends_on": [
                {
                    "task_key": "ship2ship_01"
                }
            ]
        },
        {
            "job_cluster_key": "ship2ship_cluster",
            "notebook_task": {
                "notebook_path": f"03a_Overlap Detection"
            },
            "task_key": "ship2ship_03a",
            "depends_on": [
                {
                    "task_key": "ship2ship_02"
                }
            ]
        },
        {
            "job_cluster_key": "ship2ship_cluster",
            "notebook_task": {
                "notebook_path": f"03b_Advanced Overlap Detection"
            },
            "task_key": "ship2ship_03b",
            "depends_on": [
                {
                    "task_key": "ship2ship_02"
                }
            ]
        }
    ],
        "job_clusters": [
            {
                "job_cluster_key": "ship2ship_cluster",
                "new_cluster": {
                    "spark_version": "10.4.x-cpu-ml-scala2.12",
                "spark_conf": {
                    "spark.databricks.delta.formatCheck.enabled": "false"
                    },
                    "num_workers": 8,
                    "node_type_id": {"AWS": "i3.xlarge", "MSA": "Standard_D3_v2", "GCP": "n1-highmem-4"},
                    "custom_tags": {
                        "usage": "solacc_testing"
                    },
                }
            }
        ]
    }

# COMMAND ----------

dbutils.widgets.dropdown("run_job", "False", ["True", "False"])
run_job = dbutils.widgets.get("run_job") == "True"
NotebookSolutionCompanion().deploy_compute(job_json, run_job=run_job)

# COMMAND ----------


