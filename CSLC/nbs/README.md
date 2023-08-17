## Guide for running bulk processing with COMPASS

Below outlines how to generate OPERA CSLC products using COregistered Multi-temPorAl Sar Slc toolbox.

🚨 The COMPASS toolbox is still in **pre-alpha** stage and undergoing **rapid development**. 🚨

### Install

The following will install COMPASS into a conda environment. Using `mamba` to install the dependencies is a faster option compared to using `conda`.

1. Download source code:

```bash
git clone https://github.com/opera-adt/COMPASS.git
```
2. Create COMPASS conda environment:

First create and activate COMPASS conda environment.

```bash
mamba create -n COMPASS
conda activate COMPASS
```

Create a `conda_compass.sh` file. This file can be in a directory of conda setup scripts if you already have one. The file should be in this format:

```bash 
#!/bin/bash

module purge

conda deactivate
unset conda

source <path_to_conda_installation>/etc/profile.d/conda.sh
export PATH="<path_to_conda_installation>/bin:$PATH"

conda activate COMPASS

export CPL_ZIP_ENCODING="UTF-8"
```
Run `bash conda_compass.sh` to activate COMPASS environment

3. Install dependencies:

```bash
mamba install -c conda-forge --file COMPASS/requirements.txt
mamba install -c conda-forge isce3
python -m pip install git+https://github.com/opera-adt/s1-reader.git
```

4. Install `COMPASS` via pip:

```bash
python -m pip install ./COMPASS
```

### Usage

The following commands generate coregistered SLC in radar or geo-coordinates from terminal:

```bash
s1_cslc.py --grid geo   <path to s1_cslc_geo   yaml file>
s1_cslc.py --grid radar <path to s1_cslc_radar yaml file for reference burst>
s1_cslc.py --grid radar <path to s1_cslc_radar yaml file for secondary burst>
```

The command below will generate a stack of coregistered SLCs.

```bash
s1_geocode_stack.py -s <path_to_SLCs> -d <path_to_DEM> --burst-db-file <path_to_db_file>  --burst-id <S!_bust_ID> -w <path_to_working_dir> --metadata
```
will generate run_files sub dir in stack dir

from Mary Grace Bato to Everyone:    2:09  PM
for f in `ls *.sh`; do echo "sh $f" >> run_all.sh; done
 . run_all.sh











### License
**Copyright (c) 2021** California Institute of Technology (“Caltech”). U.S. Government
sponsorship acknowledged.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided
that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this list of conditions and
the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.
* Neither the name of Caltech nor its operating division, the Jet Propulsion Laboratory, nor the
names of its contributors may be used to endorse or promote products derived from this software
without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
