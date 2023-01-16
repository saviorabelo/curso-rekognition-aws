import boto3
from pprint import pprint
from PIL import Image, ImageDraw
from io import BytesIO


def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']


#img_path = r"C:/Users/Savio/Desktop/curso-rekognition-aws/img_test/img (1).jpg"
#img = Image.open(img_path)

buckey = "amazon-rekognition"
img = "test.jpg"
#img = Image.open(BytesIO(img_path))


s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
	print(bucket)

#pprint(detect_labels(buckey, img))



