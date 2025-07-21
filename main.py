from src.BigQueryHelper import BigQueryHelper
from src.GoogleBucketHelper import GoogleBucketHelper
from src.SecretManagerHelper import SecretManagerHelper


def main():
    print("Hello from google-cloud-helper!")

    project_id = "project_id"
    gch = BigQueryHelper(project_id)

    gch.table_exists("project_id.dataset_id.table_id")

    bh = GoogleBucketHelper(project_id)
    bh.bucket_exists("bucket_name")

    smc = SecretManagerHelper()
    smc.get_secret(project_id, "secret_id")

    import pdb

    pdb.set_trace()


if __name__ == "__main__":
    main()
