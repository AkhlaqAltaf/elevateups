#!/bin/bash

# Step 1: Update the server
sudo apt update
sudo apt upgrade -y

# Step 2: Install necessary packages (if not already installed)
sudo apt install -y python3-pip python3-dev libpq-dev nginx

# Step 3: Navigate to project directory
cd /root/elevateups

# Step 4: Install Python dependencies
pip install -r requirements.txt

# Step 5: Collect static files
python manage.py collectstatic --noinput --settings=elevators.production_settings

# Step 6: Apply migrations
python manage.py migrate --settings=elevators.production_settings

# Step 7: Copy Nginx config and restart Nginx
sudo cp nginx/escalators.tech /etc/nginx/sites-available/escalators.tech
sudo ln -s /etc/nginx/sites-available/escalators.tech /etc/nginx/sites-enabled/
sudo systemctl restart nginx

# Step 8: Run Gunicorn
./run_gunicorn.sh

# Restart services to apply changes
sudo systemctl restart nginx
