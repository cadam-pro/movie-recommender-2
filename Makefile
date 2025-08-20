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
