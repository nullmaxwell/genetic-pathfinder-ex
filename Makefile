clean:
	rm -rf src/*.pyc
	rm -rf src/__pycache__

run-15:
	make clean
	python3 main.py cities_15.txt city_milage_15.txt 1750 40

run-20:
	make clean
	python3 main.py cities_20.txt city_milage_20.txt 1750 40