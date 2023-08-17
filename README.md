# SPRINT-seq

SPRINTseq (Spatially Resolved and signal-diluted Next-generation Targeted sequencing) is an innovative in situ sequencing strategy that combines hybrid block coding and molecular dilution strategies, allowing an accurate RNA detection in crowded environment. This method can profile a mouse brain coronal slice within 1 day, and generate gene expression architecture in a sub-micron resolution.

For more information, please read the article.  [Chang et.al (2023) *bioRxiv*](https://doi.org/10.1101/2022.11.16.516714)

# Code Preview

Code for SPRINT-seq consists of four parts, **barcode_design**, **image_processing**, **gene_calling** and **cell_segmentation**. Data will be processed in this order.

# Start

To run this code, packages must be installed with command:

```shell
pip install -r requirements.txt
```

And MATLAB engine should be installed, you can follow [official guideline](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html).  

**Remind!** There are lots of paths or directories need to be edited in files mentioned below.

## Barcode Design

Code in this part will generate a suitable barcode space for you to choose. 

**Caution!** These codes may cost a lot of memory.

Step 1: Run `generate_graph.py`.  An in-between file will be generated.

Step 2: Run `MIS_variance_trail_qsub.py` using the in-between file as input. Suitable barcodes will be generated in a txt file.

## Image Processing

We have provided an example data, which path is $PATH.  

Step 1: Edit the directory in python file `scan_fstack.py` as the directory you wish. Run the code: 

```shell
python scan_fstack.py
```

Step 2: Edit the directory in python file `image_process_after_stack.py` the same as the directory before. Run the code: 

```shell
python image_proess_after_stack.py
```

Results will be large stitched images, which will be used in next part.

## Gene Calling

Step 1:  Before running code, a probe sequence file should be provided. It should be a csv file and formatted like:

```csv
Name,Padlock
Gene_name1,Padlock_sequence1
Gene_name2,Padlock_sequence2
...,...
Gene_nameN,Padlock_sequenceN
```

Step 2: Run the jupyter notebook file `generate_ref_files.ipynb`. A reference barcode book will be produced named `Your_Given_Name.csv`.

Step 3: Edit the directory in `Gene_calling.py` and run it. A csv file containing spots coordinate and gene name will be generated, named `mapped_genes.csv`.

## Cell Segmentation

Edit the directory in `segment.py` and run it. This code will segment cell nucleus according to DAPI channel. A csv file containing the coordinate of nucleus centroid will be generated.

