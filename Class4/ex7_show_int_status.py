from pprint import pprint
import textfsm



template_file = 'ex2_show_int_status.tpl'
template = open(template_file)


with open('ex2_show_int_status.txt') as f:
 raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

table_keys = re_table.header
final_list = []

for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict)


print("#"*50)
pprint(final_list)
print("#"*50)



#Port      Name  Status       Vlan  Duplex Speed Type 
#Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
#Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
