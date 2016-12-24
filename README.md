# Hadoop Ecosystem Programming Practise
> An early **hands-on** guide to Hadoop Ecosystem  

## Overview

Repository as the name suggests contains, the variety of *Hadoop Ecosystem* framework components, keeping in mind the *big data analytics students & and naive data engineers*. 

Programming implementations are done using *java* and *python* (depends upon the ease of using the underlying framework component), by keeping in mind the aspect of *modularity* and *readability*.

## Usage

The developed programs belong to the hadoop ecosystem components like *hdfs*, *mapreduce*, *hbase*, and *spark* etc. A few of them gives fair idea of using different components (with the probable choice of languages like spark with pyspark or hbase with java API) depends upon the choice of operation and workload.

Programs represent a control flow as:

    Input file -> Parsing -> Applying chosen option -> Console output 


Programs are named to represent an intuitive understanding about themselves, and are kept in the related directories (Vig. *BST* contains program for *Binary-Search-Tree*). Additionaly supplied InputFile helps verifying the output. 

For example, the *BST* directory contains the following files:
                  
    BST.h
    BST.c
    InputFile

And Std instruction (unless mentioned otherwise) to run the above mentioned program (after compiling it using *gcc*) is as follows:

    ./a.out InputFile

**Note:** All programs except *spell-checker* are done tested successfully. There might be failure due to Big Input file (Scalability has not been tested yet).

## Conclusion

I am progressing to add more informatory files (vig. *README*) regarding input and operations used in programs. 

Since these programs are tested with a small set of input, hence are not claimed to be run on a complex/compute intensive input. And mostly developed to give an early lessons for beginners.


*Waiting to hear feedback/concerns.*
 
 
_Paritosh *( Parit )*
