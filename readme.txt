rsa_signature

Rodrigo Teixeira Soares		19/0019760

O programa rsa_signature é utilizado para cifrar e decifrar mensagens usando uma combinação de cifras AES e RSA.

Ele recebe como entrada uma mensagem de 128 bits (16 caracteres ascii) salva em message.txt previamente.

O programa rsa_signature funciona com os seguintes comandos a depender do caso de uso:

1) Cifra AES

Cifrar uma mensagem em message.txt, gerando uma chave aleatória, salvando-a em key.txt e salvando o resultado em cyphered.txt:

python3 rsa_signature.py 1 c message.txt key.txt cyphered.txt

Decifrar uma mensagem em cyphered.txt utilizando a chave salva em key.txt e salvando o resultado em decyphered.txt:

python3 rsa_signature.py 1 d cyphered.txt key.txt decyphered.txt

2) Cifra mista (AES + RSA):

Cifrar com AES uma mensagem em message.txt, gerando uma chave AES aleatória. Depois, cifrar esta chave com RSA, salvando a chave pública em key.txt e a privada em secret_key.txt. Ao final, salvar a chave cifrada em cyphered_key.txt e a mensagem cifrada em cyphered.txt:

python3 rsa_signature.py 2 c message.txt key.txt secret_key.txt cyphered_key.txt cyphered.txt   

Decifrar uma mensagem cifrada com AES salva em cyphered.txt, utilizando a chave pública salva em key.txt e a privada em secret_key.txt para decifrar a chave AES com RSA salva em cyphered_key.txt, guardando a mensagem decifrada em decyphered.txt:

python3 rsa_signature.py 2 d cyphered.txt key.txt secret_key.txt cyphered_key.txt decyphered.txt

3) Cifra mista com autenticação dupla:

Cifrar com AES uma mensagem em message.txt, gerando uma chave AES aleatória. Depois, cifrar esta chave com RSA, salvando a chave pública em key.txt e a privada em secret_key.txt. Então, assinar a chave cifrada com RSA usando uma nova chave privada (do usuário B), salvando a chave pública equivalente em key_b.txt. Ao final, salvar a chave cifrada e assinada em cyphered_key.txt e a mensagem cifrada em cyphered.txt:

python3 rsa_signature.py 3 c message.txt key.txt secret_key.txt key_b.txt cyphered_key.txt cyphered.txt

Decifrar uma mensagem cifrada com AES salva em cyphered.txt Utilizando a chave pública salva em key.txt e a privada em secret_key.txt para decifrar a chave AES com RSA salva em cyphered_key.txt, revertendo a assinatura previamente com a chave pública salva em key_b.txt, guardando a mensagem decifrada em decyphered.txt:

python3 rsa_signature.py 3 d cyphered.txt key.txt secret_key.txt key_b.txt cyphered_key.txt decyphered.txt

4) Assinatura RSA

Cifrar com AES uma mensagem em message.txt, gerando uma chave AES aleatória. Depois, realizar um hash (SHA3-256) na mensagem cifrada, assinando este hash com a chave privada do RSA, salvando a chave pública em key.txt e a privada em secret_key.txt. Formatar a mensagem assinada em base64. Ao final, salvar a mensagem assinada em signed_message_a.txt e a mensagem cifrada em cyphered.txt:

python3 rsa_signature.py 4 s message.txt key.txt secret_key.txt signed_message_a.txt cyphered.txt         

5) Verificação RSA:

Realizar o hash da mensagem cifrada em cyphered.txt, comparando-o com o resultado da reversão da assinatura RSA salva em signed_message_a.txt, de chave pública key.txt e privada secret_key.txt. Caso os dois hashes coincidam, avisa no console que a assinatura é legítima.

python3 rsa_signature.py 5 v cyphered.txt key.txt secret_key.txt signed_message_a.txt decyphered.txt      







