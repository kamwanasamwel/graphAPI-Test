import json
import facebook

def main():
	token = "EAADuuYgDvzoBAMZBMF2vnOf4wrwNC5RsslRML2XMKsXLSdZCsfkK3UqlCB93ZCpceL177F7nuEvBcnNtAyogoQPYJsbUciqsOi2AZBcPR7koZBsIi7xIHF3KRf4TvvEyjQ40yTOKTsYW1EcZA7J51NZAouOh2OyrO0o0jQ4vq7TZBRJijL3gbvqcEuXoip7aedSZBUU3Npu8sGAZDZD"
	graph = facebook.GraphAPI(token)
	fields = ['first_name, short_name, last_name ,email, birthday, hometown ,gender']
	profile = graph.get_object('me',fields=fields)	
	#return desired fields
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()