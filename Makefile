ruff :
	@echo "Running ruff..."
	ruff check --fix
	ruff format

.PHONY: tests
tests :
	@echo "Running tests..."
	export PYTHONPATH=src/movie_recommender  ;\
	echo $(PYTHONPATH) ;\
	pytest tests/

mr_data :
	@echo "Running src/movie_recommender/data.py..."
	python src/movie_recommender/data.py

mr_train :
	@echo "Running src/movie_recommender/train.py..."
	python src/movie_recommender/train.py
