__author__='by Mark Veligod'
import os, json, hashlib, datetime, rsa, pyAesCrypt, pickle
import base64

server_directory=os.curdir+'/server/'
state_directory=os.curdir+'/block_state/'
buffersize=64*1024




def reg_auto(
	login, 
	password,  
	path,
	name, 
	surname, 
	patronymic, 
	registration, 
	residence, 
	data_borth,
	pub_key='',
	private_key='', 
	data_time='', 
	hash_login='',
	hash=''
	):
	(pubkey, privkey) = rsa.newkeys(2048)
	files=sorting(state_directory)
	prev_files=files[-1]
	filename=str(prev_files+1)
	hashing=get_hashing(state_directory, str(prev_files))
	data_time=str(timer())
	foto=load_image(path)
	data_login={
	'login': login,
	'password': password,
	'keys': [pubkey, privkey],
	'datetime': data_time,
	'name_block': filename
	}
	data_passport={
	'name': name,
	'surname': surname,
	'patronymic': patronymic,
	'registration': registration,
	'residence': residence,
	'data_borth': data_borth,
	'data_time': data_time,
	'foto': foto,
	'hash': hashing
	}

	with open(server_directory + login + '.txt', 'wb') as file:
		pickle.dump(data_login, file)
	
	pyAesCrypt.encryptFile(server_directory + login + '.txt', server_directory + login, password, buffersize)
	os.remove(server_directory + login + '.txt')

	data_crypto={}
	for i in data_passport:
		if i == 'hash':
			data_crypto[i]=hashing
		elif i == 'foto':
			data_crypto[i]=foto
		else:
			crypto = rsa.encrypt(data_passport[i].encode('utf-8'), pubkey)
			data_crypto[i]=crypto
		

	with open(state_directory + filename, 'wb') as file:
		pickle.dump(data_crypto, file)


def load_image(filename):
	with open(filename, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
	return encoded_string

def save_image(filename):
	with open('log.jpg','wb') as writeFile:
		writeFile.write(base64.b64decode(filename))


def sorting(directory):
	file=os.listdir(directory)
	return sorted([int(i) for i in file])

def get_hashing(directory, filename):
	file=open(directory+filename, 'rb').read()
	return hashlib.md5(file).hexdigest()

def timer():
	time=datetime.datetime.now()
	return time


def decryption_log(login, password):
	data_logs={}
	files=os.listdir(server_directory)
	for file in files:
		if file == login:
			pyAesCrypt.decryptFile(server_directory+file, server_directory + file +'.txt', password, buffersize)
			with open(server_directory + file +'.txt', 'rb') as f:
				i=pickle.load(f)
			with open('logs', 'wb') as f:
				pickle.dump(i, f)


def decryption():
	data_passport={}
	with open('logs', 'rb') as f:
		i=pickle.load(f)
		keys=i['keys']
		block=i['name_block']
		with open(state_directory+block, 'rb') as asd:
			data_block=pickle.load(asd)
			for dsa in data_block:
				if dsa == 'hash':
					data_passport[dsa]=data_block['hash']
				elif dsa == 'foto':
					data_passport[dsa]=data_block['foto']
				else:
					decrypt=rsa.decrypt(data_block[dsa], keys[1])
					data_passport[dsa]=decrypt.decode('utf-8')
	print(data_passport)			
	return data_passport

def check_block():
	files=sorting(state_directory)
	result=[]
	for file in files[1:]:
		with open(state_directory+str(file), 'rb') as asd:
			now_hash=pickle.load(asd)['hash']
			prev_file=str(file-1)
			prev_hash=get_hashing(state_directory, prev_file)
			if now_hash==prev_hash:
				res='Блок не поврежден'
			else:
				res='Блок поврежден'
			result.append({'Block': prev_file, 'Status': res})
	return result


			
	


# def main():
	# reg_auto(
	# login='kirill', 
	# password='1234', 
	# rep_password='1234', 
	# path=link,
	# name='kirill', 
	# surname='voitovich', 
	# patronymic='maksimovich', 
	# registration='samara', 
	# residence='samara', 
	# data_borth='31.01.2000', 
	# )
	# decryption()
	# check_block()
	# load_image(filename=link)
# 	decryption_log(login='kirill', password='1234')

# if __name__ == '__main__':
# 	main()