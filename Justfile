# Variables
PACKAGE_NAME := "snowstorm_client"
GIT_REPO_ID := "snowstorm-client"
GIT_USER_NAME:= "bncszb"
PACKAGE_VERSION := "0.1.0"
CLIENT_NAME := "SnowstormClient"
AUTHOR_NAME := "Bence Szabó"
AUTHOR_EMAIL := "bszabo96@gmail.com"

_:
    just --list

clean:
    rm -rf ./*.egg-info build/ dist/ __pycache__/ .pytest_cache/
    find . -name "*.pyc" -delete
    find . -name "*.pyo" -delete

alias gc := generate-client

generate-client: clean
    docker run --rm -v "${PWD}:/local/out/python" openapitools/openapi-generator-cli generate \
        -i https://browser.ihtsdotools.org/snowstorm/snomed-ct/v3/api-docs/snowstorm \
        -g python \
        -o /local/out/python \
        --package-name {{PACKAGE_NAME}} \
        --artifact-version {{PACKAGE_VERSION}} \
        --git-user-id {{GIT_USER_NAME}} \
        --git-repo-id {{GIT_REPO_ID}} \
        --library urllib3 \
        --additional-properties=packageUrl=https://github.com/{{GIT_USER_NAME}}/{{GIT_REPO_ID}},packageVersion={{PACKAGE_VERSION}},projectName={{PACKAGE_NAME}},packageCompany="{{AUTHOR_NAME}}",authorName="{{AUTHOR_NAME}}",authorEmail="{{AUTHOR_EMAIL}}",packageDescription="Python client for SNOMED CT Snowstorm API"

# Install the generated package in development mode
install-dev: generate-client
    pip install -e .

# Build the package
build: generate-client
    python -m build

alias c := clean
alias i := install-dev
alias b := build