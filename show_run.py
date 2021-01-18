import os
from datetime import datetime
from datetime import date
from netmiko import ConnectHandler
import yaml
import time


start_time = datetime.now()
today_date = str(date.today())

#Get yaml dict
with open('test_device.yml', 'r') as ymlfile:
    data = yaml.safe_load(ymlfile)


#Creating log file
log_file = open('log_file.txt', "a")
log_file.write('--------------------START--------------------\n')
log_file.write('Date: ' + today_date + '\n')
log_file.write('Start Time: ' + (str(start_time))+ '\n')

#Connect to device
for device_index in data:
    
    device_name = device_index
    router = data.get(device_index)
      
    try:
        c = ConnectHandler(**router) 
                  
        run_command = c.send_config_set(['<COMMAND>'])
        print(run_command)
        # Open file to write output of the command if it is needed
        f = open('run_conf_'+ device_name +'_' + today_date + 'new.txt', "w")
        c.save_config()
        time.sleep(2)
        # sh_inventory = c.send_command('show inventory')
        f.write(run_command)
        # f.write(sh_inventory)
        f.close()
        c.disconnect()
        work_status = device_name + ' Running Config Downloaded'
        log_file.write('Status: ' + work_status + '\n')        
        print(work_status)
    except Exception as problem:
        work_status = device_name + 'Problem'
        log_file.write('Status: ' + str(problem) + '\n')
        print(work_status)
        print(problem)
    
end_time = datetime.now()
total_time = str(end_time - start_time)

log_file.write('Total Time: ' + total_time + '\n')
log_file.close()


