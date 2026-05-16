# reset_and_setup.ps1
Write-Host "Starting Database Reset and Setup..." -ForegroundColor Green

# Navigate to backend
cd "D:\project\Nexora Frontend\expense_tracker_backend"

# Activate venv
.\venv\Scripts\Activate.ps1

# Delete database
if (Test-Path db.sqlite3) {
    Remove-Item -Force db.sqlite3
    Write-Host "Deleted old database" -ForegroundColor Yellow
}

# Delete migrations
if (Test-Path api\migrations) {
    Remove-Item -Recurse -Force api\migrations
    Write-Host "Deleted old migrations" -ForegroundColor Yellow
}

# Create new migrations folder
New-Item -ItemType Directory -Path api\migrations -Force
New-Item -ItemType File -Path api\migrations\__init__.py -Force

# Create migrations
Write-Host "Creating migrations..." -ForegroundColor Green
python manage.py makemigrations api

# Apply migrations
Write-Host "Applying migrations..." -ForegroundColor Green
python manage.py migrate

# Create superuser
Write-Host "Creating superuser..." -ForegroundColor Green
python manage.py createsuperuser

Write-Host "Setup complete!" -ForegroundColor Green