import yaml
import os

def get_config():
	current_path = os.path.dirname(os.path.abspath(__file__))
	with open(current_path + '/../' + 'config.yml', 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
	return cfg