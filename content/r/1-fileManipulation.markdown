+++
title = "Common file manipulations in R"
date = 2019-12-21
toc = true  # Show table of contents? true/false
type = "docs"  # Do not modify.
[menu.r]
    # parent = "blog"
    weight = 2
+++



## Motivation

Parfois il n'est pas pratique de switcher a Terminal pour faire quelques manipulations de base, R nous fournit quelques fonctions pratiques pour faire ce type d'operations sans deranger le workflow.


## répertoire info/directory


```r
# get current working directory
getwd()

# set working directory
setwd("")

# new directory
dir.create("new_folder")

# delete a directory -- must add recursive = TRUE
unlink("some_directory", recursive = TRUE)
sapply(paste0("file", 1:100, ".txt"), unlink)

# get dir info
dirname("C:/path/to/file.txt")
```

## fichiers/files


```r
# run R code
sys.source("")
# create file
file.create("")
# create and open in the edit window
file.edit("")
# create 100 files on a fly
sapply(paste0("file", 1:100, ".txt"), file.create)
# copy or move a file
file.copy("source_file.txt", "destination_folder")
library(filesstrings)
file.move("C:/path/to/file/some_file.txt", "C:/some/other/path")
# delete a file
unlink("some_file.csv")
# delete file
file.remove("some_other_file.csv")
# list files
list.files()
list.files("another directory")
# all files
list.files("", recursive = TRUE)
list.files(pattern = ".csv")
# get file info
basename("C:/path/to/file.txt")
library(tools)
file_ext("C:/path/to/file.txt") # returns "txt"
file_ext("C:/path/to/file.csv") # returns "csv"

# use shell.exec to open file in extern window...
shell.exec("C:/path/to/file/some_file.txt")
# or file.show to launch a file
file.show("C:/path/to/file/some_file.txt")

# check if a file exists
file.exists("C:/path/to/file/some_file.txt")

# check if a folder exists
file.exists("C:/path/to/file/some_folder")

# alternatively, check if a folder exists with dir.exists
dir.exists("C:/path/to/file/some_folder")
# open a window to chosse file
file.choose()
```


## variables, batch processing


```r
# read in all the CSV files
all_data_frames <- lapply(list.files(pattern = ".csv"), read.csv)
# stack all data frames together
single_data_frame <- Reduce(rbind, all_data_frames)
```

## références/references

http://theautomatic.net/2018/07/11/manipulate-files-r/
https://www.datanovia.com/en/blog/how-to-easily-manipulate-files-and-directories-in-r/ for some advanced manipulations
https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/files for symbolic link etc.
