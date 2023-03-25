APP_IMAGE_NAME := app
APP_TAG := 0.1.0
APP_PRIVATE_PORT := 8888
APP_PUBLIC_PORT := 8000


.PHONY: build run push

build:
	docker build --rm -t $(APP_IMAGE_NAME):$(APP_TAG) .

run:
	docker run --env-file .env -it -p $(APP_PUBLIC_PORT):$(APP_PRIVATE_PORT) $(APP_IMAGE_NAME):$(APP_TAG)

push:
	docker push $(APP_IMAGE_NAME):$(APP_TAG)

