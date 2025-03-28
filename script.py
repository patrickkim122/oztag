import os
import json
import numpy as np

for folder, _, files in os.walk('.'):
    sent = 0
    received = 0
    participants = []
    message_counts = []
    messages_dict = {}
        
    for file in files:
        # if folder.split("_")[0][2:] != "hellasandypnis":
            # continue
        if folder.split("_")[0][2:] != "leosamigos700pmfield12":
            continue
        if file.startswith("message_"):
            file_path = os.path.join(folder, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                        
                    for message in data['messages']:
                        # if 'content' in message:
                        #     print(f"{message['sender_name']}: {message['content']}")
                        # elif 'photos' in message:
                        #     print(f"{message['sender_name']} sent a photo")
                        if message['sender_name'] not in messages_dict:
                            if 'content' in message:
                                messages_dict[message['sender_name']] = len(message['content'])
                            else:
                                messages_dict[message['sender_name']] = 1
                            # participants.append(message['sender_name'])
                            # message_counts.append(1)
                        else:
                            # message_counts[participants.index(message['sender_name'])] += 1
                            if 'content' in message:
                                messages_dict[message['sender_name']] += len(message['content'])
                            else:
                                messages_dict[message['sender_name']] += 1
                    
                        
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error reading file {file_path}: {e}")
                
    keys = list(messages_dict.keys())
    values = list(messages_dict.values())
    sorted_value_index = np.argsort(values)[::-1]
    messages_dict_filtered = {keys[i]: values[i] for i in sorted_value_index}
    for i in messages_dict_filtered:
        print(f"Total characters ({i}): {messages_dict_filtered[i]}")                