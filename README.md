# uv_template
python uv template 

# Setup Instructions
```bash
# Initialize virtual environment and install dependencies
make init
```

# Usage Instructions
```bash
# Run the application
make run
# Or directly using uv
uv run python main.py
```

# Development Instructions
```bash
# Run tests
make test

# Lint code 
make lint

# Format code
make format

# Generate documentation
make gdoc

# Sub entry point for development (tools)
uv run python -m tools.some_tool
```

# Project Structure
- Please check [developer guide](docs/CONTRIBUTING.md) for details on project structure and coding standards.
