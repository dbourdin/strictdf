# StrictDataFrame
This repo contains the implementation of a `StrictDataFrame`.

A `StrictDataFrame` will be created by parsing an existing pandas `DataFrame`,
and it will convert mixed columns to whatever value has more occurrences within
that column.

In order to build the `strictdf` dependency you can build the provided
Dockerfile that will generate the `.whl` file, and copy and install the
dependency into a new container, running a jupyter notebook, showing the usage
of the `StrictDataFrame`.

The jupyter notebook container will also have a `coverage` directory with the
results of the test suite execution.

## Building the docker image
You can build the docker image using the provided Dockerfile:
```
$ docker build . -t strictdf
```

## Running the container
To run the container you'll need to map the port used by the jupyter notebook
server to be able to access from the host network.
```
$ docker run --rm -ti -p8888:8888 strictdf
```
You might also want to keep the changes that you do to the notebook. In order
to do so, you might want to set a volume.
```
$ docker run --rm -ti -p8888:8888 --volume=/path/to/project/dir/strictdf/jupyter/notebook/:/tmp/notebook strictdf
```
It's also posible to map use a volume to keep changes performed on the csv
dataset.
```
$ docker run --rm -ti -p8888:8888 --volume=/path/to/project/dir/strictdf/jupyter/data/:/tmp/data strictdf
```

After running the container, just open the provided url in your browser.
