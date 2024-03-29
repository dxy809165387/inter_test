

def find(target, datadict, notfound=None):
    queue = [datadict]
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == target:
                return str(value)
            elif type(value) == dict:
                queue.append(value)
    return notfound


def datasort(data_dict):
    request_dict = {}
    for i in data_dict:
        if 'url' in i.keys():
            if i["url"] in request_dict.keys():
                request_dict[i['url']].append(i)
            else:
                request_dict[i['url']] = [i]
    return request_dict


def addrole(data, role):
    datalen = len(list(data))
    return list(zip(list(data), [role]*datalen))
