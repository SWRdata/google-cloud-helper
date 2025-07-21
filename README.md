# google-cloud-helper

This repository contains common functions for easy access to Google Cloud Infrastructure, such as Big Query or Google buckets.


## Example Usage


```python

from src.BigQueryHelper import BigQueryHelper

gch = BigQueryHelper("project_id")
gch.table_exists("project_id.dataset_id.table_id")
```


## Testing

To run the tests, execute the following command:

```
uv run pytest
```
