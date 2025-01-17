# *CDP: Cisco Discovery Protocol*
> *CDP ***is a Cisco proprietary protocol that is used for collecting directly connected neighbor device information*** like hardware, software, device name details and many more...*

*O CDP ***é um protocolo da camada 2***, independente de qualquer meio ou rede, ***que*** corre nos dispositivos CISCO e ***permite às aplicações de rede conhecer os dispositivos diretamente ligados***.*

*Este protocolo facilita a gestão dos dispositivos Cisco:*
- *Descobrindo-os (switch, router, servidores, etc);*
- *Determinando como estão configurados;*
- *Permitindo aos diferentes sistemas utilizarem diferentes protocolos
de camada 3 para aprender acerca de cada um.*


> ## *CDP Versions*
> - ****CDPv1***: the initial version which is capable only to collect device information connected to next end.*
> - ****CDPv2***: is the most recent release of the protocol and provides more intelligent device tracking features like instances of mismatch native VLAN IDs on 802.1Q trunks, and mismatch in duplex states between connecting devices.*

## *Como funciona?*
> *All Cisco devices transmit CDP packets periodically (default time interval value is 60 seconds though this is adjustable). These packets advertise a time-to-live (TTL) value in seconds, which indicates the number of seconds that the packet must be retained before it can be discarded (default value is 180 seconds).*
> - *CDP packets are sent with a time-to-live value that is nonzero after an interface is enabled; and*
> - *With a time-to-live value of zero immediately before an interface is down. This provides quick state discovery.*

 - *Cada dispositivo configurado com CDP anuncia pelo menos um endereço, através do qual consegue receber mensagens e envia anúncios periódicos para um endereço multicast conhecido.*
 - *Os dispositivos descobrem-se uns aos outros somente escutando o endereço mencionado.*
 - *Escutam ainda estes anúncios para saber quando uma interface está em cima ou em baixo.*
 - *Os anúncios contêm um TTL, que indica o tempo máximo que um dispositivo Cisco deve manter a informação CDP.*
 - *Os anúncios suportados e configurados em software Cisco, são enviados, por defeito, a cada 60 segundos, nas interfaces que suportam cabeçalhos Subnetwork Access Protocol (SNAP).*
 - *Os dispositivos Cisco nunca reencaminham pacotes CDP.*

> *All Cisco devices receive CDP packets, process them and cache the information in the packet. Cisco devices never forward a CDP packet. If any information changes from the last received packet, the new information is cached and the older information is discarded even if its time-to-live value has not yet expired.*

- *Os dispositivos Cisco que suportam CDP, guardam a informação numa tabela própria para o efeito.*
 - *A informação da tabela é refrescada sempre que é recebido um anúncio.*
 - *Após a falha na receção de 3 anúncios consecutivos, a informação é removida da tabela.*

> ### *CDP Configuration*
> - *CDP is enabled by default on Cisco Device.*
> - *Disabling CDP globally and enabling on an interface is not possible.*
> - *If on and interface CDP is disabled and then the encapsulation of the interface is changed, CDP is re-enabled automatically on that interface even if CDP was previously disabled.*
> 
> | ***Command*** | ***Description*** |
> |-------------------|---------------------------------|
> | ***(config)# cdp run*** | *Enables CDP globally on device.* |
> | ***(config)# no cdp run*** | *Disables CDP globally on device.* |
> | ***(config-if)# cdp enable*** | *Enables CDP on an interface device if CDP is enabled globally.* |
> | ***(config-if)# no cdp enable*** | *Disables CDP on an interface device.* |
> | ***(config)# cdp timer*** | *Specifies CDP packets transmission frequency. Default 60 sec.* |
> | ***(config)# cdp holdtime*** | *Specifies time limit for which a receiving device should hold information before discarding. Default 180 sec.* |

> ### *CDP Spoofing*
> *In CDP spoofing, an attacker sends packet with multicast mac-address (01:00:0c:cc:cc:cc) as destination and various spoofed or fake mac-addresses as source. When a Cisco Device receives these frames it starts to add the information in CDP table and the table will start to build larger because the attacker may sends thousands of CDP frames to the device. If the device is unable to handle this attack there is a probability that the device may crash after a few time that's why it is recommended to disable CDP on interfaces that connects non cisco devices' user station.*