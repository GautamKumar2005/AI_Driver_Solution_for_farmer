import sys
import json

def retrieve_data(data_type):
    # Dummy implementation of offline data retrieval
    data = {
        'crop_data': [
            {'name': 'Wheat', 'yield': 100, 'health': 'Good'},
            {'name': 'Corn', 'yield': 150, 'health': 'Fair'},
        ],
        'pest_data': [
            {'name': 'Aphids', 'infestation_level': 'High'},
            {'name': 'Caterpillars', 'infestation_level': 'Low'},
        ]
    }
    return data.get(data_type, 'Data type not found')

if __name__ == '__main__':
    data_type = sys.argv[1]
    result = retrieve_data(data_type)
    print(json.dumps(result))
