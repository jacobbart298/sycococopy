#SPECIFICATION 

# define roles with keyword role
roles:
    name1
    name2

# define communication protocol with keyword protocol
protocol(name):
    #define the protocol

#send
send type(condition) from p to q 

#receive // LATEN WE NOG EVEN WEG, want receive zou overal tussen moeten komen 
receive type from p to q

#sequenciality
sequence:
    protocol1
    protocol2

#shuffling / TODO think of other term
shuffle:
    protocol1
    protocol2

#choice
choice:
    protocol1
    protocol2

#close channel
close p to q



roles:
    buyer1
    buyer2
    seller

protocol(twobuyer):
    sequence:
        send str from buyer1 to seller
        shuffle:
            send int from seller to buyer1
            send int from seller to buyer2
        send int from buyer1 to buyer2
        send bool from buyer2 to seller
        shuffle:
            close buyer1 to seller
            close buyer1 to buyer2
            close seller to buyer1
            close seller to buyer2
            close buyer2 to seller