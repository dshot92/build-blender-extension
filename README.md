# This workflow are in .github/workflows directory.

Github action to build the blender extension and store the resulting .zip artifact.
Use latest linux daily build from blender.org

### Usage
Create a github action in .github/workflows directory of the extension repository.
```yaml
name: Build Extension

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:  # Allows manual triggering from the Actions tab

jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - name: Build Blender Extension
          uses: dshot92/build-blender-extension@main
```

