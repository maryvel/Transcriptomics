# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 21:57:11 2025

@author: Maria Jimenez Velasco
Course: Post-genomic

This code take csv file and extract basic transcriptomic information
"""
import pandas as pd
import os

path = r"C:\Users\Maria\Documents\Bioinformatics_Maria\Classes_Fall_2025\Postgenomics\HWS\Lab3\transcriptomics\transcriptomics"
 
file = os.path.join(path, "condition_Atrophic_vs_Control.csv")
df = pd.read_csv(file)
print(df.shape)

# Number of significant genes
num_sig = (df['padj'] < 0.05).sum()
print("\nNumber of significant genes (padj < 0.05)")
print(num_sig)

# Number of upregulated  genes
num_up =  (df['log2FoldChange'] > 0).sum()
print("number of upregulated genes")
print(num_up)

#  Number of downregulated  genes
num_down = ((df['log2FoldChange'] < 0)).sum()
print("number of downregulated genes")
print(num_down)

# Optional: get the genes themselves
# Count upregulated genes (log2FoldChange > 2)
upregulated = df[df['log2FoldChange'] > 2]
print("Upregulated genes (log2FC > 2):", len(upregulated))

# Count downregulated genes (log2FoldChange < -2)
downregulated = df[df['log2FoldChange'] < -2]
print("Downregulated genes (log2FC < -2):", len(downregulated))