"""Cache Config"""
import os

DISKS = {
    "default": "local",
    "local": {
        "driver": "file",
        "path": os.path.join(os.getcwd(), "tests/integrations/storage/uploads/"),
    },
    "s3": {
        "driver": "s3",
        "client": os.getenv("AWS_CLIENT"),
        "secret": os.getenv("AWS_SECRET"),
        "bucket": os.getenv("AWS_BUCKET"),
    },
}
