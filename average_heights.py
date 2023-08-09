# -*- coding: utf-8 -*-
import pandas as pd
import csv

with open(r"C:/Users/franc/OneDrive/Documentos/entdados.dat") as file:
    dp_lines = [line.strip() for line in file if line.startswith("DP")]
    
for line in dp_lines:
    print(line)
    
with open("output.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["DP Lines"]) 
    writer.writerows([[line] for line in dp_lines])