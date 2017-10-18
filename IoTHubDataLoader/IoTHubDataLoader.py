from D2CMsgSender import IoTDataMsgSender
import time 
from BuildData import BuildData
connectionString = 'HostName=[YourIoTHub].azure-devices.net;DeviceId=[LoadTest];SharedAccessKey=[DeviceKey]'
MessagesToSend = 1000


if __name__ == '__main__':  
    
    IoTHubMsgSender = IoTDataMsgSender(connectionString)
    buildData = BuildData();
    template = buildData.loadTemplate("template.json")
    x = 0
    while(x < MessagesToSend):
        x = x+1
        message = buildData.getDistribution(template)
        sasToken =  IoTHubMsgSender.buildIoTHubSasToken()
        print(IoTHubMsgSender.sendD2CMsg(message,sasToken))
        time.sleep(5)




