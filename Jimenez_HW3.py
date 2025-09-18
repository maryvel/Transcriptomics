import pandas as pd
import os

'''
INSERT CODE HERE
Homework 3.A
(i) Merge the 5 normal CSV files together and the 5 tumor CSV files, 
result should 2 separate Dataframes, one with Normal variants and another with Tumor variants.

SUGGESTION: Prior to coding, create 2 empty folders, Normal_CSV and Tumor_CSV, 
manually move the 5 normal CSVs into the Normal_CSV folder, and then move
the 5 tumor CSVs into the Tumor_CSV folder, this can be done 
by using the search bar in the Finder(Mac) or Folder(Windows) app. 
The script can then point to the directory (similar to HW1) to read and merge the files within, 
using a function within the pandas (pd) package.

Reading in a CSV file Example:
DataFrame1 = pd.read_csv("DataFrame1.csv")

Merging Example:
newDataFrame = pd.concat(DataFrame1, DataFrame2, axis=0) 
'''

print("========== create normal and tumor folders ========\n")
path = r"C:\Users\Maria\Documents\Bioinformatics_Maria\Classes_Fall_2025\Postgenomics\HWS\Lab3"
 

all_files = []

path_normal = os.path.join(path, "Normal_CSV")
path_tumor = os.path.join(path, "Tumor_CSV")

# create the folder if it does not exists
if not os.path.exists(path_normal):
    os.makedirs(path_normal)  # Creates the folder
    print(f"Folder '{path_normal}' created.")
else:
    print(f"Folder '{path_normal}' already exists.")
    
if not os.path.exists(path_tumor):
    os.makedirs(path_tumor)  # Creates the folder
    print(f"Folder '{path_tumor}' created.")
else:
    print(f"Folder '{path_tumor}' already exists.")
    
    

directory = os.path.join(path, "files")

    # List everything in the folder (files + subfolders)
all_files = os.listdir(directory) 
normal_csv = [f for f in all_files if f.endswith("_normal.csv")]
tumor_csv = [f for f in all_files if f.endswith("_tumor.csv")]


print("shape per normal file")

for item in normal_csv:
    src_path = os.path.join(path, "files", item)
    
    temp = pd.read_csv(src_path)
    print(temp.shape)
    
    dst_path = os.path.join(path_normal, item)   

    with open(src_path, "rb") as src_file:   # open source in binary mode
       with open(dst_path, "wb") as dst_file:  # open destination in binary mode
           dst_file.write(src_file.read())
           
print("shape per tumor file")

for item in tumor_csv:
    src_path = os.path.join(path, "files", item)
    temp = pd.read_csv(src_path)
    print(temp.shape)
    
    dst_path = os.path.join(path_tumor, item)   

    with open(src_path, "rb") as src_file:   # open source in binary mode
       with open(dst_path, "wb") as dst_file:  # open destination in binary mode
           dst_file.write(src_file.read())
    
def merging_files(folder, type_file):
    # Reading in a CSV file Example:
    # DataFrame1 = pd.read_csv("DataFrame1.csv")

    # Merging Example:
    # newDataFrame = pd.concat(DataFrame1, DataFrame2, axis=0) 
    all_files = os.listdir(folder) 

    
    
    
    # Read and combine
    dfs = [pd.read_csv( os.path.join(folder, file), index_col=None) for file in all_files]  # Read all files
    combined_df = pd.concat(dfs, ignore_index=True)  # Combine them into one big DataFrame
    if "Unnamed: 0" in combined_df.columns:
            combined_df = combined_df.drop(columns=["Unnamed: 0"])
        # print(df.head())
    
    # Save to a single CSV file
    combined_df.to_csv(os.path.join(folder,"combined_"+type_file+"_file.csv"), index=False)
    print(type_file+"_combined_file",  combined_df.shape)

    return combined_df

normal_combined = merging_files(path_normal, "normal")
tumor_combined = merging_files(path_tumor, "tumor")

# Function adds in alt_seq column to, input is a dataframe and function returns a dataframe
def addALT_Seq(csv):

    alt = []
    for row in range(csv.shape[0]):
        ref_seq = csv["ref_seq"][row]
        if ref_seq == csv["var_seq1"][row]:
            alt.append(csv["var_seq2"][row])
        else:
            alt.append(csv["var_seq1"][row])
    csv.insert(csv.shape[1], "alt_seq", alt)
    return csv



'''
INSERT CODE HERE
Homework 3.A
(ii) Using the output from A(i), run the addALT_Seq() function:
Example:
newDataFrame_withALTseq = addALT_Seq(NewDataFrame)
'''
normal_withALTseq = addALT_Seq(normal_combined)
tumor_withALTseq = addALT_Seq(tumor_combined)
# print(tumor_withALTseq.head())
# print(tumor_withALTseq.shape)

'''
INSERT CODE HERE
Homework 3.A
(iii) Using the output from A(ii), remove duplicates based on the given columns:
[“chrom”, “left”, “ref_seq”, “alt_seq”, “Patient_ID”]
Save the two DataFrames as: Final_Normal and Final_Tumor

Remove Duplicates Example:
Final = newDataFrame_withALTseq.drop_duplicates(columns)
'''
print("withALTSeq shape: ")
print(normal_withALTseq.shape)
print(tumor_withALTseq.shape)

columns_toRemove =  ["chrom", "left", "ref_seq", "alt_seq", "Patient_ID"]
Final_Normal = normal_withALTseq.drop_duplicates(columns_toRemove)
Final_Tumor = tumor_withALTseq.drop_duplicates(columns_toRemove)
print(Final_Normal.head())

'''
OUTPUT CHECK
Homework 3.A
(iv) Run the lines below:

print("The number of (Rows, Columns) in Tumor:")
print(Final_Tumor.shape)
print("The number of (Rows, Columns) in Normal:")
print(Final_Normal.shape)
'''
print("The number of (Rows, Columns) in Tumor:")
print(Final_Tumor.shape)
print("The number of (Rows, Columns) in Normal:")
print(Final_Normal.shape)


normal_path = os.path.join(path_normal, "Final_Normal.csv")
tumor_path = os.path.join(path_tumor, "Final_Tumor.csv")

Final_Normal.to_csv(normal_path, index=False)
Final_Tumor.to_csv(tumor_path, index=False)
