'''
You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times that users have clicked on an ad on each individual domain. Every line consists of a click count and a domain name, like this:

counts = [ "900,google.com",
     "60,mail.yahoo.com",
     "10,mobile.sports.yahoo.com",
     "40,sports.yahoo.com",
     "300,yahoo.com",
     "10,stackoverflow.com",
     "20,overflow.com",
     "5,com.com",
     "2,en.wikipedia.org",
     "1,m.wikipedia.org",
     "1,mobile.sports",
     "1,google.co.uk"]

Write a function that takes this input as a parameter and returns a data structure containing the number of clicks that were recorded on each domain AND each subdomain under it. For example, a click on "mail.yahoo.com" counts toward the totals for "mail.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "mail" and "mail.yahoo" are not valid domains. Note that "mobile.sports" appears as a separate domain near the bottom of the input.)

Sample output (in any order/format):

calculateClicksByDomain(counts) =>
com:                     1345
google.com:              900
stackoverflow.com:       10
overflow.com:            20
yahoo.com:               410
mail.yahoo.com:          60
mobile.sports.yahoo.com: 10
sports.yahoo.com:        50
com.com:                 5
org:                     3
wikipedia.org:           3
en.wikipedia.org:        2
m.wikipedia.org:         1
mobile.sports:           1
sports:                  1
uk:                      1
co.uk:                   1
google.co.uk:            1

n: number of domains in the input
(individual domains and subdomains have a constant upper length)
'''

counts = [
    "900,google.com",
    "60,mail.yahoo.com",
    "10,mobile.sports.yahoo.com",
    "40,sports.yahoo.com",
    "300,yahoo.com",
    "10,stackoverflow.com",
    "20,overflow.com",
    "5,com.com",
    "2,en.wikipedia.org",
    "1,m.wikipedia.org",
    "1,mobile.sports",
    "1,google.co.uk" 
]


class Trie:
  def __init__(self):
    self.root = {}
  def add(self, domain, count):
    node = self.root
    print(domain)
    domains = domain.split('.')
    domains = reversed(domains)
    for sub_domain in domains:
      node = node.setdefault(sub_domain,{})
    node['_end_'] = count

def calculateClicksByDomain(counts):
    c_dict = {}
    for i in counts:
        s = i.split(',')
        c_dict[s[1]] = int(s[0]) 

    trie = Trie()
    for k,v in c_dict.items():
        trie.add(k,v)

    def print_trie(trie):
        for k,v in trie.items():
            if k != '_end_':
                print(k,v)
                print_trie(v)
            else:
                print(k,v)
    print_trie(trie.root)

    def trie_counter(trie, domain, domain_dict):
        c = 0
        if '_end_' in trie:
            c += trie['_end_']
        for k,v in trie.items():
            print('k:',k,'v:',v)
            if k != '_end_':
                c += trie_counter(v, domain+'.'+k, domain_dict)
        domain_dict[domain] = c
        return c
    domain_dict = {}
    trie_counter(trie.root, '', domain_dict)  

    
    return domain_dict


d = calculateClicksByDomain(counts)
d_view = [ (v,k) for k,v in d.items() ]
d_view.sort(reverse=True) # natively sort tuples by first element
for v,k in d_view:
    print ("%s: %d" % (k,v))
# com                  
# yahoo 300 , 340    google 900
# sports 40

