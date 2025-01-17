# *SSH: Secure Shell*
> ## *What is SSH (Secure Shell)?*
> ****SSH is a software package that enables secure system administration and file transfers over insecure networks.*** It is used in nearly every data center and in every large enterprise.*

> ## *The SSH protocol*
> ****The SSH protocol uses encryption to secure the connection between a client and a server.*** All user authentication, commands, output, and file transfers are encrypted to protect against attacks in the network.*

*O protocolo SSH (Bloqueio de Segurança) pode ser usado para realizar acesso remoto entre dispositivos através de conexões criptografadas.*
 - *Utilizado para realizar transferências de arquivos por meio do SFTP (SSH File Transfer Protocol ou Secure File Transfer Protocol).*
 - *Utilizado para configurar, gerenciar, monitorar e operar firewalls, roteadores, switches e servidores de redes e ambientes digitais na web.*
 - *Utiliza a porta 22 e é descrito pela RFC 4251.*

> ***The acronym SSH stands for "Secure Shell."*** The SSH protocol was designed as a secure alternative to unsecured remote shell protocols. ***It utilizes a client-server paradigm, in which clients and servers communicate via a secure channel.****

 - *Implementa o serviço de acesso remoto seguro da arquitetura TCP/IP.*
 - *Baseado no modelo Cliente-Servidor.*
 - *Utiliza os serviços de transporte: Com conexão (envio e recebimento de mensagens).*
 - *Provê comunicação segura para:*
    - *Aplicações de terminal remoto;*
    - *Transferência de arquivos;*
    - *Execução remota de comandos.*

> ***The SSH protocol has three layers:***
> - ****The transport layer.*** Ensures secure communication between the server and the client, monitors data encryption/decryption, and protects the integrity of the connection. It also performs data caching and compression.*

 - *Usa os serviços da camada de transporte para permitir a comunicação entre os processos de aplicação.*
    - *Serviço de datagramas;*
    - *Serviço de circuito virtual.*

    *O desenvolvedor da aplicação deve selecionar o serviço de transporte a ser adotado.*
     - *Serviço de transporte sem conexão: Utiliza o protocolo UDP;*
     - *Serviço de transporte com conexão: Utiliza o protocolo TCP.*

> - ****The authentication layer.*** Conducts the client authentication procedure.*
> - ****The connection layer.*** Manages communication channels after the authentication.*

<p align="center">
<img src="ASSETS/SSH_PROTOCOL.png">
</p>

#### *Criptografia assimétrica*
*Existem duas chaves, uma chave pública onde qualquer indivíduo pode criptografar (chave pública), e outra chave privada que apenas o recetor possui para descriptografar a mensagem.*

> ****The channel created by SSH uses public-key cryptography to authenticate the client.*** Once the connection is established, SSH provides an encrypted way to exchange information safely regardless of the underlying network infrastructure.*

<p align="center">
<img src="ASSETS/SSH2.png">
</p>

### *Componentes do Secure Shell:*
 - ****Servidor SSH***: Aceita requisições de clientes SSH, provendo autenticação, privacidade e integridade;*
 - ****Cliente SSH***: Envia requisições ao servidor SSH para abrir a sessão de terminal remoto, transferências de arquivos ou execução de comandos.*
 - ***Protocolo SSH:***
    - *Define um canal seguro de comunicação;*
    - *Adota a porta TCP 22;*
    - *Existem duas versões (SSH-1 e SSH-2).*

### *Chaves de criptografia*
 - ****Chave de estação*** (assimétrica):*
    - *Usada como prova de identidade da estação do servidor;*
    - *Cliente mantém uma base de dados de estações conhecidas.*
 - ****Chave de servidor*** (assimétrica):*
    - *Usada para proteger a chave de sessão;*
    - *Deve ser recriada periodicamente.*
 - ****Chave de sessão*** (simétrica): Usada para cifrar comunicação entre o cliente e o servidor.*

<p align="center">
<img src="ASSETS/SSH_CONNECTION.png">
</p>

> ## *How Secure is SSH?*
> *When used with standard security precautions, the SSH protocol is considered to be highly secure. However, human factors play a significant role in maintaining the security of SSH connections.*
> 
> *Brute force attacks on SSH servers are a common scenario. Attackers attempt to connect to a large number of SSH servers using common usernames and passwords. When they gain access to a server, they use privilege escalation to gain access to the root account.*
> 
> *SSH keys are recommended as a more secure authentication method than passwords. However, poor SSH key management still presents a significant risk to organizations whose critical information depends on keeping the keys secret.*
> 
> *While SSH keys offer better protection, their misuse can provide malicious individuals access to privileged information. This information includes accounts and resources, such as databases, routers, payment systems, etc.*
> 
> *Exposed SSH ports are another potential security weakness. Some malware programs attack IoT devices with ports exposed, using them as a backdoor entrance to the local network.*
> 
> *Lastly, a large number of SSH clients on the market means that the security of the protocol also depends on the security of third-party apps.*
