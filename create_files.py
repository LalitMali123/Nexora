import os

# Create directories
directories = [
    'api/migrations',
    'media',
    'staticfiles',
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    # Create __init__.py in migrations folder if it doesn't exist
    if directory == 'api/migrations':
        init_file = os.path.join(directory, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('')