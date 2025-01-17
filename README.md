<pre>
========================================================

   ________________  ___         ________             
  / ____/ ____/ __ \/   |       / ____/ /___ _      __
 / /   / / __/ /_/ / /| |______/ /_  / / __ \ | /| / /
/ /___/ /_/ / _, _/ ___ /_____/ __/ / / /_/ / |/ |/ / 
\____/\____/_/ |_/_/  |_|    /_/   /_/\____/|__/|__/  
                                                      

========================================================
</pre>
[![Github Action](https://github.com/tancheng/CGRA-Flow/actions/workflows/main.yml/badge.svg)](https://github.com/tancheng/CGRA-Flow/actions/workflows/main.yml)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

CGRA-Flow is an integrated framework for CGRA compilation, exploration, synthesis, and development.

User Interface Snapshot/Demo
--------------------------------------------------------------------------
![Capture](https://user-images.githubusercontent.com/6756658/213010564-fa74b34e-218f-435e-9e8e-ef5a40f8899d.PNG)

A demo at repl.it (https://repl.it/@ChengTan/cgra-flow) shows some features of CGRA-Flow (the verilog generation and evaluation are not available due to *repl.it*'s limited support of python environment). To explore all the features, please setup CGRA-Flow locally or leverage the docker image.

Docker
--------------------------------------------------------
The docker image is available [here](https://hub.docker.com/layers/cgra/cgra-flow/demo/images/sha256-7ca327d24f555376d91cba6fa30e3fbaa4a4c0d4053a82ac9059c374a3dee5bd?context=repo).

As CGRA-Flow requires GUI, a script is provided for setting up the display:
```sh
 docker pull cgra/cgra-flow:demo

 # if this is your first time establishing a container for CGRA-Flow:
 sh ./run_docker.sh
 # else, use the following command to reopen the same container: 
 sh ./start_docker.sh

 # Don't forget to activate the python virtual environment once you are in the container:
 source /WORK_REPO/venv/bin/activate
```
Otherwise, if you don't need the GUI, development can be performed in the container with the environment well set up:
```sh
 docker pull cgra/cgra-flow:demo
 docker run -it cgra/cgra-flow:demo
 source /WORK_REPO/venv/bin/activate
```

Execution
--------------------------------------------------------
```sh
 mkdir build && cd build
 python ../launchUI.py
```

Installation
--------------------------------------------------------

CGRA-Flow requires Python3.7.

Refer to the build [scripts](https://github.com/tancheng/CGRA-Flow/blob/master/.github/workflows/main.yml) or look into specific repo for the manual installation if you don't want to use docker.


Citation
--------------------------------------------------------------------------
```
@inproceedings{tan2020opencgra,
  title={OpenCGRA: An open-source unified framework for modeling, testing, and evaluating CGRAs},
  author={Tan, Cheng and Xie, Chenhao and Li, Ang and Barker, Kevin J and Tumeo, Antonino},
  booktitle={2020 IEEE 38th International Conference on Computer Design (ICCD)},
  pages={381--388},
  year={2020},
  organization={IEEE}
}
```

Publications leveraging (parts of) CGRA-Flow toolchain
--------------------------------------------------------------------------
- _"MESA: Microarchitecture Extensions for Spatial Architecture Generation."_ ISCA'23.
- _"An Architecture Interface and Offload Model for Low-Overhead, Near-Data, Distributed Accelerators."_ MICRO'22.
- _"MATCHA: A Fast and Energy-Efficient Accelerator for Fully Homomorphic Encryption over the Torus."_ DAC'22.
- _"DRIPS: Dynamic Rebalancing of Pipelined Streaming Applications on CGRAs."_ HPCA'22.
- _"ARENA: Asynchronous Reconfigurable Accelerator Ring to Enable Data-Centric Parallel Computing."_ TPDS'21.
- _"Ultra-Elastic CGRAs for Irregular Loop Specialization."_ HPCA'21.



License
--------------------------------------------------------------------------

CGRA-Flow is offered under the terms of the Open Source Initiative BSD 3-Clause License. More information about this license can be found here:

  - http://choosealicense.com/licenses/bsd-3-clause
  - http://opensource.org/licenses/BSD-3-Clause
