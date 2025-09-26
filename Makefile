IMAGE_NAME := movie-review-app

# Build the Docker image
build:
	@echo "Building Docker image ${IMAGE_NAME}..."
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	@echo "Running Docker container from image ${IMAGE_NAME}..."
	docker run --rm -p 8501:8501 $(IMAGE_NAME)

# Stop and clean/remove the Docker container
clean:
	@echo "Stopping ${IMAGE_NAME} and removing container and image..."
	docker stop $(IMAGE_NAME)_container || true
	docker rmi $(IMAGE_NAME) || true