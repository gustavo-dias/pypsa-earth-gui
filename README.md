# PyPSA-Earth-GUI

> [!WARNING]
> This project is in early development. Expect eventual breaking changes and bugs.

An unofficial graphical user interface (GUI) for [PyPSA-Earth](https://github.com/pypsa-meets-earth/pypsa-earth). When fully developed, it will allow PyPSA-Earth users to:
1. Configure a model;
2. Solve it and;
3. Visualize the results.

**Development status: currently only step 1 is supported (as of 2026-07-05).**

## Installation

#### Linux (Performed on Ubuntu 24.04.4 LTS).

We assume there is a working installation of PyPSA-Earth and all its dependencies in the (local) machine. If not, [install](https://pypsa-earth.readthedocs.io/en/latest/index.html) it first. Then:

1. Clone the repo to disk:
    ```
    ~/path/to/installation/dir$ git clone https://github.com/gustavo-dias/pypsa-earth-gui.git
    ```
2. Navigate into the installation directory: 
    ```
    ~/path/to/installation/dir$ cd pypsa-earth-gui
    ```
3. Create the conda/mamba environment with the yaml file: 
    ```
    ~/path/to/installation/dir/pypsa-earth-gui$ conda env create -f ./envs/environment.yaml
    ```

## Usage

1. Activate the conda/mamba environment: 
    ```
    ~/path/to/installation/dir/pypsa-earth-gui$ conda activate pypsa-earth-gui
    ```
2. Run the application invoking streamlit:
    ```
    (pypsa-earth-gui) user@machine:~/path/to/installation/dir/pypsa-earth-gui$ streamlit run run.py
    ```

The app should open in one of the installed web-browsers.

## Contributing

We do not recommend openning PRs unless you are already directly involved with the development. Contact maintainers for details.

## License

AGPL-3.0-or-later.
