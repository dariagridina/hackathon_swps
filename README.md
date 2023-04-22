## Installation

### Create virtual environment
```bash
python3 -m venv venv
```

### Activate virtual environment
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
python manage.py migrate
```

### Collect static files
```bash
python manage.py collectstatic
```

### Load test data
```bash
python manage.py load_code_fixtures
```

### Run server
```bash
python manage.py runserver
```
