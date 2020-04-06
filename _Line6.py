def solution(directory, command):
    answer = []
    for i in command:
        comm, dirc = i.split(' ')
        if comm == 'mkdir':
            directory.append(dirc)
        elif comm == 'rm':
            directory = [x for x in directory if dirc not in x]
        elif comm == 'cp':
            fromDirc, toDirc = dirc.split(' ')
            directory.append(toDirc+fromDirc)

    return answer

directory = ["/","/hello","/hello/tmp","/root","/root/abcd","/root/abcd/etc","/root/abcd/hello"]
command = ["mkdir /root/tmp","cp /hello /root/tmp", "rm /hello"]