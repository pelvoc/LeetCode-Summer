def exclusiveTime(self, N, logs):
    ans = [0] * N
    #stack = SuperStack()
    stack = []

    for log in logs:
        fn, typ, time = log.split(':')
        fn, time = int(fn), int(time)

        if typ == 'start':
            stack.append(time)
        else:
            delta = time - stack.pop() + 1
            ans[fn] += delta
            #stack.add_across(delta)
            stack = [t+delta for t in stack] #inefficient

    return ans