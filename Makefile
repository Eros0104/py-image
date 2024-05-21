PYTHON = python3

MAIN = ./src/main.py

DEFAULT_IMAGE_PATH = ./example/monkey.png

OUTPUT = ./example/output

run-all: run-gaussian run-median run-canny run-fourier-low run-fourier-high run-fourier-band run-noise-gaussian run-noise-salt-pepper run-multiple-filters run-multiple-filter-2

run-gaussian:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --blur gaussian --kernel 15 --output $(OUTPUT)/blur-gaussian.png
	@echo "Applied Gaussian blur filter on $(DEFAULT_IMAGE_PATH) with kernel size 15"

run-median:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --blur median --kernel 15 --output $(OUTPUT)/blur-median.png
	@echo "Applied Median blur filter on $(DEFAULT_IMAGE_PATH) with kernel size 15"

run-canny:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --edge canny --output $(OUTPUT)/edge-canny.png
	@echo "Applied Canny edge detection on $(DEFAULT_IMAGE_PATH)"

run-fourier-low:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --fourier low --output $(OUTPUT)/fourier-low.png
	@echo "Applied Low-pass filter on $(DEFAULT_IMAGE_PATH) using Fourier Transform"

run-fourier-high:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --fourier high --output $(OUTPUT)/fourier-high.png
	@echo "Applied High-pass filter on $(DEFAULT_IMAGE_PATH) using Fourier Transform"

run-fourier-band:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --fourier band --output $(OUTPUT)/fourier-band.png
	@echo "Applied Band-pass filter on $(DEFAULT_IMAGE_PATH) using Fourier Transform"

run-noise-gaussian:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --noise gaussian --mean 20 --stddev 20 --output $(OUTPUT)/noise-gaussian.png
	@echo "Applied Gaussian noise on $(DEFAULT_IMAGE_PATH)"

run-noise-salt-pepper:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --noise salt_pepper --output $(OUTPUT)/noise-salt-pepper.png
	@echo "Applied Salt and Pepper noise on $(DEFAULT_IMAGE_PATH)"

run-multiple-filters:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --blur median --kernel 25 --fourier low --output $(OUTPUT)/multiple-filters.png
	@echo "Applied Gaussian blur and Low-pass filter on $(DEFAULT_IMAGE_PATH)"

run-multiple-filter-2:
	@$(PYTHON) $(MAIN) --path $(DEFAULT_IMAGE_PATH) --noise salt_pepper --pepper_prob 0.5 --fourier low --output $(OUTPUT)/multiple-filters-2.png
	@echo "Applied Salt and Pepper noise and Low-pass filter on $(DEFAULT_IMAGE_PATH)"