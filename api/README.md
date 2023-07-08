# ML API

This is an example of a deployed ML Model using the famous iris dataset. This example provides the user with the ability to `/train` a model as well as make `/predict` requests to the Flask REST API. It can be deployed locally and tested with the appropriate `just` commands.

## Prerequisites 

- `docker` [Install Link](https://docs.docker.com/engine/install/)

## Build

To build the image, run `just build`. This will create the Docker image. 

## Deployment

Run `just deploy` to run the container on the local machine.

## API Usage

The API offers two endpoints.

`/train` - This will train a KNearestNeighbors model on the Iris data set and dump the model locally.

`/predict` - The predict method expects a request body with `data` equal to a payload of 4 float values as the model input `data=<float, 4>`. The returned integer is the prediction of the flower.

Convinently there is a `just train` and `just predict` which utilizes `curl` to test the deployed container.

## References

[Reference to Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set)
