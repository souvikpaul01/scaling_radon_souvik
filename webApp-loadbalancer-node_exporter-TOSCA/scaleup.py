import sys
import os

file_to_delete = "/home/ubuntu/opera/xopera-opera/examples/nginx_openstack/webApp-loadbalancer-node_exporter-TOSCA/.opera/instances/nginx-lb_0"
try:
    os.remove(file_to_delete)
   
    os.system('python upscale.py service.yaml service_test.yaml')

#    os.system('opera deploy service_test.yaml')

    print ('File deleted')
except FileNotFoundError:
    print ('File not found:', file_to_delete)


#os.system('python upscale.py service.yaml service_test.yaml')

os.system('opera deploy service_test.yaml')

