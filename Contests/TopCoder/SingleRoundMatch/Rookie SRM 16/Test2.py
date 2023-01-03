class Messaging:
    def getNext(self, messages, time):
        n = len(messages)
        q = []
        ct = 0
        for message in messages:
            mes = message.split()
            t = int(mes[2])
            
            if t > time:
                break
            if t > ct and q:
                k = t - ct
                # print(q)
                # print(k)
                nq = len(q)
                if k >= nq:
                    q = []
                else:
                    q.sort()
                    q = q[:nq-k]
            ct = t
            q.append((int(mes[1]), mes[0]))
        q.sort()
        # print(q)
        k = time - ct + 1
        if k > len(q):
            return ""
        else:
            return q[-k][1]

        
def main():
    messages = ("priority 9 1", "be 3 1", "queues 5 2", "can 4 3", "implemented 1 3", "but 8 7", "in 11 7", "would 2 7", "nlogn 12 8", "yours 21 10", "that 10 10", "slower 18 10", "than 14 11", "can 75 11", "be 50 11", "much 42 13", "be 30 30")
    time = 14

    sol = Messaging()
    print(sol.getNext(messages, time))

if __name__ == '__main__':
    main()