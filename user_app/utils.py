import base64
from PIL import Image
from io import BytesIO


def raw_upload_file_to_base64(uploaded_file):
	image = Image.open(uploaded_file)

	if image.mode == 'RGBA':
		image = image.convert('RGB')

	output = BytesIO()
	image.save(output, format='JPEG')
	return base64.b64encode(output.getvalue()).decode('utf-8')


def base64_to_image_file(base64_string):
	image_data = base64.b64decode(base64_string)
	return Image.open(BytesIO(image_data))
