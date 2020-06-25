### Reading results
The actual results from experimentation can be viewed from ```cyber_analytics_assessment.pdf```.

To analysis completed notebook, visit the ```~/archived``` folder. Else, to re-create results, go to 'Getting started'
```
.archived
+--datasets_*.tar.gz                   ## *.tar.gz files contains all the original, extracted and re-engineered datasets. Unzip these files before running the notebook
+--analytics.ipynb                     ## Jupyter Notebook containing all original outputs. Running of notebook will require re-creating the steps from 'Getting started'
+--cyber_analytics_assessment.pdf      ## The notebook outputs were saved as PDF for simple viewing


## To unzip all dataset files
cat *.tar.gz | tar zxvf - -i
gunzip -k http.log.gz
```

### Getting started
This was completed using python3 libraries on Jupyter Notebook. User will need to have Anaconda Prompt to re-create results.
```
## open Anaconda prompt
## once in ~/analytics_developemnt create the conda environment with required dependencies
conda create --name <env>
gunzip -k http.log.gz

## install required conda libraries
conda install -c anaconda pandas
conda install -c anaconda numpy
conda install -c jmcmurray os
conda install -c intel scikit-learn
conda install -c lightsource2-tag collection

jupyter notebook
```
