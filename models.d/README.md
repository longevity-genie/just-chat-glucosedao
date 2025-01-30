# models.d Folder

This folder (`models.d/`) is intended for storing ChatUI models data.

## Usage

- Place any necessary datasets, configuration files, or other required resources in this folder.
- The contents of this folder will be accessible within the container at `/data`.
- Ensure that files stored here are relevant to the agents' operations and do not contain sensitive or unnecessary data.

## Notes

- Files in this directory may be mapped or mounted depending on the container setup.
- The mapping is defined in `docker-compose.yml`, so if you want to alter it, change :

  ```yaml
  volumes:
    - ./data:/data

# 

This folder is automatically populated when application starts.
Don't edit these manually.