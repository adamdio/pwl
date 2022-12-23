from minio import Minio
import mdf

#create a client
client = mdf.play_connect()

buckets = client.list_buckets()
for bucket in buckets:
    print("Name:",bucket.name,"Creation date":,bucket.creation_date)