_:
    just --list

alias gc := generate-client

generate-client:
    docker run --rm -v "${PWD}:/local/out/python" openapitools/openapi-generator-cli generate \
    -i https://browser.ihtsdotools.org/snowstorm/snomed-ct/v3/api-docs/snowstorm \
    -g python \
    -o /local/out/python
