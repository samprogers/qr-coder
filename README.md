# qr-coder
Basic website to generate free QR codes

# Local Dev Setup
Setting up the project is pretty minimal. Steps include:

1. Build docker imagee `docker-compose up --build -d`
2. Start local development server `docker exec -it qr-coder ./bin/start.sh`
3. Add hosts enntry to /etc/hosts otherwise use 0.0.0.0
`127.0.0.1 snyk.site qr-coder.site`
4. Navigate to http://qr-coder.site:8000/ in your browser

# Testing
Run the following command `docker exec -it qr-coder poetry run pytest`

# CI/CD
- All commits to this project will run through the pytest test suite. Tests can be added/modified in the tests directory
- All merges into main needs to approved by the maintainer
- CD will kick off after merges here: https://github.com/samprogers/qr-coder/actions/workflows/cd.yaml
