name: Hello GitHub Actions

on:
  push:
    branches: [ "main" ] # Only run on push to main branch
  pull_request:
    branches: [ "main" ] # Only run on pull requests targeting main branch

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install pytest
      run: pip install pytest
    - name: Run tests
      run: pytest
    - name: Run Hello Script
      run: python hello.py
