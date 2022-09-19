# Ship2Ship Transfer Detection
Ship Overlap

<img src="https://github.com/databrickslabs/mosaic/raw/main/notebooks/examples/python/Ship2ShipTransfers/images/kepler_output.png" width=70%>

## Introduction
This is an algorithmic implementation to detect Ship to Ship transfers at scale using Databricks. It was presented at the [Data and AI Summit 2022](https://www.youtube.com/watch?v=XQNflqbgP7Q). 

This Mosaic example explores a novel, algorithmic approach to detecting Ship to Ship transfers at scale using AIS data. In particular it aims to surpass existing, naive implementations that are just based on a particular distance radius like the one shown below:

<img src="https://github.com/databrickslabs/mosaic/raw/main/notebooks/examples/python/Ship2ShipTransfers/images/naive_approach.png" width=50%>

Although the naive approach can be optimised with indices to be quite performant, additional improvements can be made. This is quite apparent if we look at the following data points below:

Naive Approach with buffers

<img src="https://github.com/databrickslabs/mosaic/raw/main/notebooks/examples/python/Ship2ShipTransfers/images/buffer_approach.png" >

According to our naive approach, where we buffer around our LAT/LONG points, the two vessels would not intersect. However, if we construct the actual path the vessels took, our algorithmic implementation would detect an overlap between the two paths, as shown below:

Path Line Strings approach

<img src="https://github.com/databrickslabs/mosaic/raw/main/notebooks/examples/python/Ship2ShipTransfers/images/linestring_approach.png" >

This model is expanded upon in the course of the attached notebooks. It shows how to ingest AIS data, how to process it at scale leveraging Mosaic in Databricks, and provides examples of how to extend the analysis to incorporate additional sources. 

*created by [@tiems90](https://github.com/tiems90)* 

| library                                | description             | license             | source                                              |
|----------------------------------------|-------------------------|---------------------|-----------------------------------------------------|
| mosaic                                 | library                 | Databricks License  | https://github.com/databrickslabs/mosaic            |

To run this accelerator, clone this repo into a Databricks workspace. Attach the RUNME notebook to any cluster running a DBR 11.0 or later runtime, and execute the notebook via Run-All. A multi-step-job describing the accelerator pipeline will be created, and the link will be provided. Execute the multi-step-job to see how the pipeline runs.

The job configuration is written in the RUNME notebook in json format. The cost associated with running the accelerator is the user's responsibility.
