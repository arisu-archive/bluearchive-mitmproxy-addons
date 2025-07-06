# Contributing to Arisu Archive Mitmproxy Addons

Thank you for your interest in contributing to the Arisu Archive mitmproxy addons project! We welcome contributions from the community and appreciate your help in making this project better.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Creating Addons](#creating-addons)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [Documentation](#documentation)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and constructive in all interactions.

## How to Contribute

There are many ways to contribute to this project:

- 🐛 **Report bugs** and suggest improvements
- 📝 **Improve documentation** and add examples
- 🔧 **Develop new addons** for different use cases
- 🌍 **Translate** documentation to other languages
- 📊 **Share datasets** (with proper anonymization)
- 💬 **Help other users** in issues and discussions

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- mitmproxy 8.0+

### Setup Instructions

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/arisu-archive/bluearchive-mitmproxy-addons.git
   cd bluearchive-mitmproxy-addons
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Creating Addons

### Addon Structure

All addons should be placed in the `addons/` directory and follow this basic structure:

```python
"""
Brief description of what the addon does.
"""

import logging
from mitmproxy import http
from mitmproxy import ctx


class YourAddon:
    """Your addon class description."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def load(self, loader):
        """Load addon configuration options."""
        loader.add_option(
            name="your_option",
            typespec=str,
            default="default_value",
            help="Description of your option"
        )
    
    def request(self, flow: http.HTTPFlow) -> None:
        """Handle HTTP requests."""
        pass
    
    def response(self, flow: http.HTTPFlow) -> None:
        """Handle HTTP responses."""
        pass


# Required for mitmproxy to load the addon
addons = [YourAddon()]
```

### Addon Guidelines

1. **Name your addon descriptively** - Use clear, descriptive names
2. **Add proper documentation** - Include docstrings and comments
3. **Handle errors gracefully** - Don't crash on unexpected input
4. **Use logging appropriately** - Log important events and errors
5. **Make it configurable** - Add options for customization
6. **Respect user privacy** - Don't log sensitive information
7. **Test thoroughly** - Ensure your addon works with different scenarios

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_blue_archive.py

# Run with coverage
pytest --cov=addons
```

### Writing Tests

Create test files in the `tests/` directory with names like `test_your_addon.py`:

```python
import pytest
from addons.your_addon import YourAddon

def test_your_addon():
    addon = YourAddon()
    # Your test code here
    assert True
```

## Submitting Changes

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update the changelog** if applicable
5. **Create a pull request** with a clear title and description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or properly documented)
```

## Code Style

### Python Style Guide

- Follow **PEP 8** guidelines
- Use **type hints** where appropriate
- Add **docstrings** to all functions and classes
- Use **descriptive variable names**
- Keep **line length** under 100 characters
- Use **4 spaces** for indentation

### Code Formatting

We use `black` for code formatting:

```bash
# Format all Python files
black .

# Check formatting without changes
black --check .
```

### Linting

We use `flake8` for linting:

```bash
# Run linter
flake8 addons/ tests/

# Run with specific configuration
flake8 --max-line-length=100 addons/
```

### Type Checking

We use `mypy` for type checking:

```bash
# Run type checker
mypy addons/

# Run with specific configuration
mypy --strict addons/
```

## Documentation

### Documentation Guidelines

- Use **clear, concise language**
- Add **screenshots** for visual features
- Keep **documentation up to date** with code changes
- Use **proper markdown formatting**

### Documentation Structure

- `README.md` - Main project documentation
- `CONTRIBUTING.md` - This file
- `docs/` - Detailed documentation (if needed)
- Inline code comments for complex logic

## Getting Help

If you need help with contributing:

1. Check the [FAQ](README.md#faq) in the README
2. Search [existing issues](https://github.com/arisu-archive/mitmproxy-addon/issues)
3. Create a new issue with the "question" label

Thank you for contributing to the Arisu Archive mitmproxy addons project! 🎉 