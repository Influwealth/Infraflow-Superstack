#!/bin/bash
echo "🔧 Preparing InfraFlow stack..."
export $(grep -v '^#' .env | xargs)
pip install -r requirements.txt
docker-compose pull
docker-compose up -d
echo "✅ InfraFlow is LIVE!"
