# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
US = dataiku.Dataset("US")
US_df = US.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_output_df = US_df # For this sample code, simply copy input to output


# Write recipe outputs
python_output = dataiku.Dataset("python_output")
python_output.write_with_schema(python_output_df)