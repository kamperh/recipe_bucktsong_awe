Unsupervised Acoustic Word Embeddings on Buckeye English and NCHLT Xitsonga
===========================================================================

Overview
--------
**Note:** An updated version of this recipe is available at
https://github.com/kamperh/recipe_bucktsong_awe_py3. This updated recipe is
implemented in Python 3 (instead of Python 2.7) and uses LibROSA for feature
extraction (instead of HTK).

Unsupervised acoustic word embedding (AWE) approaches are implemented and
evaluated on the Buckeye English and NCHLT Xitsonga speech datasets. The
experiments are described in:

- H. Kamper, "Truly unsupervised acoustic word embeddings using weak top-down
  constraints in encoder-decoder models," in *Proc. ICASSP*, 2019.
  [[arXiv](https://arxiv.org/abs/1811.00403)]

Please cite this paper if you use the code.


Disclaimer
----------
The code provided here is not pretty. But I believe that research should be
reproducible. I provide no guarantees with the code, but please let me know if
you have any problems, find bugs or have general comments.


Datasets
--------
Portions of the Buckeye English and NCHLT Xitsonga corpora are used. The whole
Buckeye corpus will be required to execute the steps here, and the portion of
the NCHLT data. These can be downloaded from:

- Buckeye corpus:
  [buckeyecorpus.osu.edu](http://buckeyecorpus.osu.edu/)
- NCHLT Xitsonga portion:
  [www.zerospeech.com](http://www.lscp.net/persons/dupoux/bootphon/zerospeech2014/website/page_4.html).
  This requires registration for the challenge.

From the complete Buckeye corpus we split off several subsets. The most
important are the sets labelled as `devpart1` and `zs` in the code here. These
sets respectively correspond to `English1` and `English2` in [Kamper et al.,
2016](http://arxiv.org/abs/1606.06950), so see the paper for more details. More
details of which speakers are found in which set is also given at the end of
[features/readme.md](features/readme.md). We use the entire Xitsonga dataset
provided as part of the Zero Speech Challenge 2015 (this is already a subset of
the NCHLT data).

Download all these datasets beforehand. These can be stored apart from the
code.


Clone the repository
--------------------
Clone the repository by running:

    git clone https://github.com/kamperh/bucktsong_awe

Move into the repository directory:

    cd bucktsong_awe


Docker
------
This recipe comes with Dockerfiles which can be used to build images containing
all of the required dependencies. This recipe can be completed without using
Docker, but using the image makes it easier to resolve dependencies. To use the
docker image you need to first:

- Install [Docker](https://docs.docker.com/install/) and follow the [post
  installation
  steps](https://docs.docker.com/install/linux/linux-postinstall/).
- Install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker).

The one dependency for building the image is [HTK](http://htk.eng.cam.ac.uk/).
Download the file `HTK-3.4.1.tar.gz` from their website and copy this into the
`docker` directory.

Then, to build a docker image, run the following:

    cd docker
    docker build -f Dockerfile.gpu -t tf-htk .
    cd ..

All the rest of the steps can be run in a container in interactive mode. You
will need to mount the dataset directories. To run the container in interactive
mode with the mounted directories, run:

    docker run --runtime=nvidia \
        -v /r2d2/backup/endgame/datasets/buckeye:/data/buckeye \
        -v /r2d2/backup/endgame/datasets/zrsc2015/xitsonga_wavs:/data/xitsonga_wavs \
        -v "$(pwd)":/home -it -p 8887:8887 tf-htk

Alternatively, simply run `./docker.sh`, which executes the above command and
starts an interactive container.


Preliminaries
-------------
If you are not using the docker image, install all the standalone dependencies
(see Dependencies section below). Then follow the steps here. The docker image
includes all these dependencies and GitHub repositories.

Clone the required GitHub repositories into `../src/` as follows:

    mkdir ../src/  # not necessary using docker
    git clone https://github.com/kamperh/speech_dtw.git ../src/speech_dtw/

Build the `speech_dtw` tools by running:

    cd ../src/speech_dtw
    make
    make test
    cd -

For `speech_dtw` you need to run `make` to build. Unit tests can be performed
by running `make test`. See the readmes for more details.


Testing
-------
In the root project directory, run `make test` to run unit tests.


Feature extraction
------------------
Update the paths in `paths.py`. If you are using docker, this file should
already contain the mounted directories. Extract filterbank and MFCC features
moving to the directory (`cd features`) and then running the steps in
[features/readme.md](features/readme.md).


Frame-level same-different evaluation
-------------------------------------
To perform frame-level same-different evaluation based on dynamic time warping
(DTW), follow the steps in [samediff/readme.md](samediff/readme.md).


Downsampled acoustic word embeddings
------------------------------------
Extract and evaluate downsampled acoustic word embeddings by running the steps
in [downsample/readme.md](downsample/readme.md).


Neural acoustic word embeddings
-------------------------------
Train and evaluate encoder-decoder recurrent neural network acoustic word
embedding methods by running the steps in
[embeddings/readme.md](embeddings/readme.md).


Notebooks
---------
Some example notebooks are given in the `notebooks/` directory. Not that these
were used mainly during development, so they are not completely refined. A
docker container can be used to launch a notebook session by running
`./docker_notebook.sh` and then opening http://localhost:8889/.


Dependencies
------------
Standalone packages:

- [Python 2.7](https://www.python.org/)
- [NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/)
- [HTK](http://htk.eng.cam.ac.uk/): Used for MFCC feature extraction.
- [TensorFlow](https://www.tensorflow.org/)

Repositories from GitHub:

- [speech_dtw](https://github.com/kamperh/speech_dtw/): Used for same-different
  evaluation.  Should be cloned into the directory `../src/speech_dtw/`, as
  done in the Preliminary section above.

All of these dependencies are packaged in the docker images.


License
-------
The code is distributed under the Creative Commons Attribution-ShareAlike
license ([CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)).
