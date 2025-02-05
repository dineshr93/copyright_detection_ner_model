b:
	echo "step:0 Running test_ner_model_from_dir.py ============================================="
	python get_training_data_from_scancode.py
	echo "step:1 Running prepare_ner.py ============================================="
	python prepare_ner_data.py
	echo "step:2 Running train_ner_model.py ============================================="
	python train_ner_model.py
	echo "step:3 Running test_ner_model.py ============================================="
	python test_ner_model.py